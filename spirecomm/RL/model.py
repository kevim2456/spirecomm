from spirecomm.spire.card import CardType

import json
import copy
import random
from pprintpp import pprint as pp
from bidict import bidict

import torch
from torch import tensor
import torch.nn.functional as F


false = False
true = True
dtype = torch.float
card_name_dict = bidict( {
    "None": 0,
    "Bandage Up": 1,
    "Blind": 2,
    "Dark Shackles": 3,
    "Deep Breath": 4,
    "Discovery": 5,
    "Dramatic Entrance": 6,
    "Enlightenment": 7,
    "Finesse": 8,
    "Flash of Steel": 9,
    "Forethought": 10,
    "Good Instincts": 11,
    "Impatience": 12,
    "Jack of All Trades": 13,
    "Madness": 14,
    "Mind Blast": 15,
    "Panacea": 16,
    "Panic Button": 17,
    "Purity": 18,
    "Swift Strike": 19,
    "Trip": 20,
    "Apotheosis": 21,
    "Chrysalis": 22,
    "Hand of Greed": 23,
    "Magnetism": 24,
    "Master of Strategy": 25,
    "Mayhem": 26,
    "Metamorphosis": 27,
    "Panache": 28,
    "Sadistic Nature": 29,
    "Secret Technique": 30,
    "Secret Weapon": 31,
    "The Bomb": 32,
    "Thinking Ahead": 33,
    "Transmutation": 34,
    "Violence": 35,
    "Apparition": 36,
    "Become Almighty": 37,
    "Beta": 38,
    "Bite": 39,
    "Expunger": 40,
    "Fame and Fortune": 41,
    "Insight": 42,
    "J.A.X.": 43,
    "Live Forever": 44,
    "Miracle": 45,
    "Omega": 46,
    "Ritual Dagger": 47,
    "Safety": 48,
    "Shiv": 49,
    "Smite": 50,
    "Through Violence": 51,
    "Bash": 52,
    "Defend": 53,
    "Strike": 54,
    "Anger": 55,
    "Armaments": 56,
    "Body Slam": 57,
    "Clash": 58,
    "Cleave": 59,
    "Clothesline": 60,
    "Flex": 61,
    "Havoc": 62,
    "Headbutt": 63,
    "Heavy Blade": 64,
    "Iron Wave": 65,
    "Perfected Strike": 66,
    "Pommel Strike": 67,
    "Shrug It Off": 68,
    "Sword Boomerang": 69,
    "Thunderclap": 70,
    "True Grit": 71,
    "Twin Strike": 72,
    "Warcry": 73,
    "Wild Strike": 74,
    "Battle Trance": 75,
    "Blood for Blood": 76,
    "Bloodletting": 77,
    "Burning Pact": 78,
    "Carnage": 79,
    "Combust": 80,
    "Dark Embrace": 81,
    "Disarm": 82,
    "Dropkick": 83,
    "Dual Wield": 84,
    "Entrench": 85,
    "Evolve": 86,
    "Feel No Pain": 87,
    "Fire Breathing": 88,
    "Flame Barrier": 89,
    "Ghostly Armor": 90,
    "Hemokinesis": 91,
    "Infernal Blade": 92,
    "Inflame": 93,
    "Intimidate": 94,
    "Metallicize": 95,
    "Power Through": 96,
    "Pummel": 97,
    "Rage": 98,
    "Rampage": 99,
    "Reckless Charge": 100,
    "Rupture": 101,
    "Searing Blow": 102,
    "Second Wind": 103,
    "Seeing Red": 104,
    "Sentinel": 105,
    "Sever Soul": 106,
    "Shockwave": 107,
    "Spot Weakness": 108,
    "Uppercut": 109,
    "Whirlwind": 110,
    "Barricade": 111,
    "Berserk": 112,
    "Bludgeon": 113,
    "Brutality": 114,
    "Corruption": 115,
    "Demon Form": 116,
    "Double Tap": 117,
    "Exhume": 118,
    "Feed": 119,
    "Fiend Fire": 120,
    "Immolate": 121,
    "Impervious": 122,
    "Juggernaut": 123,
    "Limit Break": 124,
    "Offering": 125,
    "Reaper": 126,
    "Bandage Up+": 127,
    "Blind+": 128,
    "Dark Shackles+": 129,
    "Deep Breath+": 130,
    "Discovery+": 131,
    "Dramatic Entrance+": 132,
    "Enlightenment+": 133,
    "Finesse+": 134,
    "Flash of Steel+": 135,
    "Forethought+": 136,
    "Good Instincts+": 137,
    "Impatience+": 138,
    "Jack of All Trades+": 139,
    "Madness+": 140,
    "Mind Blast+": 141,
    "Panacea+": 142,
    "Panic Button+": 143,
    "Purity+": 144,
    "Swift Strike+": 145,
    "Trip+": 146,
    "Apotheosis+": 147,
    "Chrysalis+": 148,
    "Hand of Greed+": 149,
    "Magnetism+": 150,
    "Master of Strategy+": 151,
    "Mayhem+": 152,
    "Metamorphosis+": 153,
    "Panache+": 154,
    "Sadistic Nature+": 155,
    "Secret Technique+": 156,
    "Secret Weapon+": 157,
    "The Bomb+": 158,
    "Thinking Ahead+": 159,
    "Transmutation+": 160,
    "Violence+": 161,
    "Apparition+": 162,
    "Become Almighty+": 163,
    "Beta+": 164,
    "Bite+": 165,
    "Expunger+": 166,
    "Fame and Fortune+": 167,
    "Insight+": 168,
    "J.A.X.+": 169,
    "Live Forever+": 170,
    "Miracle+": 171,
    "Omega+": 172,
    "Ritual Dagger+": 173,
    "Safety+": 174,
    "Shiv+": 175,
    "Smite+": 176,
    "Through Violence+": 177,
    "Bash+": 178,
    "Defend+": 179,
    "Strike+": 180,
    "Anger+": 181,
    "Armaments+": 182,
    "Body Slam+": 183,
    "Clash+": 184,
    "Cleave+": 185,
    "Clothesline+": 186,
    "Flex+": 187,
    "Havoc+": 188,
    "Headbutt+": 189,
    "Heavy Blade+": 190,
    "Iron Wave+": 191,
    "Perfected Strike+": 192,
    "Pommel Strike+": 193,
    "Shrug It Off+": 194,
    "Sword Boomerang+": 195,
    "Thunderclap+": 196,
    "True Grit+": 197,
    "Twin Strike+": 198,
    "Warcry+": 199,
    "Wild Strike+": 200,
    "Battle Trance+": 201,
    "Blood for Blood+": 202,
    "Bloodletting+": 203,
    "Burning Pact+": 204,
    "Carnage+": 205,
    "Combust+": 206,
    "Dark Embrace+": 207,
    "Disarm+": 208,
    "Dropkick+": 209,
    "Dual Wield+": 210,
    "Entrench+": 211,
    "Evolve+": 212,
    "Feel No Pain+": 213,
    "Fire Breathing+": 214,
    "Flame Barrier+": 215,
    "Ghostly Armor+": 216,
    "Hemokinesis+": 217,
    "Infernal Blade+": 218,
    "Inflame+": 219,
    "Intimidate+": 220,
    "Metallicize+": 221,
    "Power Through+": 222,
    "Pummel+": 223,
    "Rage+": 224,
    "Rampage+": 225,
    "Reckless Charge+": 226,
    "Rupture+": 227,
    "Searing Blow+": 228,
    "Second Wind+": 229,
    "Seeing Red+": 230,
    "Sentinel+": 231,
    "Sever Soul+": 232,
    "Shockwave+": 233,
    "Spot Weakness+": 234,
    "Uppercut+": 235,
    "Whirlwind+": 236,
    "Barricade+": 237,
    "Berserk+": 238,
    "Bludgeon+": 239,
    "Brutality+": 240,
    "Corruption+": 241,
    "Demon Form+": 242,
    "Double Tap+": 243,
    "Exhume+": 244,
    "Feed+": 245,
    "Fiend Fire+": 246,
    "Immolate+": 247,
    "Impervious+": 248,
    "Juggernaut+": 249,
    "Limit Break+": 250,
    "Offering+": 251,
    "Reaper+": 252,
    "Clumsy": 253,
    "Decay": 254,
    "Doubt": 255,
    "Injury": 256,
    "Normality": 257,
    "Pain": 258,
    "Parasite": 259,
    "Regret": 260,
    "Shame": 261,
    "Writhe": 262,
    "Ascender's Bane": 263,
    "Curse of the Bell": 264,
    "Necronomicurse": 265,
    "Pride": 266,
    "Burn": 267,
    "Dazed": 268,
    "Slimed": 269,
    "Void": 270,
    "Wound": 271
} )
EPSILON = 0.7

def flatten_list(data):
    flat = []
    def f(data):
    # iterating over the data
        for element in data:
            # checking for list
            if type(element) == list:
                # calling the same function with current element as new argument
                f(element)
            else:
                flat.append(element)
    f(data)
    return flat

class Net(torch.nn.Module):
    def __init__(self, n_feature, n_hidden, n_output):
        super(Net, self).__init__()
        self.hidden1 = torch.nn.Linear(n_feature, n_hidden)  # hidden layer
        self.hidden2 = torch.nn.Linear(n_hidden, n_hidden)   # hidden layer
        self.hidden3 = torch.nn.Linear(n_hidden, n_hidden)   # hidden layer
        self.hidden4 = torch.nn.Linear(n_hidden, n_hidden)   # hidden layer
        self.predict = torch.nn.Linear(n_hidden, n_output)   # output layer

    def forward(self, x):
        x = F.relu(self.hidden1(x))      # activation function for hidden layer
        x = F.relu(self.hidden2(x))      # activation function for hidden layer
        x = F.relu(self.hidden3(x))      # activation function for hidden layer
        x = F.relu(self.hidden4(x))      # activation function for hidden layer
        x = F.softmax(self.predict(x), dim=0)             # linear output
        return x

class Model:
    def __init__(self):
        self.dump_filename = None
        self.reward = 0
        self.n_feature = 2936
        self.n_hidden = 50
        self.n_output = len(card_name_dict)+1
        self.net = Net(n_feature=self.n_feature, n_hidden=self.n_hidden, n_output=self.n_output)
        self.optimizer = torch.optim.SGD(self.net.parameters(), lr=0.0002)
        self.loss_func = torch.nn.MSELoss()
        self.set_dump()

    def set_dump(self, s = "C:\\Users\\kevinliu.cs08\\Documents\\GitHub\\spirecomm\\model.json"):
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

    def get_data(self, combat_info):
        self.combat_info = copy.deepcopy(combat_info)
        self.dump("hello world")
        self.calc_combat_reward()
        self.dump("done calc combat reward")
        self.encode_empty_card( self.combat_info["turns"][1][1] )
        self.dump("done encode empty card")
        self.encode_decision()

    def give_action(self, turn_k, situ_k, turn_info):
        self.dump("in give_action")
        if random.uniform(0,1) < EPSILON:   # greedy
            self.dump("NN output")
            self.encode_empty_card(turn_info)
            player = torch.tensor( [i for i in turn_info["player"].values()], dtype=dtype )
            monsters = self.encode_monster_data(turn_info)
            hand_input = self.encode_card_data(turn_info,"hand")
            action = torch.cat( (tensor([turn_k,situ_k]),player,monsters,hand_input), 0)

            out = self.net(action)
            hand_weight = self.encode_hand_weight(turn_info)
            rlt = out*hand_weight
            card_to_play_name = card_name_dict.inverse.get(torch.argmax(rlt).item(), "None")

            return card_to_play_name
        else:
            self.dump("random output")
            cards = [i["name"] for i in turn_info["hand"] if i["is_playable"]] + ["None"]
            self.dump(cards)
            card = random.choice(cards)
            self.dump(card)
            return card

    def calc_combat_reward(self):
        hp_gain = self.combat_info["end_info"]["current_hp"] - self.combat_info["start_info"]["current_hp"]
        # max_hp = self.combat_info["end_info"]["max_hp"] - self.combat_info["start_info"]["max_hp"]
        # gold   = self.combat_info["end_info"]["gold"] - self.combat_info["start_info"]["gold"]
        # turn_n = len(self.combat_info["turns"])
        # floor  = self.combat_info["start_info"]["floor"]
        # win    = 10 if self.combat_info["win"] else 0
        # reward = (3*hp, max_hp, gold, -turn_n, 100*floor**0.33)
        if hp_gain > 20 : hp_gain = 20
        elif hp_gain < -80 : hp_gain = -80
        self.reward = (hp_gain+80)/100

    def encode_monster_data(self, tmp):
        name = "monsters"
        max_n = 10 #max_monster_num
        num = len(tmp[name])
        if num > max_n :
            self.dump("Error: num of monsters exceeds max_n")
            return tensor([])
        rv = []
        for i in range(max_n):
            if i < num:
                rv.append([ True ]+[ i for i in tmp[name][i].values()])
            else:
                rv.append([ False ]+[ 0 for _ in range(len(tmp[name][0]))])
        return torch.tensor(flatten_list(rv))

    def encode_card_data_feature(self, key, value):
        table = {
            "name": card_name_dict,
            "type": {
                "ATTACK": 1,
                'SKILL': 2,
                'POWER': 3,
                'STATUS': 4,
                'CURSE': 5
            },
        }
        if key in table.keys():
            rv = [False]*(len(table[key])+1)
            rv[table[key].get(value,False)] = True
            return rv
        else:
            return value

    def encode_empty_card(self,tmp):
        self.dump("in encode_empty_card")
        self.empty_card_tensor = torch.cat(
            (
                tensor([False]),
                tensor( flatten_list( [ self.encode_card_data_feature(k,0) for k,v in tmp["hand"][0].items() ]))
            ),
            0
        )
        self.dump("done encode_empty_card")

    def encode_card_data(self, tmp, name):
        max_n = 10
        num = len(tmp[name])
        if num > max_n :
            self.dump("Error: num of card exceeds max_n")
            return tensor([])
        rv = tensor([],dtype=dtype)
        for i in range(max_n):
            if i < num:
                rv = torch.cat(
                    (
                        rv,
                        tensor([True], dtype=dtype),
                        tensor( flatten_list( [self.encode_card_data_feature(k,v) for k,v in tmp[name][i].items()] ), dtype=dtype )
                    ), 0
                )
            else:
                rv = torch.cat( (rv, self.empty_card_tensor), 0)
        return rv

    def encode_hand_weight(self, tmp):
        rv = torch.zeros( len(card_name_dict) + 1 )
        rv[0] = 1
        for i in tmp["hand"]:
            if i["is_playable"]:
                rv[ card_name_dict.get(i["name"], 0) ] = 1
        return rv

    def encode_action_with_reward(self, the_card_name, weight, hand_size_minus_one):
        weight = weight*(1-self.reward) / hand_size_minus_one
        weight[ card_name_dict.inverse.get(the_card_name,0) ] = self.reward
        return weight

    def encode_decision(self):
        self.dump('hello encode decision','w')

        for turn_k in self.combat_info["turns"].keys():
            for situ_k in self.combat_info["turns"][turn_k].keys():
                self.dump(str(turn_k)+', '+str(situ_k), end=' :\n')
                tmp = self.combat_info["turns"][turn_k][situ_k]

                player = torch.tensor( [i for i in tmp["player"].values()], dtype=dtype )
                monsters = self.encode_monster_data(tmp)
                hand_input = self.encode_card_data(tmp,"hand")
                # print(len(player),len(monsters),len(hand))
                action = torch.cat( (tensor([int(turn_k),int(situ_k)]),player,monsters,hand_input), 0)

                self.dump(len(action))

                out = self.net(action)
                hand_weight = self.encode_hand_weight(tmp)
                hand_size_minus_one = sum(hand_weight)-1
                rlt = out*hand_weight
                reward = self.encode_action_with_reward(tmp.get("action","None"), hand_weight, hand_size_minus_one)

                # print(reward)

                loss = self.loss_func(out, reward)
                self.optimizer.zero_grad()   # clear gradients for next train
                loss.backward()         # backpropagation, compute gradients
                self.optimizer.step()        # apply gradients

                # self.dump( card_name_dict.inverse.get(torch.argmax(rlt).item(), "None") )
                # self.dump( card_name_dict.get(2, "None") )
        self.dump("end a combat")

if __name__ == '__main__':
    m = Model()
    t = {
    "start_info": {
        "act": 2,
        "current_hp": 56,
        "floor": 28,
        "gold": 276,
        "max_hp": 80
    },
    "turns": {
        "1": {
            "1": {
                "player": {
                    "current_hp": 56,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 4
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "half_dead": false,
                        "current_hp": 161,
                        "block": 0,
                        "max_hp": 164
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": -2,
                        "name": "Writhe",
                        "type": "CURSE",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Disarm+",
                        "type": "SKILL",
                        "upgrades": 1
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Shrug It Off+",
                        "type": "SKILL",
                        "upgrades": 1
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Pommel Strike+",
                        "type": "ATTACK",
                        "upgrades": 1
                    }
                ]
            },
            "2": {
                "player": {
                    "current_hp": 56,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "half_dead": false,
                        "current_hp": 161,
                        "block": 0,
                        "max_hp": 164
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": -2,
                        "name": "Writhe",
                        "type": "CURSE",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Shrug It Off+",
                        "type": "SKILL",
                        "upgrades": 1
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Pommel Strike+",
                        "type": "ATTACK",
                        "upgrades": 1
                    }
                ]
            },
            "3": {
                "player": {
                    "current_hp": 56,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 2
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "half_dead": false,
                        "current_hp": 151,
                        "block": 0,
                        "max_hp": 164
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": -2,
                        "name": "Writhe",
                        "type": "CURSE",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Shrug It Off+",
                        "type": "SKILL",
                        "upgrades": 1
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Immolate+",
                        "type": "ATTACK",
                        "upgrades": 1
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    }
                ]
            },
            "4": {
                "player": {
                    "current_hp": 56,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 0
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "half_dead": false,
                        "current_hp": 123,
                        "block": 0,
                        "max_hp": 164
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": -2,
                        "name": "Writhe",
                        "type": "CURSE",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Shrug It Off+",
                        "type": "SKILL",
                        "upgrades": 1
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    }
                ]
            }
        },
        "2": {
            "1": {
                "player": {
                    "current_hp": 50,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 4
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "half_dead": false,
                        "current_hp": 120,
                        "block": 0,
                        "max_hp": 164
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Iron Wave",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": -1,
                        "name": "Whirlwind+",
                        "type": "ATTACK",
                        "upgrades": 1
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 0,
                        "name": "Panic Button",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            },
            "2": {
                "player": {
                    "current_hp": 50,
                    "block": 30,
                    "max_hp": 80,
                    "energy": 4
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "half_dead": false,
                        "current_hp": 120,
                        "block": 0,
                        "max_hp": 164
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Iron Wave",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": -1,
                        "name": "Whirlwind+",
                        "type": "ATTACK",
                        "upgrades": 1
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            },
            "3": {
                "player": {
                    "current_hp": 50,
                    "block": 30,
                    "max_hp": 80,
                    "energy": 0
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "half_dead": false,
                        "current_hp": 88,
                        "block": 0,
                        "max_hp": 164
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Iron Wave",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            }
        },
        "3": {
            "1": {
                "player": {
                    "current_hp": 50,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 4
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "half_dead": false,
                        "current_hp": 85,
                        "block": 0,
                        "max_hp": 164
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 0,
                        "name": "Flex",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Inflame+",
                        "type": "POWER",
                        "upgrades": 1
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            },
            "2": {
                "player": {
                    "current_hp": 50,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 4
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "half_dead": false,
                        "current_hp": 85,
                        "block": 0,
                        "max_hp": 164
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Inflame+",
                        "type": "POWER",
                        "upgrades": 1
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            },
            "3": {
                "player": {
                    "current_hp": 50,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "half_dead": false,
                        "current_hp": 85,
                        "block": 0,
                        "max_hp": 164
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            },
            "4": {
                "player": {
                    "current_hp": 50,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 2
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "half_dead": false,
                        "current_hp": 74,
                        "block": 0,
                        "max_hp": 164
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            },
            "5": {
                "player": {
                    "current_hp": 50,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 1
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "half_dead": false,
                        "current_hp": 63,
                        "block": 0,
                        "max_hp": 164
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            },
            "6": {
                "player": {
                    "current_hp": 50,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 0
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "half_dead": false,
                        "current_hp": 52,
                        "block": 0,
                        "max_hp": 164
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 2,
                        "name": "Perfected Strike+",
                        "type": "ATTACK",
                        "upgrades": 1
                    }
                ]
            }
        },
        "4": {
            "1": {
                "player": {
                    "current_hp": 32,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 4
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "half_dead": false,
                        "current_hp": 49,
                        "block": 0,
                        "max_hp": 164
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Bash",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": -2,
                        "name": "Burn",
                        "type": "STATUS",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Perfected Strike+",
                        "type": "ATTACK",
                        "upgrades": 1
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": -2,
                        "name": "Wound",
                        "type": "STATUS",
                        "upgrades": 0
                    }
                ]
            },
            "2": {
                "player": {
                    "current_hp": 32,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 2
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "half_dead": false,
                        "current_hp": 19,
                        "block": 0,
                        "max_hp": 164
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Bash",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": -2,
                        "name": "Burn",
                        "type": "STATUS",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": -2,
                        "name": "Wound",
                        "type": "STATUS",
                        "upgrades": 0
                    }
                ]
            },
            "3": {
                "player": {
                    "current_hp": 32,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 0
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "half_dead": false,
                        "current_hp": 8,
                        "block": 0,
                        "max_hp": 164
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": -2,
                        "name": "Burn",
                        "type": "STATUS",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": -2,
                        "name": "Wound",
                        "type": "STATUS",
                        "upgrades": 0
                    }
                ]
            }
        },
        "5": {
            "1": {
                "player": {
                    "current_hp": 18,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 4
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "half_dead": false,
                        "current_hp": 5,
                        "block": 0,
                        "max_hp": 164
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Iron Wave",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 0,
                        "name": "Flex",
                        "type": "SKILL",
                        "upgrades": 0
                    }
                ]
            },
            "2": {
                "player": {
                    "current_hp": 18,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 4
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "half_dead": false,
                        "current_hp": 5,
                        "block": 0,
                        "max_hp": 164
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Iron Wave",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    }
                ]
            }
        }
    },
    "end_info": {
        "current_hp": 24,
        "gold": 276,
        "max_hp": 80
    },
    "win": true
} # 2864
    t2 = {
    "start_info": {
        "act": 1,
        "current_hp": 80,
        "floor": 1,
        "gold": 99,
        "max_hp": 80
    },
    "turns": {
        "1": {
            "1": {
                "player": {
                    "current_hp": 80,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 5,
                        "half_dead": false,
                        "move_adjusted_damage": 5,
                        "max_hp": 11,
                        "current_hp": 11,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 7,
                        "half_dead": false,
                        "move_adjusted_damage": 7,
                        "max_hp": 30,
                        "current_hp": 30,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    }
                ]
            },
            "2": {
                "player": {
                    "current_hp": 80,
                    "block": 5,
                    "max_hp": 80,
                    "energy": 2
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 5,
                        "half_dead": false,
                        "move_adjusted_damage": 5,
                        "max_hp": 11,
                        "current_hp": 11,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 7,
                        "half_dead": false,
                        "move_adjusted_damage": 7,
                        "max_hp": 30,
                        "current_hp": 30,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    }
                ]
            },
            "3": {
                "player": {
                    "current_hp": 80,
                    "block": 10,
                    "max_hp": 80,
                    "energy": 1
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 5,
                        "half_dead": false,
                        "move_adjusted_damage": 5,
                        "max_hp": 11,
                        "current_hp": 11,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 7,
                        "half_dead": false,
                        "move_adjusted_damage": 7,
                        "max_hp": 30,
                        "current_hp": 30,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            },
            "4": {
                "player": {
                    "current_hp": 80,
                    "block": 10,
                    "max_hp": 80,
                    "energy": 0
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 5,
                        "half_dead": false,
                        "move_adjusted_damage": 5,
                        "max_hp": 11,
                        "current_hp": 5,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 7,
                        "half_dead": false,
                        "move_adjusted_damage": 7,
                        "max_hp": 30,
                        "current_hp": 30,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            }
        },
        "2": {
            "1": {
                "player": {
                    "current_hp": 78,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 5,
                        "half_dead": false,
                        "move_adjusted_damage": 5,
                        "max_hp": 11,
                        "current_hp": 5,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 30,
                        "current_hp": 30,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Bash",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    }
                ]
            },
            "2": {
                "player": {
                    "current_hp": 78,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 1
                },
                "monsters": [
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": 5,
                        "half_dead": false,
                        "move_adjusted_damage": 5,
                        "max_hp": 11,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 30,
                        "current_hp": 30,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    }
                ]
            },
            "3": {
                "player": {
                    "current_hp": 78,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 0
                },
                "monsters": [
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": 5,
                        "half_dead": false,
                        "move_adjusted_damage": 5,
                        "max_hp": 11,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 30,
                        "current_hp": 24,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    }
                ]
            }
        },
        "3": {
            "1": {
                "player": {
                    "current_hp": 78,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": 5,
                        "half_dead": false,
                        "move_adjusted_damage": 5,
                        "max_hp": 11,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 7,
                        "half_dead": false,
                        "move_adjusted_damage": 7,
                        "max_hp": 30,
                        "current_hp": 24,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            },
            "2": {
                "player": {
                    "current_hp": 78,
                    "block": 5,
                    "max_hp": 80,
                    "energy": 2
                },
                "monsters": [
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": 5,
                        "half_dead": false,
                        "move_adjusted_damage": 5,
                        "max_hp": 11,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 7,
                        "half_dead": false,
                        "move_adjusted_damage": 7,
                        "max_hp": 30,
                        "current_hp": 24,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            },
            "3": {
                "player": {
                    "current_hp": 78,
                    "block": 5,
                    "max_hp": 80,
                    "energy": 1
                },
                "monsters": [
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": 5,
                        "half_dead": false,
                        "move_adjusted_damage": 5,
                        "max_hp": 11,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 7,
                        "half_dead": false,
                        "move_adjusted_damage": 7,
                        "max_hp": 30,
                        "current_hp": 20,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            },
            "4": {
                "player": {
                    "current_hp": 78,
                    "block": 5,
                    "max_hp": 80,
                    "energy": 0
                },
                "monsters": [
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": 5,
                        "half_dead": false,
                        "move_adjusted_damage": 5,
                        "max_hp": 11,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 7,
                        "half_dead": false,
                        "move_adjusted_damage": 7,
                        "max_hp": 30,
                        "current_hp": 16,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            }
        },
        "4": {
            "1": {
                "player": {
                    "current_hp": 76,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": 5,
                        "half_dead": false,
                        "move_adjusted_damage": 5,
                        "max_hp": 11,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 30,
                        "current_hp": 16,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Bash",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            },
            "2": {
                "player": {
                    "current_hp": 76,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 1
                },
                "monsters": [
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": 5,
                        "half_dead": false,
                        "move_adjusted_damage": 5,
                        "max_hp": 11,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 30,
                        "current_hp": 8,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            }
        }
    },
    "end_info": {
        "current_hp": 80,
        "gold": 99,
        "max_hp": 80
    },
    "win": true
} # 4 45 2839 => 2879
    t3 = {
    "start_info": {
        "act": 1,
        "current_hp": 56,
        "floor": 16,
        "gold": 137,
        "max_hp": 80
    },
    "turns": {
        "1": {
            "1": {
                "player": {
                    "current_hp": 56,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 140,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 0,
                        "name": "Offering+",
                        "type": "SKILL",
                        "upgrades": 1
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            },
            "2": {
                "player": {
                    "current_hp": 56,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 140,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 0,
                        "name": "Offering+",
                        "type": "SKILL",
                        "upgrades": 1
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            },
            "3": {
                "player": {
                    "current_hp": 56,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 140,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 0,
                        "name": "Offering+",
                        "type": "SKILL",
                        "upgrades": 1
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            },
            "4": {
                "player": {
                    "current_hp": 56,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 140,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 0,
                        "name": "Offering+",
                        "type": "SKILL",
                        "upgrades": 1
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            },
            "5": {
                "player": {
                    "current_hp": 56,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 140,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 0,
                        "name": "Offering+",
                        "type": "SKILL",
                        "upgrades": 1
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 0,
                        "name": "Metallicize",
                        "type": "POWER",
                        "upgrades": 0
                    }
                ]
            },
            "6": {
                "player": {
                    "current_hp": 50,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 5
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 140,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 0,
                        "name": "Metallicize",
                        "type": "POWER",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Perfected Strike+",
                        "type": "ATTACK",
                        "upgrades": 1
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Impervious+",
                        "type": "SKILL",
                        "upgrades": 1
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Shrug It Off",
                        "type": "SKILL",
                        "upgrades": 0
                    }
                ]
            },
            "7": {
                "player": {
                    "current_hp": 50,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 5
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 140,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Perfected Strike+",
                        "type": "ATTACK",
                        "upgrades": 1
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Impervious+",
                        "type": "SKILL",
                        "upgrades": 1
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Shrug It Off",
                        "type": "SKILL",
                        "upgrades": 0
                    }
                ]
            },
            "8": {
                "player": {
                    "current_hp": 50,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 111,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Impervious+",
                        "type": "SKILL",
                        "upgrades": 1
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Shrug It Off",
                        "type": "SKILL",
                        "upgrades": 0
                    }
                ]
            },
            "9": {
                "player": {
                    "current_hp": 50,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 2
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 100,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Impervious+",
                        "type": "SKILL",
                        "upgrades": 1
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Shrug It Off",
                        "type": "SKILL",
                        "upgrades": 0
                    }
                ]
            },
            "10": {
                "player": {
                    "current_hp": 50,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 1
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 89,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": false,
                        "cost": 2,
                        "name": "Impervious+",
                        "type": "SKILL",
                        "upgrades": 1
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Shrug It Off",
                        "type": "SKILL",
                        "upgrades": 0
                    }
                ]
            },
            "11": {
                "player": {
                    "current_hp": 50,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 0
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 78,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": false,
                        "cost": 2,
                        "name": "Impervious+",
                        "type": "SKILL",
                        "upgrades": 1
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Shrug It Off",
                        "type": "SKILL",
                        "upgrades": 0
                    }
                ]
            }
        },
        "2": {
            "1": {
                "player": {
                    "current_hp": 50,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 78,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Bash",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": -1,
                        "name": "Whirlwind+",
                        "type": "ATTACK",
                        "upgrades": 1
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Impervious+",
                        "type": "SKILL",
                        "upgrades": 1
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            },
            "2": {
                "player": {
                    "current_hp": 50,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 1
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 70,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": -1,
                        "name": "Whirlwind+",
                        "type": "ATTACK",
                        "upgrades": 1
                    },
                    {
                        "exhausts": true,
                        "is_playable": false,
                        "cost": 2,
                        "name": "Impervious+",
                        "type": "SKILL",
                        "upgrades": 1
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            },
            "3": {
                "player": {
                    "current_hp": 50,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 0
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 58,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": false,
                        "cost": 2,
                        "name": "Impervious+",
                        "type": "SKILL",
                        "upgrades": 1
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            }
        },
        "3": {
            "1": {
                "player": {
                    "current_hp": 50,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 58,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 58,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Perfected Strike+",
                        "type": "ATTACK",
                        "upgrades": 1
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Shrug It Off",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            },
            "2": {
                "player": {
                    "current_hp": 50,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 1
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 34,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 58,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Shrug It Off",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            },
            "3": {
                "player": {
                    "current_hp": 50,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 0
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 28,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 58,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": true,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Shrug It Off",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            }
        },
        "4": {
            "1": {
                "player": {
                    "current_hp": 50,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 28,
                        "current_hp": 28,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 8,
                        "half_dead": false,
                        "move_adjusted_damage": 8,
                        "max_hp": 28,
                        "current_hp": 28,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 58,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    }
                ]
            },
            "2": {
                "player": {
                    "current_hp": 50,
                    "block": 5,
                    "max_hp": 80,
                    "energy": 2
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 28,
                        "current_hp": 28,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 8,
                        "half_dead": false,
                        "move_adjusted_damage": 8,
                        "max_hp": 28,
                        "current_hp": 28,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 58,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    }
                ]
            },
            "3": {
                "player": {
                    "current_hp": 50,
                    "block": 5,
                    "max_hp": 80,
                    "energy": 1
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 28,
                        "current_hp": 24,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 8,
                        "half_dead": false,
                        "move_adjusted_damage": 8,
                        "max_hp": 28,
                        "current_hp": 28,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 58,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    }
                ]
            },
            "4": {
                "player": {
                    "current_hp": 50,
                    "block": 5,
                    "max_hp": 80,
                    "energy": 0
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 28,
                        "current_hp": 20,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 8,
                        "half_dead": false,
                        "move_adjusted_damage": 8,
                        "max_hp": 28,
                        "current_hp": 28,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 58,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": true,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    }
                ]
            }
        },
        "5": {
            "1": {
                "player": {
                    "current_hp": 50,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 28,
                        "current_hp": 20,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 28,
                        "current_hp": 28,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 16,
                        "half_dead": false,
                        "move_adjusted_damage": 16,
                        "max_hp": 58,
                        "current_hp": 58,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Shrug It Off",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Impervious+",
                        "type": "SKILL",
                        "upgrades": 1
                    }
                ]
            },
            "2": {
                "player": {
                    "current_hp": 50,
                    "block": 6,
                    "max_hp": 80,
                    "energy": 2
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 28,
                        "current_hp": 20,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 28,
                        "current_hp": 28,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 16,
                        "half_dead": false,
                        "move_adjusted_damage": 16,
                        "max_hp": 58,
                        "current_hp": 58,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Impervious+",
                        "type": "SKILL",
                        "upgrades": 1
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            },
            "3": {
                "player": {
                    "current_hp": 50,
                    "block": 36,
                    "max_hp": 80,
                    "energy": 0
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 28,
                        "current_hp": 20,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 28,
                        "current_hp": 28,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 16,
                        "half_dead": false,
                        "move_adjusted_damage": 16,
                        "max_hp": 58,
                        "current_hp": 58,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            }
        },
        "6": {
            "1": {
                "player": {
                    "current_hp": 50,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 8,
                        "half_dead": false,
                        "move_adjusted_damage": 8,
                        "max_hp": 28,
                        "current_hp": 20,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 28,
                        "current_hp": 28,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 58,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Bash",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Perfected Strike+",
                        "type": "ATTACK",
                        "upgrades": 1
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    }
                ]
            },
            "2": {
                "player": {
                    "current_hp": 50,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 1
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 8,
                        "half_dead": false,
                        "move_adjusted_damage": 8,
                        "max_hp": 28,
                        "current_hp": 2,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 28,
                        "current_hp": 28,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 58,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 2,
                        "name": "Bash",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    }
                ]
            },
            "3": {
                "player": {
                    "current_hp": 50,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 0
                },
                "monsters": [
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": 8,
                        "half_dead": false,
                        "move_adjusted_damage": 8,
                        "max_hp": 28,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 28,
                        "current_hp": 28,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 58,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 2,
                        "name": "Bash",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    }
                ]
            }
        },
        "7": {
            "1": {
                "player": {
                    "current_hp": 50,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": 8,
                        "half_dead": false,
                        "move_adjusted_damage": 8,
                        "max_hp": 28,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 8,
                        "half_dead": false,
                        "move_adjusted_damage": 8,
                        "max_hp": 28,
                        "current_hp": 28,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 16,
                        "half_dead": false,
                        "move_adjusted_damage": 16,
                        "max_hp": 58,
                        "current_hp": 58,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": -1,
                        "name": "Whirlwind+",
                        "type": "ATTACK",
                        "upgrades": 1
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    }
                ]
            },
            "2": {
                "player": {
                    "current_hp": 50,
                    "block": 3,
                    "max_hp": 80,
                    "energy": 2
                },
                "monsters": [
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": 8,
                        "half_dead": false,
                        "move_adjusted_damage": 8,
                        "max_hp": 28,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 8,
                        "half_dead": false,
                        "move_adjusted_damage": 8,
                        "max_hp": 28,
                        "current_hp": 28,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 16,
                        "half_dead": false,
                        "move_adjusted_damage": 16,
                        "max_hp": 58,
                        "current_hp": 58,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": -1,
                        "name": "Whirlwind+",
                        "type": "ATTACK",
                        "upgrades": 1
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            },
            "3": {
                "player": {
                    "current_hp": 50,
                    "block": 3,
                    "max_hp": 80,
                    "energy": 0
                },
                "monsters": [
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": 8,
                        "half_dead": false,
                        "move_adjusted_damage": 8,
                        "max_hp": 28,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 8,
                        "half_dead": false,
                        "move_adjusted_damage": 8,
                        "max_hp": 28,
                        "current_hp": 16,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 16,
                        "half_dead": false,
                        "move_adjusted_damage": 16,
                        "max_hp": 58,
                        "current_hp": 46,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            }
        },
        "8": {
            "1": {
                "player": {
                    "current_hp": 36,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": 8,
                        "half_dead": false,
                        "move_adjusted_damage": 8,
                        "max_hp": 28,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 28,
                        "current_hp": 16,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 46,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Shrug It Off",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    }
                ]
            },
            "2": {
                "player": {
                    "current_hp": 36,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 2
                },
                "monsters": [
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": 8,
                        "half_dead": false,
                        "move_adjusted_damage": 8,
                        "max_hp": 28,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 28,
                        "current_hp": 12,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 46,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Shrug It Off",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    }
                ]
            },
            "3": {
                "player": {
                    "current_hp": 36,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 1
                },
                "monsters": [
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": 8,
                        "half_dead": false,
                        "move_adjusted_damage": 8,
                        "max_hp": 28,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 28,
                        "current_hp": 12,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 46,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Shrug It Off",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    }
                ]
            },
            "4": {
                "player": {
                    "current_hp": 36,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 0
                },
                "monsters": [
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": 8,
                        "half_dead": false,
                        "move_adjusted_damage": 8,
                        "max_hp": 28,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 28,
                        "current_hp": 12,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 46,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Shrug It Off",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    }
                ]
            }
        },
        "9": {
            "1": {
                "player": {
                    "current_hp": 36,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": 8,
                        "half_dead": false,
                        "move_adjusted_damage": 8,
                        "max_hp": 28,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 28,
                        "current_hp": 12,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 46,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": -1,
                        "name": "Whirlwind+",
                        "type": "ATTACK",
                        "upgrades": 1
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Bash",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    }
                ]
            },
            "2": {
                "player": {
                    "current_hp": 36,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 0
                },
                "monsters": [
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": 8,
                        "half_dead": false,
                        "move_adjusted_damage": 8,
                        "max_hp": 28,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 28,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 28,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 2,
                        "name": "Bash",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    }
                ]
            }
        },
        "10": {
            "1": {
                "player": {
                    "current_hp": 36,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": 8,
                        "half_dead": false,
                        "move_adjusted_damage": 8,
                        "max_hp": 28,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 28,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 10,
                        "half_dead": false,
                        "move_adjusted_damage": 10,
                        "max_hp": 28,
                        "current_hp": 28,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 10,
                        "half_dead": false,
                        "move_adjusted_damage": 10,
                        "max_hp": 28,
                        "current_hp": 28,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Perfected Strike+",
                        "type": "ATTACK",
                        "upgrades": 1
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            },
            "2": {
                "player": {
                    "current_hp": 36,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 1
                },
                "monsters": [
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": 8,
                        "half_dead": false,
                        "move_adjusted_damage": 8,
                        "max_hp": 28,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 28,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 10,
                        "half_dead": false,
                        "move_adjusted_damage": 10,
                        "max_hp": 28,
                        "current_hp": 10,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 10,
                        "half_dead": false,
                        "move_adjusted_damage": 10,
                        "max_hp": 28,
                        "current_hp": 28,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            },
            "3": {
                "player": {
                    "current_hp": 36,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 0
                },
                "monsters": [
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": 8,
                        "half_dead": false,
                        "move_adjusted_damage": 8,
                        "max_hp": 28,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 28,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 10,
                        "half_dead": false,
                        "move_adjusted_damage": 10,
                        "max_hp": 28,
                        "current_hp": 6,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 10,
                        "half_dead": false,
                        "move_adjusted_damage": 10,
                        "max_hp": 28,
                        "current_hp": 28,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            }
        },
        "11": {
            "1": {
                "player": {
                    "current_hp": 22,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": 8,
                        "half_dead": false,
                        "move_adjusted_damage": 8,
                        "max_hp": 28,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 28,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 7,
                        "half_dead": false,
                        "move_adjusted_damage": 7,
                        "max_hp": 28,
                        "current_hp": 6,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 28,
                        "current_hp": 28,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Bash",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            },
            "2": {
                "player": {
                    "current_hp": 22,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 1
                },
                "monsters": [
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": 8,
                        "half_dead": false,
                        "move_adjusted_damage": 8,
                        "max_hp": 28,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 28,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": 7,
                        "half_dead": false,
                        "move_adjusted_damage": 7,
                        "max_hp": 28,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 28,
                        "current_hp": 28,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            },
            "3": {
                "player": {
                    "current_hp": 22,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 0
                },
                "monsters": [
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": 8,
                        "half_dead": false,
                        "move_adjusted_damage": 8,
                        "max_hp": 28,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 28,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": 7,
                        "half_dead": false,
                        "move_adjusted_damage": 7,
                        "max_hp": 28,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 28,
                        "current_hp": 24,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": true,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            }
        },
        "12": {
            "1": {
                "player": {
                    "current_hp": 22,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": 8,
                        "half_dead": false,
                        "move_adjusted_damage": 8,
                        "max_hp": 28,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 28,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": 7,
                        "half_dead": false,
                        "move_adjusted_damage": 7,
                        "max_hp": 28,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 28,
                        "current_hp": 24,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": -1,
                        "name": "Whirlwind+",
                        "type": "ATTACK",
                        "upgrades": 1
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Perfected Strike+",
                        "type": "ATTACK",
                        "upgrades": 1
                    }
                ]
            },
            "2": {
                "player": {
                    "current_hp": 22,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 1
                },
                "monsters": [
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": 8,
                        "half_dead": false,
                        "move_adjusted_damage": 8,
                        "max_hp": 28,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 28,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": 7,
                        "half_dead": false,
                        "move_adjusted_damage": 7,
                        "max_hp": 28,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 140,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": true,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 58,
                        "current_hp": 0,
                        "block": 0
                    },
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 28,
                        "current_hp": 6,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": -1,
                        "name": "Whirlwind+",
                        "type": "ATTACK",
                        "upgrades": 1
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Slimed",
                        "type": "STATUS",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    }
                ]
            }
        }
    },
    "end_info": {
        "current_hp": 28,
        "gold": 137,
        "max_hp": 80
    },
    "win": true
}
    t4 = {
    "start_info": {
        "act": 1,
        "current_hp": 80,
        "floor": 1,
        "gold": 99,
        "max_hp": 80
    },
    "turns": {
        "1": {
            "1": {
                "player": {
                    "current_hp": 80,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 11,
                        "half_dead": false,
                        "move_adjusted_damage": 11,
                        "max_hp": 41,
                        "current_hp": 41,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Reaper",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ],
                "action": "Defend"
            },
            "2": {
                "player": {
                    "current_hp": 80,
                    "block": 5,
                    "max_hp": 80,
                    "energy": 2
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 11,
                        "half_dead": false,
                        "move_adjusted_damage": 11,
                        "max_hp": 41,
                        "current_hp": 41,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": true,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Reaper",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ],
                "action": "Reaper"
            },
            "3": {
                "player": {
                    "current_hp": 80,
                    "block": 5,
                    "max_hp": 80,
                    "energy": 0
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 11,
                        "half_dead": false,
                        "move_adjusted_damage": 11,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            }
        },
        "2": {
            "1": {
                "player": {
                    "current_hp": 74,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Bash",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    }
                ],
                "action": "Defend"
            },
            "2": {
                "player": {
                    "current_hp": 74,
                    "block": 5,
                    "max_hp": 80,
                    "energy": 2
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Bash",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    }
                ],
                "action": "Defend"
            },
            "3": {
                "player": {
                    "current_hp": 74,
                    "block": 10,
                    "max_hp": 80,
                    "energy": 1
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 2,
                        "name": "Bash",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ],
                "action": "End Turn"
            }
        },
        "3": {
            "1": {
                "player": {
                    "current_hp": 74,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 7,
                        "half_dead": false,
                        "move_adjusted_damage": 10,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 6
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Bash",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ],
                "action": "Defend"
            },
            "2": {
                "player": {
                    "current_hp": 74,
                    "block": 5,
                    "max_hp": 80,
                    "energy": 2
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 7,
                        "half_dead": false,
                        "move_adjusted_damage": 10,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 6
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Bash",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ],
                "action": "Defend"
            },
            "3": {
                "player": {
                    "current_hp": 74,
                    "block": 10,
                    "max_hp": 80,
                    "energy": 1
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 7,
                        "half_dead": false,
                        "move_adjusted_damage": 10,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 6
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 2,
                        "name": "Bash",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ],
                "action": "End Turn"
            }
        },
        "4": {
            "1": {
                "player": {
                    "current_hp": 74,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 7,
                        "half_dead": false,
                        "move_adjusted_damage": 10,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 5
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    }
                ],
                "action": "Defend"
            },
            "2": {
                "player": {
                    "current_hp": 74,
                    "block": 5,
                    "max_hp": 80,
                    "energy": 2
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 7,
                        "half_dead": false,
                        "move_adjusted_damage": 10,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 5
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    }
                ],
                "action": "Defend"
            },
            "3": {
                "player": {
                    "current_hp": 74,
                    "block": 10,
                    "max_hp": 80,
                    "energy": 1
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 7,
                        "half_dead": false,
                        "move_adjusted_damage": 10,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 5
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ],
                "action": "End Turn"
            }
        },
        "5": {
            "1": {
                "player": {
                    "current_hp": 74,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 5
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    }
                ],
                "action": "Defend"
            },
            "2": {
                "player": {
                    "current_hp": 74,
                    "block": 5,
                    "max_hp": 80,
                    "energy": 2
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 5
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    }
                ],
                "action": "Defend"
            },
            "3": {
                "player": {
                    "current_hp": 74,
                    "block": 10,
                    "max_hp": 80,
                    "energy": 1
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 5
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    }
                ],
                "action": "Defend"
            },
            "4": {
                "player": {
                    "current_hp": 74,
                    "block": 15,
                    "max_hp": 80,
                    "energy": 0
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 5
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            }
        },
        "6": {
            "1": {
                "player": {
                    "current_hp": 74,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 7,
                        "half_dead": false,
                        "move_adjusted_damage": 13,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 6
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Bash",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ],
                "action": "Defend"
            },
            "2": {
                "player": {
                    "current_hp": 74,
                    "block": 5,
                    "max_hp": 80,
                    "energy": 2
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 7,
                        "half_dead": false,
                        "move_adjusted_damage": 13,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 6
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Bash",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ],
                "action": "End Turn"
            }
        },
        "7": {
            "1": {
                "player": {
                    "current_hp": 66,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 7,
                        "half_dead": false,
                        "move_adjusted_damage": 13,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 5
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Bash",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    }
                ],
                "action": "Defend"
            },
            "2": {
                "player": {
                    "current_hp": 66,
                    "block": 5,
                    "max_hp": 80,
                    "energy": 2
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 7,
                        "half_dead": false,
                        "move_adjusted_damage": 13,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 5
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Bash",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    }
                ],
                "action": "Defend"
            },
            "3": {
                "player": {
                    "current_hp": 66,
                    "block": 10,
                    "max_hp": 80,
                    "energy": 1
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 7,
                        "half_dead": false,
                        "move_adjusted_damage": 13,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 5
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 2,
                        "name": "Bash",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    }
                ],
                "action": "Defend"
            },
            "4": {
                "player": {
                    "current_hp": 66,
                    "block": 15,
                    "max_hp": 80,
                    "energy": 0
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 7,
                        "half_dead": false,
                        "move_adjusted_damage": 13,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 5
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 2,
                        "name": "Bash",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            }
        },
        "8": {
            "1": {
                "player": {
                    "current_hp": 66,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 5
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ],
                "action": "Defend"
            },
            "2": {
                "player": {
                    "current_hp": 66,
                    "block": 5,
                    "max_hp": 80,
                    "energy": 2
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 5
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ],
                "action": "End Turn"
            }
        },
        "9": {
            "1": {
                "player": {
                    "current_hp": 66,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 11,
                        "half_dead": false,
                        "move_adjusted_damage": 20,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 6
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ],
                "action": "Defend"
            },
            "2": {
                "player": {
                    "current_hp": 66,
                    "block": 5,
                    "max_hp": 80,
                    "energy": 2
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 11,
                        "half_dead": false,
                        "move_adjusted_damage": 20,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 6
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ],
                "action": "End Turn"
            }
        },
        "10": {
            "1": {
                "player": {
                    "current_hp": 51,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 7,
                        "half_dead": false,
                        "move_adjusted_damage": 16,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Bash",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    }
                ],
                "action": "Defend"
            },
            "2": {
                "player": {
                    "current_hp": 51,
                    "block": 5,
                    "max_hp": 80,
                    "energy": 2
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 7,
                        "half_dead": false,
                        "move_adjusted_damage": 16,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Bash",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    }
                ],
                "action": "Defend"
            },
            "3": {
                "player": {
                    "current_hp": 51,
                    "block": 10,
                    "max_hp": 80,
                    "energy": 1
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 7,
                        "half_dead": false,
                        "move_adjusted_damage": 16,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 2,
                        "name": "Bash",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    }
                ],
                "action": "Defend"
            },
            "4": {
                "player": {
                    "current_hp": 51,
                    "block": 15,
                    "max_hp": 80,
                    "energy": 0
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 7,
                        "half_dead": false,
                        "move_adjusted_damage": 16,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 2,
                        "name": "Bash",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            }
        },
        "11": {
            "1": {
                "player": {
                    "current_hp": 50,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 5
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Bash",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ],
                "action": "Defend"
            },
            "2": {
                "player": {
                    "current_hp": 50,
                    "block": 5,
                    "max_hp": 80,
                    "energy": 2
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 5
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Bash",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ],
                "action": "Defend"
            },
            "3": {
                "player": {
                    "current_hp": 50,
                    "block": 10,
                    "max_hp": 80,
                    "energy": 1
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 5
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 2,
                        "name": "Bash",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ],
                "action": "End Turn"
            }
        },
        "12": {
            "1": {
                "player": {
                    "current_hp": 50,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 11,
                        "half_dead": false,
                        "move_adjusted_damage": 23,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 6
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    }
                ],
                "action": "Defend"
            },
            "2": {
                "player": {
                    "current_hp": 50,
                    "block": 5,
                    "max_hp": 80,
                    "energy": 2
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 11,
                        "half_dead": false,
                        "move_adjusted_damage": 23,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 6
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    }
                ],
                "action": "Defend"
            },
            "3": {
                "player": {
                    "current_hp": 50,
                    "block": 10,
                    "max_hp": 80,
                    "energy": 1
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 11,
                        "half_dead": false,
                        "move_adjusted_damage": 23,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 6
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ],
                "action": "End Turn"
            }
        },
        "13": {
            "1": {
                "player": {
                    "current_hp": 37,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Bash",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ],
                "action": "Defend"
            },
            "2": {
                "player": {
                    "current_hp": 37,
                    "block": 5,
                    "max_hp": 80,
                    "energy": 2
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Bash",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ],
                "action": "Defend"
            },
            "3": {
                "player": {
                    "current_hp": 37,
                    "block": 10,
                    "max_hp": 80,
                    "energy": 1
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 2,
                        "name": "Bash",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ],
                "action": "End Turn"
            }
        },
        "14": {
            "1": {
                "player": {
                    "current_hp": 37,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 7,
                        "half_dead": false,
                        "move_adjusted_damage": 22,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 6
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    }
                ],
                "action": "Defend"
            },
            "2": {
                "player": {
                    "current_hp": 37,
                    "block": 5,
                    "max_hp": 80,
                    "energy": 2
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 7,
                        "half_dead": false,
                        "move_adjusted_damage": 22,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 6
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    }
                ],
                "action": "Defend"
            },
            "3": {
                "player": {
                    "current_hp": 37,
                    "block": 10,
                    "max_hp": 80,
                    "energy": 1
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 7,
                        "half_dead": false,
                        "move_adjusted_damage": 22,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 6
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ],
                "action": "End Turn"
            }
        },
        "15": {
            "1": {
                "player": {
                    "current_hp": 25,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 11,
                        "half_dead": false,
                        "move_adjusted_damage": 26,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 5
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ],
                "action": "Defend"
            },
            "2": {
                "player": {
                    "current_hp": 25,
                    "block": 5,
                    "max_hp": 80,
                    "energy": 2
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 11,
                        "half_dead": false,
                        "move_adjusted_damage": 26,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 5
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ],
                "action": "End Turn"
            }
        },
        "16": {
            "1": {
                "player": {
                    "current_hp": 4,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Bash",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ],
                "action": "Defend"
            },
            "2": {
                "player": {
                    "current_hp": 4,
                    "block": 5,
                    "max_hp": 80,
                    "energy": 2
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Bash",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ],
                "action": "Defend"
            },
            "3": {
                "player": {
                    "current_hp": 4,
                    "block": 10,
                    "max_hp": 80,
                    "energy": 1
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 2,
                        "name": "Bash",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ],
                "action": "Defend"
            },
            "4": {
                "player": {
                    "current_hp": 4,
                    "block": 15,
                    "max_hp": 80,
                    "energy": 0
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 2,
                        "name": "Bash",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": false,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ]
            }
        },
        "17": {
            "1": {
                "player": {
                    "current_hp": 4,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 7,
                        "half_dead": false,
                        "move_adjusted_damage": 25,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 6
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    }
                ],
                "action": "Defend"
            },
            "2": {
                "player": {
                    "current_hp": 4,
                    "block": 5,
                    "max_hp": 80,
                    "energy": 2
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 7,
                        "half_dead": false,
                        "move_adjusted_damage": 25,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 6
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    }
                ],
                "action": "Defend"
            },
            "3": {
                "player": {
                    "current_hp": 4,
                    "block": 10,
                    "max_hp": 80,
                    "energy": 1
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 7,
                        "half_dead": false,
                        "move_adjusted_damage": 25,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 6
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ],
                "action": "End Turn"
            },
            "4": {
                "player": {
                    "current_hp": 0,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 1
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 7,
                        "half_dead": false,
                        "move_adjusted_damage": 25,
                        "max_hp": 41,
                        "current_hp": 37,
                        "block": 0
                    }
                ],
                "hand": []
            }
        }
    },
    "end_info": {
        "current_hp": 0,
        "gold": 99,
        "max_hp": 80
    },
    "win": false
}
    t5 = {
    "start_info": {
        "act": 1,
        "current_hp": 80,
        "floor": 1,
        "gold": 99,
        "max_hp": 80
    },
    "turns": {
        1: {
            1: {
                "player": {
                    "current_hp": 80,
                    "block": 0,
                    "max_hp": 80,
                    "energy": 3
                },
                "monsters": [
                    {
                        "is_gone": false,
                        "move_hits": 1,
                        "move_base_damage": 11,
                        "half_dead": false,
                        "move_adjusted_damage": 11,
                        "max_hp": 44,
                        "current_hp": 1,
                        "block": 0
                    }
                ],
                "hand": [
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 2,
                        "name": "Bash",
                        "type": "ATTACK",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Defend",
                        "type": "SKILL",
                        "upgrades": 0
                    },
                    {
                        "exhausts": false,
                        "is_playable": true,
                        "cost": 1,
                        "name": "Strike",
                        "type": "ATTACK",
                        "upgrades": 0
                    }
                ],
                "action": "Strike"
            }
        }
    },
    "end_info": {
        "current_hp": 80,
        "gold": 99,
        "max_hp": 80
    },
    "win": true
}


    m.get_data(t5)
    # net = Net(n_feature=100,n_hidden=20,n_output=100)
    # print(net)
