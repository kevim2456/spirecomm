import time
import random
import copy
import json

from spirecomm.spire.game import Game
from spirecomm.spire.character import Intent, PlayerClass
import spirecomm.spire.card
from spirecomm.spire.screen import RestOption
from spirecomm.communication.action import *
from spirecomm.ai.priorities import *
from spirecomm.RL.a import *


class SimpleAgent:

    def __init__(self, chosen_class=PlayerClass.THE_SILENT):
        self.prev_game = Game()
        self.game = Game()
        self.combat_info = {}
        self.errors = 0
        self.choose_good_card = False
        self.skipped_cards = False
        self.visited_shop = False
        self.map_route = []
        self.chosen_class = chosen_class
        self.priorities = Priority()
        self.change_class(chosen_class)
        self.push_data_callback = None
        self.get_action_callback = None

    def change_class(self, new_class):
        self.chosen_class = new_class
        if self.chosen_class == PlayerClass.THE_SILENT:
            self.priorities = SilentPriority()
        elif self.chosen_class == PlayerClass.IRONCLAD:
            self.priorities = IroncladPriority()
        elif self.chosen_class == PlayerClass.DEFECT:
            self.priorities = DefectPowerPriority()
        else:
            self.priorities = random.choice(list(PlayerClass))

    def handle_error(self, error):
        raise Exception(error)

    def set_dump(self, s = "C:\\Users\\kevinliu.cs08\\Documents\\GitHub\\spirecomm\\combat.json"):
        self.dump_filename = s
        self.dump("test test",'w')

    def dump(self,s,method='a',end='\n'):
        f = open(self.dump_filename,method)
        try: f.write(s)
        except:
            try: f.write(repr(s))
            except: f.write("dump None str object")
        f.write(end)
        f.close()

    def register_push_data_callback(self, callback):
        self.push_data_callback = callback

    def model_train(self):
        self.push_data_callback(self.combat_info)

    def register_get_action_callback(self, callback):
        self.get_action_callback = callback

    def model_get_action(self, turn_n, action_n, turn_info):
        return self.get_action_callback(turn_n, action_n, turn_info)

    def get_combat_start_info(self):
        info = ["act", "current_hp", "floor", "gold", "max_hp"]
        rv = {}
        for i in info:
            rv.update({i:self.game.json_state.get(i)})
        return rv

    def get_combat_end_info(self):
        info = ["current_hp", "gold", "max_hp"]
        rv = {}
        for i in info:
            rv.update({i:self.game.json_state.get(i)})
        return rv

    def get_turn_info(self):
        info = [["combat_state","player"],["combat_state","monsters"]]
        rv = {}
        json_copy = copy.deepcopy(self.game.json_state)
        for i in info:
            rv.update(recur_get(json_copy,i))

        player_info_drop = ["powers","orbs"]
        for k in player_info_drop:
            rv["player"].pop(k)

        monster_info_drop = ["intent", "move_id", "last_move_id", "second_last_move_id", "name", "id", "powers"]
        for k in monster_info_drop:
            for i in range(len(rv["monsters"])):
                rv["monsters"][i].pop(k,None)

        rv.update(recur_get(json_copy,["combat_state","hand"]))
        card_info_drop = ["id","uuid", "rarity", "has_target"]
        for i in rv["hand"]:
            for k in card_info_drop:
                i.pop(k)

        return rv

    def get_combat_info(self):
        false = False
        true = True
        if self.prev_game.in_combat == False and self.game.in_combat == True:
            self.dump('','w',end='')
            self.combat_info.clear()
            self.combat_info["start_info"] = self.get_combat_start_info()
            self.combat_info["turns"] = {}
        if self.game.in_combat:
            n_turn = self.game.turn
            if n_turn != self.prev_game.turn:
                self.combat_info["turns"][n_turn] = {}
            n_action = len(self.combat_info["turns"][n_turn]) + 1
            self.combat_info["turns"][n_turn][n_action] = self.get_turn_info()
            # self.dump(json.dumps(self.combat_info, indent=4))
        if self.prev_game.screen_type==spirecomm.spire.screen.ScreenType["NONE"]:
            if self.game.screen_type==spirecomm.spire.screen.ScreenType["COMBAT_REWARD"]:
                self.combat_info["end_info"] = self.get_combat_end_info()
                self.combat_info["win"] = True
                self.dump(json.dumps(self.combat_info, indent=4),'w')
                self.model_train()
            elif self.game.screen_type==spirecomm.spire.screen.ScreenType["GAME_OVER"]:
                self.combat_info["end_info"] = self.get_combat_end_info()
                self.combat_info["win"] = False
                self.dump(json.dumps(self.combat_info, indent=4),'w')
                self.model_train()

    def get_next_action_in_game(self, game_state):
        self.prev_game = self.game
        self.game = game_state
        self.get_combat_info()
        #time.sleep(0.07)
        if self.game.choice_available:
            return self.handle_screen()
        if self.game.proceed_available:
            return ProceedAction()
        if self.game.play_available:
            if self.game.room_type == "MonsterRoomBoss" and len(self.game.get_real_potions()) > 0:
                potion_action = self.use_next_potion()
                if potion_action is not None:
                    return potion_action
            return self.get_play_card_action()
        if self.game.end_available:
            return EndTurnAction()
        if self.game.cancel_available:
            return CancelAction()

    def get_next_action_out_of_game(self):
        return StartGameAction(self.chosen_class)

    def is_monster_attacking(self):
        for monster in self.game.monsters:
            if monster.intent.is_attack() or monster.intent == Intent.NONE:
                return True
        return False

    def get_incoming_damage(self):
        incoming_damage = 0
        for monster in self.game.monsters:
            if not monster.is_gone and not monster.half_dead:
                if monster.move_adjusted_damage is not None:
                    incoming_damage += monster.move_adjusted_damage * monster.move_hits
                elif monster.intent == Intent.NONE:
                    incoming_damage += 5 * self.game.act
        return incoming_damage

    def get_low_hp_target(self):
        available_monsters = [monster for monster in self.game.monsters if monster.current_hp > 0 and not monster.half_dead and not monster.is_gone]
        best_monster = min(available_monsters, key=lambda x: x.current_hp)
        return best_monster

    def get_high_hp_target(self):
        available_monsters = [monster for monster in self.game.monsters if monster.current_hp > 0 and not monster.half_dead and not monster.is_gone]
        best_monster = max(available_monsters, key=lambda x: x.current_hp)
        return best_monster

    def many_monsters_alive(self):
        available_monsters = [monster for monster in self.game.monsters if monster.current_hp > 0 and not monster.half_dead and not monster.is_gone]
        return len(available_monsters) > 1

    def get_play_card_action(self):
        playable_cards = [card for card in self.game.hand if card.is_playable]
        # zero_cost_cards = [card for card in playable_cards if card.cost == 0]
        # zero_cost_attacks = [card for card in zero_cost_cards if card.type == spirecomm.spire.card.CardType.ATTACK]
        # zero_cost_non_attacks = [card for card in zero_cost_cards if card.type != spirecomm.spire.card.CardType.ATTACK]
        # nonzero_cost_cards = [card for card in playable_cards if card.cost != 0]
        # aoe_cards = [card for card in playable_cards if self.priorities.is_card_aoe(card)]
        # if self.game.player.block > self.get_incoming_damage() - (self.game.act + 4):
        #     offensive_cards = [card for card in nonzero_cost_cards if not self.priorities.is_card_defensive(card)]
        #     if len(offensive_cards) > 0:
        #         nonzero_cost_cards = offensive_cards
        #     else:
        #         nonzero_cost_cards = [card for card in nonzero_cost_cards if not card.exhausts]

        turn_n = len(self.combat_info["turns"])
        action_n = len(self.combat_info["turns"][turn_n])
        if len(playable_cards) == 0:
            self.combat_info["turns"][turn_n][action_n]['action'] = "End Turn"
            return EndTurnAction()

        # if len(zero_cost_non_attacks) > 0:
        #     card_to_play = self.priorities.get_best_card_to_play(zero_cost_non_attacks)
        # elif len(nonzero_cost_cards) > 0:
        #     card_to_play = self.priorities.get_best_card_to_play(nonzero_cost_cards)
        #     if len(aoe_cards) > 0 and self.many_monsters_alive() and card_to_play.type == spirecomm.spire.card.CardType.ATTACK:
        #         card_to_play = self.priorities.get_best_card_to_play(aoe_cards)
        # elif len(zero_cost_attacks) > 0:
        #     card_to_play = self.priorities.get_best_card_to_play(zero_cost_attacks)
        # else:
        #     # This shouldn't happen!
        #     self.combat_info["turns"][turn_n][action_n]['action'] = "End Turn"
        #     return EndTurnAction()

        self.dump("get card play action")
        card_to_play_name = self.model_get_action(turn_n, action_n, self.combat_info["turns"][turn_n][action_n])
        self.dump(repr(type(card_to_play_name)))
        self.dump( card_to_play_name )

        if card_to_play_name == "None":
            self.dump("card to play == None >>> End Turn")
            self.combat_info["turns"][turn_n][action_n]['action'] = "End Turn"
            return EndTurnAction()
        # self.dump("got card play action :"+card_to_play_name,end="\n\n")
        card_to_play = None
        self.dump("hand:")
        for card in self.game.hand:
            self.dump(card.name)
            if card.name == card_to_play_name:
                card_to_play = card
                break

        self.dump("end of print hand")

        self.dump("card to play == Not None")

        if card_to_play.has_target:
            available_monsters = [monster for monster in self.game.monsters if monster.current_hp > 0 and not monster.half_dead and not monster.is_gone]
            if len(available_monsters) == 0:
                self.combat_info["turns"][turn_n][action_n]['action'] = "End Turn"
                self.dump("no monsters >>> End Turn")
                return EndTurnAction()
            if card_to_play.type == spirecomm.spire.card.CardType.ATTACK:
                target = self.get_low_hp_target()
            else:
                target = self.get_high_hp_target()
            self.combat_info["turns"][turn_n][action_n]['action'] = card_to_play.name
            self.dump("play card with target")
            return PlayCardAction(card=card_to_play, target_monster=target)
        else:
            self.combat_info["turns"][turn_n][action_n]['action'] = card_to_play.name
            self.dump("play card without target")
            return PlayCardAction(card=card_to_play)

    def use_next_potion(self):
        for potion in self.game.get_real_potions():
            if potion.can_use:
                if potion.requires_target:
                    return PotionAction(True, potion=potion, target_monster=self.get_low_hp_target())
                else:
                    return PotionAction(True, potion=potion)

    def handle_screen(self):
        if self.game.screen_type == ScreenType.EVENT:
            events_dict = {'Neow Event': 1,'Ancient Writing': 1, 'Augmenter': 2, 'Big Fish': 1, 'Bonfire Spirits': 0, 'The Cleric': 1, 'The Colosseum': 0, 'Council of Ghosts': 1
                , 'Cursed Tome': 1, 'Dead Adventurer': 1, 'Designer In-Spire': 0, 'The Divine Fountain': 0, 'Duplicator': 0, 'Face Trader': 2, 'Falling': 2, 'Forgotten Altar': 2, 'Golden Idol': 1
                , 'Golden Shrine': 0, 'The Joust': 0, 'Knowing Skull': 2, 'Lab': 0, 'The Library': 1, 'Living Wall': 2, 'Masked Bandits': 0, 'Match and Keep!': 0, 'The Mausoleum': 0
                , 'Mind Bloom': 1, 'The Moai Head': 2, 'Mushrooms': 0, 'Mysterious Sphere': 0, 'The Nest': 0, 'A Note For Yourself': 1, 'N\'loth': 2, 'Old Beggar': 0, 'Ominous Forge': 0, 'Pleading Vagrant': 0
                , 'Purifier': 0, 'Scrap Ooze': 1, 'Secret Portal': 0, 'Sensory Stone': 0, 'Shining Light': 0, 'The Ssssserpent': 0, 'Tomb of Lord Red Mask': 0, 'Transmogrifier': 0
                , 'Upgrade Shrine' : 0,'Vampires' : 2,'We Meet Again' : 0,'Wheel of Change' : 0,'Winding Halls' : 1,'Wing Statue' : 0,'The Woman in Blue' : 0,'World of Goop' : 0}
            response = events_dict.get(self.game.screen.event_id)
            if len(self.game.screen.options) == 1:
                return ChooseAction(0)
            elif response != None:
                return ChooseAction(response)
            else:
                return ChooseAction(0)
            """""
            if self.game.screen.event_id in ["Vampires", "Masked Bandits", "Knowing Skull", "Ghosts", "Liars Game", "Golden Idol", "Drug Dealer", "The Library"]:
                return ChooseAction(len(self.game.screen.options) - 1)
            else:
                return ChooseAction(0)
            """""
        elif self.game.screen_type == ScreenType.CHEST:
            return OpenChestAction()
        elif self.game.screen_type == ScreenType.SHOP_ROOM:
            if not self.visited_shop:
                self.visited_shop = True
                return ChooseShopkeeperAction()
            else:
                self.visited_shop = False
                return ProceedAction()
        elif self.game.screen_type == ScreenType.REST:
            return self.choose_rest_option()
        elif self.game.screen_type == ScreenType.CARD_REWARD:
            return self.choose_card_reward()
        elif self.game.screen_type == ScreenType.COMBAT_REWARD:
            for reward_item in self.game.screen.rewards:
                if reward_item.reward_type == RewardType.POTION and self.game.are_potions_full():
                    continue
                elif reward_item.reward_type == RewardType.CARD and self.skipped_cards:
                    continue
                else:
                    return CombatRewardAction(reward_item)
            self.skipped_cards = False
            return ProceedAction()
        elif self.game.screen_type == ScreenType.MAP:
            return self.make_map_choice()
        elif self.game.screen_type == ScreenType.BOSS_REWARD:
            relics = self.game.screen.relics
            best_boss_relic = self.priorities.get_best_boss_relic(relics)
            return BossRewardAction(best_boss_relic)
        elif self.game.screen_type == ScreenType.SHOP_SCREEN:
            if self.game.screen.purge_available and self.game.gold >= self.game.screen.purge_cost:
                return ChooseAction(name="purge")
            for card in self.game.screen.cards:
                if self.game.gold >= card.price and not self.priorities.should_skip(card):
                    return BuyCardAction(card)
            for relic in self.game.screen.relics:
                if self.game.gold >= relic.price:
                    return BuyRelicAction(relic)
            return CancelAction()
        elif self.game.screen_type == ScreenType.GRID:
            if not self.game.choice_available:
                return ProceedAction()
            if self.game.screen.for_upgrade or self.choose_good_card:
                available_cards = self.priorities.get_sorted_cards(self.game.screen.cards)
            else:
                available_cards = self.priorities.get_sorted_cards(self.game.screen.cards, reverse=True)
            num_cards = self.game.screen.num_cards
            return CardSelectAction(available_cards[:num_cards])
        elif self.game.screen_type == ScreenType.HAND_SELECT:
            if not self.game.choice_available:
                return ProceedAction()
            # Usually, we don't want to choose the whole hand for a hand select. 3 seems like a good compromise.
            num_cards = min(self.game.screen.num_cards, 3)
            return CardSelectAction(self.priorities.get_cards_for_action(self.game.current_action, self.game.screen.cards, num_cards))
        else:
            return ProceedAction()

    def choose_rest_option(self):
        rest_options = self.game.screen.rest_options
        if len(rest_options) > 0 and not self.game.screen.has_rested:
            if RestOption.REST in rest_options and self.game.current_hp < self.game.max_hp / 2:
                return RestAction(RestOption.REST)
            elif RestOption.REST in rest_options and self.game.act != 1 and self.game.floor % 17 == 15 and self.game.current_hp < self.game.max_hp * 0.9:
                return RestAction(RestOption.REST)
            elif RestOption.SMITH in rest_options:
                return RestAction(RestOption.SMITH)
            elif RestOption.LIFT in rest_options:
                return RestAction(RestOption.LIFT)
            elif RestOption.DIG in rest_options:
                return RestAction(RestOption.DIG)
            elif RestOption.REST in rest_options and self.game.current_hp < self.game.max_hp:
                return RestAction(RestOption.REST)
            else:
                return ChooseAction(0)
        else:
            return ProceedAction()

    def count_copies_in_deck(self, card):
        count = 0
        for deck_card in self.game.deck:
            if deck_card.card_id == card.card_id:
                count += 1
        return count

    def choose_card_reward(self):
        reward_cards = self.game.screen.cards
        if self.game.screen.can_skip and not self.game.in_combat:
            pickable_cards = [card for card in reward_cards if self.priorities.needs_more_copies(card, self.count_copies_in_deck(card))]
        else:
            pickable_cards = reward_cards
        if len(pickable_cards) > 0:
            potential_pick = self.priorities.get_best_card(pickable_cards)
            return CardRewardAction(potential_pick)
        elif self.game.screen.can_bowl:
            return CardRewardAction(bowl=True)
        else:
            self.skipped_cards = True
            return CancelAction()

    def generate_map_route(self):
        node_rewards = self.priorities.MAP_NODE_PRIORITIES.get(self.game.act)
        best_rewards = {0: {node.x: node_rewards[node.symbol] for node in self.game.map.nodes[0].values()}}
        best_parents = {0: {node.x: 0 for node in self.game.map.nodes[0].values()}}
        min_reward = min(node_rewards.values())
        map_height = max(self.game.map.nodes.keys())
        for y in range(0, map_height):
            best_rewards[y+1] = {node.x: min_reward * 20 for node in self.game.map.nodes[y+1].values()}
            best_parents[y+1] = {node.x: -1 for node in self.game.map.nodes[y+1].values()}
            for x in best_rewards[y]:
                node = self.game.map.get_node(x, y)
                best_node_reward = best_rewards[y][x]
                for child in node.children:
                    test_child_reward = best_node_reward + node_rewards[child.symbol]
                    if test_child_reward > best_rewards[y+1][child.x]:
                        best_rewards[y+1][child.x] = test_child_reward
                        best_parents[y+1][child.x] = node.x
        best_path = [0] * (map_height + 1)
        best_path[map_height] = max(best_rewards[map_height].keys(), key=lambda x: best_rewards[map_height][x])
        for y in range(map_height, 0, -1):
            best_path[y - 1] = best_parents[y][best_path[y]]
        self.map_route = best_path

    def make_map_choice(self):
        if len(self.game.screen.next_nodes) > 0 and self.game.screen.next_nodes[0].y == 0:
            self.generate_map_route()
            self.game.screen.current_node.y = -1
        if self.game.screen.boss_available:
            return ChooseMapBossAction()
        chosen_x = self.map_route[self.game.screen.current_node.y + 1]
        for choice in self.game.screen.next_nodes:
            if choice.x == chosen_x:
                return ChooseMapNodeAction(choice)
        # This should never happen
        return ChooseAction(0)
