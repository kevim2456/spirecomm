# from spirecomm.spire.game import Game
# from spirecomm.spire.character import Intent, PlayerClass
# import spirecomm.spire.card
# from spirecomm.spire.screen import RestOption
# from spirecomm.communication.action import *
import json

def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

def recur_get(obj, iter):
    name = '_'.join(iter)
    def recur(obj, iter):
        obj = obj.get(iter.pop(0), None)
        if len(iter): return recur(obj, iter)
        else: return obj
    obj = recur(obj, iter)
    return {name:obj}

def a_fetch(game):
    str = "C:\\Users\\kevinliu.cs08\\Documents\\GitHub\\spirecomm\\test.json"
    f = open(str,'w')
    f.write("in a.py\n")
    f.write(json.dumps(game.json_state, indent=4))
    f.write("\n\n")
    f.write(json.dumps(flatten_json(game.json_state), indent=4))
    f.write("\n\n")
    f.close()

# if dead
# game_state":{"screen_type":"GAME_OVER
# else
# game_state : screen_type : reward

if __name__ == '__main__':
    from pprintpp import pprint as pp
    false = False
    true = True
    t = {
    "act": 1,
    "act_boss": "The Guardian",
    "action_phase": "WAITING_ON_USER",
    "ascension_level": 0,
    "class": "IRONCLAD",
    "combat_state": {
        "cards_discarded_this_turn": 0,
        "discard_pile": [],
        "draw_pile": [
            {
                "cost": 1,
                "exhausts": false,
                "has_target": false,
                "id": "Defend_R",
                "is_playable": true,
                "name": "Defend",
                "rarity": "BASIC",
                "type": "SKILL",
                "upgrades": 0,
                "uuid": "489816c6-644d-47c1-89d1-8e2600ad50b2"
            },
            {
                "cost": 1,
                "exhausts": false,
                "has_target": true,
                "id": "Strike_R",
                "is_playable": true,
                "name": "Strike",
                "rarity": "BASIC",
                "type": "ATTACK",
                "upgrades": 0,
                "uuid": "df098b32-13f7-485f-b8c6-c5b6f89d7c5e"
            },
            {
                "cost": 1,
                "exhausts": false,
                "has_target": false,
                "id": "Defend_R",
                "is_playable": true,
                "name": "Defend",
                "rarity": "BASIC",
                "type": "SKILL",
                "upgrades": 0,
                "uuid": "99402c8a-7b5c-4737-8311-fe8898a5fb1d"
            },
            {
                "cost": 2,
                "exhausts": false,
                "has_target": true,
                "id": "Bash",
                "is_playable": true,
                "name": "Bash",
                "rarity": "BASIC",
                "type": "ATTACK",
                "upgrades": 0,
                "uuid": "0d765bc6-9010-43be-b893-dbca52a0e2ee"
            },
            {
                "cost": 1,
                "exhausts": false,
                "has_target": true,
                "id": "Strike_R",
                "is_playable": true,
                "name": "Strike",
                "rarity": "BASIC",
                "type": "ATTACK",
                "upgrades": 0,
                "uuid": "09a40d52-094a-4296-bfff-88fa67169665"
            }
        ],
        "exhaust_pile": [],
        "hand": [
            {
                "cost": 1,
                "exhausts": false,
                "has_target": false,
                "id": "Defend_R",
                "is_playable": true,
                "name": "Defend",
                "rarity": "BASIC",
                "type": "SKILL",
                "upgrades": 0,
                "uuid": "d2ec4bd1-95a5-4982-a538-935a114ddbc5"
            },
            {
                "cost": 1,
                "exhausts": false,
                "has_target": true,
                "id": "Strike_R",
                "is_playable": true,
                "name": "Strike",
                "rarity": "BASIC",
                "type": "ATTACK",
                "upgrades": 0,
                "uuid": "e33184b2-d089-4000-a773-2c3599e932dc"
            },
            {
                "cost": 1,
                "exhausts": false,
                "has_target": false,
                "id": "Defend_R",
                "is_playable": true,
                "name": "Defend",
                "rarity": "BASIC",
                "type": "SKILL",
                "upgrades": 0,
                "uuid": "f35e8745-e361-49e9-b0e9-8bb325f0a899"
            },
            {
                "cost": 1,
                "exhausts": false,
                "has_target": true,
                "id": "Strike_R",
                "is_playable": true,
                "name": "Strike",
                "rarity": "BASIC",
                "type": "ATTACK",
                "upgrades": 0,
                "uuid": "a60ad85b-c937-432e-b07e-d9f8264960b6"
            },
            {
                "cost": 1,
                "exhausts": false,
                "has_target": true,
                "id": "Strike_R",
                "is_playable": true,
                "name": "Strike",
                "rarity": "BASIC",
                "type": "ATTACK",
                "upgrades": 0,
                "uuid": "ea787ed9-ab11-405a-b753-be81d1efea5e"
            }
        ],
        "limbo": [],
        "monsters": [
            {
                "block": 0,
                "current_hp": 40,
                "half_dead": false,
                "id": "JawWorm",
                "intent": "ATTACK",
                "is_gone": false,
                "max_hp": 40,
                "move_adjusted_damage": 11,
                "move_base_damage": 11,
                "move_hits": 1,
                "move_id": 1,
                "name": "Jaw Worm",
                "powers": []
            }
        ],
        "player": {
            "block": 0,
            "current_hp": 88,
            "energy": 3,
            "max_hp": 88,
            "orbs": [],
            "powers": []
        },
        "turn": 1
    },
    "current_hp": 88,
    "deck": [
        {
            "cost": 1,
            "exhausts": false,
            "has_target": true,
            "id": "Strike_R",
            "is_playable": true,
            "name": "Strike",
            "rarity": "BASIC",
            "type": "ATTACK",
            "upgrades": 0,
            "uuid": "ea787ed9-ab11-405a-b753-be81d1efea5e"
        },
        {
            "cost": 1,
            "exhausts": false,
            "has_target": true,
            "id": "Strike_R",
            "is_playable": true,
            "name": "Strike",
            "rarity": "BASIC",
            "type": "ATTACK",
            "upgrades": 0,
            "uuid": "a60ad85b-c937-432e-b07e-d9f8264960b6"
        },
        {
            "cost": 1,
            "exhausts": false,
            "has_target": true,
            "id": "Strike_R",
            "is_playable": true,
            "name": "Strike",
            "rarity": "BASIC",
            "type": "ATTACK",
            "upgrades": 0,
            "uuid": "df098b32-13f7-485f-b8c6-c5b6f89d7c5e"
        },
        {
            "cost": 1,
            "exhausts": false,
            "has_target": true,
            "id": "Strike_R",
            "is_playable": true,
            "name": "Strike",
            "rarity": "BASIC",
            "type": "ATTACK",
            "upgrades": 0,
            "uuid": "09a40d52-094a-4296-bfff-88fa67169665"
        },
        {
            "cost": 1,
            "exhausts": false,
            "has_target": true,
            "id": "Strike_R",
            "is_playable": true,
            "name": "Strike",
            "rarity": "BASIC",
            "type": "ATTACK",
            "upgrades": 0,
            "uuid": "e33184b2-d089-4000-a773-2c3599e932dc"
        },
        {
            "cost": 1,
            "exhausts": false,
            "has_target": false,
            "id": "Defend_R",
            "is_playable": true,
            "name": "Defend",
            "rarity": "BASIC",
            "type": "SKILL",
            "upgrades": 0,
            "uuid": "d2ec4bd1-95a5-4982-a538-935a114ddbc5"
        },
        {
            "cost": 1,
            "exhausts": false,
            "has_target": false,
            "id": "Defend_R",
            "is_playable": true,
            "name": "Defend",
            "rarity": "BASIC",
            "type": "SKILL",
            "upgrades": 0,
            "uuid": "489816c6-644d-47c1-89d1-8e2600ad50b2"
        },
        {
            "cost": 1,
            "exhausts": false,
            "has_target": false,
            "id": "Defend_R",
            "is_playable": true,
            "name": "Defend",
            "rarity": "BASIC",
            "type": "SKILL",
            "upgrades": 0,
            "uuid": "f35e8745-e361-49e9-b0e9-8bb325f0a899"
        },
        {
            "cost": 1,
            "exhausts": false,
            "has_target": false,
            "id": "Defend_R",
            "is_playable": true,
            "name": "Defend",
            "rarity": "BASIC",
            "type": "SKILL",
            "upgrades": 0,
            "uuid": "99402c8a-7b5c-4737-8311-fe8898a5fb1d"
        },
        {
            "cost": 2,
            "exhausts": false,
            "has_target": true,
            "id": "Bash",
            "is_playable": true,
            "name": "Bash",
            "rarity": "BASIC",
            "type": "ATTACK",
            "upgrades": 0,
            "uuid": "0d765bc6-9010-43be-b893-dbca52a0e2ee"
        }
    ],
    "floor": 1,
    "gold": 99,
    "is_screen_up": false,
    "map": [
        {
            "children": [
                {
                    "x": 0,
                    "y": 1
                }
            ],
            "parents": [],
            "symbol": "M",
            "x": 0,
            "y": 0
        },
        {
            "children": [
                {
                    "x": 1,
                    "y": 1
                },
                {
                    "x": 2,
                    "y": 1
                }
            ],
            "parents": [],
            "symbol": "M",
            "x": 1,
            "y": 0
        },
        {
            "children": [
                {
                    "x": 4,
                    "y": 1
                }
            ],
            "parents": [],
            "symbol": "M",
            "x": 3,
            "y": 0
        },
        {
            "children": [
                {
                    "x": 5,
                    "y": 1
                }
            ],
            "parents": [],
            "symbol": "M",
            "x": 5,
            "y": 0
        },
        {
            "children": [
                {
                    "x": 1,
                    "y": 2
                }
            ],
            "parents": [],
            "symbol": "?",
            "x": 0,
            "y": 1
        },
        {
            "children": [
                {
                    "x": 2,
                    "y": 2
                }
            ],
            "parents": [],
            "symbol": "?",
            "x": 1,
            "y": 1
        },
        {
            "children": [
                {
                    "x": 3,
                    "y": 2
                }
            ],
            "parents": [],
            "symbol": "M",
            "x": 2,
            "y": 1
        },
        {
            "children": [
                {
                    "x": 5,
                    "y": 2
                }
            ],
            "parents": [],
            "symbol": "?",
            "x": 4,
            "y": 1
        },
        {
            "children": [
                {
                    "x": 5,
                    "y": 2
                }
            ],
            "parents": [],
            "symbol": "?",
            "x": 5,
            "y": 1
        },
        {
            "children": [
                {
                    "x": 1,
                    "y": 3
                }
            ],
            "parents": [],
            "symbol": "?",
            "x": 1,
            "y": 2
        },
        {
            "children": [
                {
                    "x": 2,
                    "y": 3
                }
            ],
            "parents": [],
            "symbol": "M",
            "x": 2,
            "y": 2
        },
        {
            "children": [
                {
                    "x": 4,
                    "y": 3
                }
            ],
            "parents": [],
            "symbol": "$",
            "x": 3,
            "y": 2
        },
        {
            "children": [
                {
                    "x": 4,
                    "y": 3
                },
                {
                    "x": 5,
                    "y": 3
                },
                {
                    "x": 6,
                    "y": 3
                }
            ],
            "parents": [],
            "symbol": "M",
            "x": 5,
            "y": 2
        },
        {
            "children": [
                {
                    "x": 0,
                    "y": 4
                }
            ],
            "parents": [],
            "symbol": "M",
            "x": 1,
            "y": 3
        },
        {
            "children": [
                {
                    "x": 3,
                    "y": 4
                }
            ],
            "parents": [],
            "symbol": "?",
            "x": 2,
            "y": 3
        },
        {
            "children": [
                {
                    "x": 3,
                    "y": 4
                },
                {
                    "x": 4,
                    "y": 4
                }
            ],
            "parents": [],
            "symbol": "M",
            "x": 4,
            "y": 3
        },
        {
            "children": [
                {
                    "x": 5,
                    "y": 4
                }
            ],
            "parents": [],
            "symbol": "?",
            "x": 5,
            "y": 3
        },
        {
            "children": [
                {
                    "x": 6,
                    "y": 4
                }
            ],
            "parents": [],
            "symbol": "$",
            "x": 6,
            "y": 3
        },
        {
            "children": [
                {
                    "x": 0,
                    "y": 5
                }
            ],
            "parents": [],
            "symbol": "M",
            "x": 0,
            "y": 4
        },
        {
            "children": [
                {
                    "x": 2,
                    "y": 5
                },
                {
                    "x": 3,
                    "y": 5
                }
            ],
            "parents": [],
            "symbol": "M",
            "x": 3,
            "y": 4
        },
        {
            "children": [
                {
                    "x": 4,
                    "y": 5
                }
            ],
            "parents": [],
            "symbol": "?",
            "x": 4,
            "y": 4
        },
        {
            "children": [
                {
                    "x": 5,
                    "y": 5
                }
            ],
            "parents": [],
            "symbol": "M",
            "x": 5,
            "y": 4
        },
        {
            "children": [
                {
                    "x": 5,
                    "y": 5
                }
            ],
            "parents": [],
            "symbol": "M",
            "x": 6,
            "y": 4
        },
        {
            "children": [
                {
                    "x": 0,
                    "y": 6
                }
            ],
            "parents": [],
            "symbol": "R",
            "x": 0,
            "y": 5
        },
        {
            "children": [
                {
                    "x": 1,
                    "y": 6
                }
            ],
            "parents": [],
            "symbol": "R",
            "x": 2,
            "y": 5
        },
        {
            "children": [
                {
                    "x": 3,
                    "y": 6
                }
            ],
            "parents": [],
            "symbol": "E",
            "x": 3,
            "y": 5
        },
        {
            "children": [
                {
                    "x": 4,
                    "y": 6
                }
            ],
            "parents": [],
            "symbol": "R",
            "x": 4,
            "y": 5
        },
        {
            "children": [
                {
                    "x": 4,
                    "y": 6
                }
            ],
            "parents": [],
            "symbol": "E",
            "x": 5,
            "y": 5
        },
        {
            "children": [
                {
                    "x": 0,
                    "y": 7
                }
            ],
            "parents": [],
            "symbol": "M",
            "x": 0,
            "y": 6
        },
        {
            "children": [
                {
                    "x": 0,
                    "y": 7
                }
            ],
            "parents": [],
            "symbol": "M",
            "x": 1,
            "y": 6
        },
        {
            "children": [
                {
                    "x": 3,
                    "y": 7
                }
            ],
            "parents": [],
            "symbol": "M",
            "x": 3,
            "y": 6
        },
        {
            "children": [
                {
                    "x": 5,
                    "y": 7
                }
            ],
            "parents": [],
            "symbol": "M",
            "x": 4,
            "y": 6
        },
        {
            "children": [
                {
                    "x": 0,
                    "y": 8
                },
                {
                    "x": 1,
                    "y": 8
                }
            ],
            "parents": [],
            "symbol": "?",
            "x": 0,
            "y": 7
        },
        {
            "children": [
                {
                    "x": 4,
                    "y": 8
                }
            ],
            "parents": [],
            "symbol": "E",
            "x": 3,
            "y": 7
        },
        {
            "children": [
                {
                    "x": 5,
                    "y": 8
                }
            ],
            "parents": [],
            "symbol": "M",
            "x": 5,
            "y": 7
        },
        {
            "children": [
                {
                    "x": 0,
                    "y": 9
                }
            ],
            "parents": [],
            "symbol": "T",
            "x": 0,
            "y": 8
        },
        {
            "children": [
                {
                    "x": 1,
                    "y": 9
                }
            ],
            "parents": [],
            "symbol": "T",
            "x": 1,
            "y": 8
        },
        {
            "children": [
                {
                    "x": 3,
                    "y": 9
                }
            ],
            "parents": [],
            "symbol": "T",
            "x": 4,
            "y": 8
        },
        {
            "children": [
                {
                    "x": 6,
                    "y": 9
                }
            ],
            "parents": [],
            "symbol": "T",
            "x": 5,
            "y": 8
        },
        {
            "children": [
                {
                    "x": 0,
                    "y": 10
                }
            ],
            "parents": [],
            "symbol": "?",
            "x": 0,
            "y": 9
        },
        {
            "children": [
                {
                    "x": 1,
                    "y": 10
                }
            ],
            "parents": [],
            "symbol": "?",
            "x": 1,
            "y": 9
        },
        {
            "children": [
                {
                    "x": 2,
                    "y": 10
                }
            ],
            "parents": [],
            "symbol": "E",
            "x": 3,
            "y": 9
        },
        {
            "children": [
                {
                    "x": 6,
                    "y": 10
                }
            ],
            "parents": [],
            "symbol": "R",
            "x": 6,
            "y": 9
        },
        {
            "children": [
                {
                    "x": 0,
                    "y": 11
                }
            ],
            "parents": [],
            "symbol": "M",
            "x": 0,
            "y": 10
        },
        {
            "children": [
                {
                    "x": 2,
                    "y": 11
                }
            ],
            "parents": [],
            "symbol": "?",
            "x": 1,
            "y": 10
        },
        {
            "children": [
                {
                    "x": 3,
                    "y": 11
                }
            ],
            "parents": [],
            "symbol": "?",
            "x": 2,
            "y": 10
        },
        {
            "children": [
                {
                    "x": 5,
                    "y": 11
                },
                {
                    "x": 6,
                    "y": 11
                }
            ],
            "parents": [],
            "symbol": "M",
            "x": 6,
            "y": 10
        },
        {
            "children": [
                {
                    "x": 1,
                    "y": 12
                }
            ],
            "parents": [],
            "symbol": "R",
            "x": 0,
            "y": 11
        },
        {
            "children": [
                {
                    "x": 2,
                    "y": 12
                }
            ],
            "parents": [],
            "symbol": "M",
            "x": 2,
            "y": 11
        },
        {
            "children": [
                {
                    "x": 3,
                    "y": 12
                }
            ],
            "parents": [],
            "symbol": "E",
            "x": 3,
            "y": 11
        },
        {
            "children": [
                {
                    "x": 5,
                    "y": 12
                }
            ],
            "parents": [],
            "symbol": "R",
            "x": 5,
            "y": 11
        },
        {
            "children": [
                {
                    "x": 6,
                    "y": 12
                }
            ],
            "parents": [],
            "symbol": "M",
            "x": 6,
            "y": 11
        },
        {
            "children": [
                {
                    "x": 2,
                    "y": 13
                }
            ],
            "parents": [],
            "symbol": "M",
            "x": 1,
            "y": 12
        },
        {
            "children": [
                {
                    "x": 2,
                    "y": 13
                }
            ],
            "parents": [],
            "symbol": "M",
            "x": 2,
            "y": 12
        },
        {
            "children": [
                {
                    "x": 4,
                    "y": 13
                }
            ],
            "parents": [],
            "symbol": "$",
            "x": 3,
            "y": 12
        },
        {
            "children": [
                {
                    "x": 6,
                    "y": 13
                }
            ],
            "parents": [],
            "symbol": "M",
            "x": 5,
            "y": 12
        },
        {
            "children": [
                {
                    "x": 6,
                    "y": 13
                }
            ],
            "parents": [],
            "symbol": "M",
            "x": 6,
            "y": 12
        },
        {
            "children": [
                {
                    "x": 1,
                    "y": 14
                },
                {
                    "x": 2,
                    "y": 14
                }
            ],
            "parents": [],
            "symbol": "M",
            "x": 2,
            "y": 13
        },
        {
            "children": [
                {
                    "x": 3,
                    "y": 14
                }
            ],
            "parents": [],
            "symbol": "M",
            "x": 4,
            "y": 13
        },
        {
            "children": [
                {
                    "x": 5,
                    "y": 14
                }
            ],
            "parents": [],
            "symbol": "M",
            "x": 6,
            "y": 13
        },
        {
            "children": [
                {
                    "x": 3,
                    "y": 16
                }
            ],
            "parents": [],
            "symbol": "R",
            "x": 1,
            "y": 14
        },
        {
            "children": [
                {
                    "x": 3,
                    "y": 16
                }
            ],
            "parents": [],
            "symbol": "R",
            "x": 2,
            "y": 14
        },
        {
            "children": [
                {
                    "x": 3,
                    "y": 16
                }
            ],
            "parents": [],
            "symbol": "R",
            "x": 3,
            "y": 14
        },
        {
            "children": [
                {
                    "x": 3,
                    "y": 16
                }
            ],
            "parents": [],
            "symbol": "R",
            "x": 5,
            "y": 14
        }
    ],
    "max_hp": 88,
    "potions": [
        {
            "can_discard": false,
            "can_use": false,
            "id": "Potion Slot",
            "name": "Potion Slot",
            "requires_target": false
        },
        {
            "can_discard": false,
            "can_use": false,
            "id": "Potion Slot",
            "name": "Potion Slot",
            "requires_target": false
        },
        {
            "can_discard": false,
            "can_use": false,
            "id": "Potion Slot",
            "name": "Potion Slot",
            "requires_target": false
        }
    ],
    "relics": [
        {
            "counter": -1,
            "id": "Burning Blood",
            "name": "Burning Blood"
        }
    ],
    "room_phase": "COMBAT",
    "room_type": "MonsterRoom",
    "screen_name": "NONE",
    "screen_state": {},
    "screen_type": "NONE",
    "seed": 6957534091124485133
}

    z = {}
    l = [["combat_state","player"],["combat_state","monsters"]]
    # print(*[recur_get(t,i) for i in l])
    for i in l :
        z.update(recur_get(t,i))
    zs = repr(z)
    print(zs)


    # state2pop = [
    #     'act_boss',
    #     'action_phase',
    #     'ascension_level',
    #     'class',
    #     'gold',
    #     'is_screen_up',
    #     'map',
    #     'potions',
    #     'relics',
    #     'room_phase',
    #     'room_type',
    #     'screen_name',
    #     'screen_state',
    #     'screen_type',
    #     'seed'
    # ]
    # state2get = ["act","combat_state","current_hp","floor"]
    # state_in_combat2get = ["cards_discarded_this_turn",]
    # t2 = [ t.get(i) for i in state2get ] + [ t["combat_state"].get(i) for i in state_in_combat2get]
    # cards_in_combat_state = [
    #     'discard_pile','draw_pile','exhaust_pile'
    # ]
    # cardfeaturn2pop = [
    #     'has_target','rarity','upgrades','uuid'
    # ]
    #
    # for i in range(len(t["combat_state"]["hand"])):
    #     for f in cardfeaturn2pop:
    #         t["combat_state"]["hand"][i].pop(f)
    #
    # cardfeaturn2pop += ['cost','exhausts','id','is_playable']
    # for c in cards_in_combat_state:
    #     for i in range(len(t["combat_state"][c])):
    #         for f in cardfeaturn2pop:
    #             t["combat_state"][c][i].pop(f)
    #
    # cardfeaturn2pop += ["type"]
    # for i in range(len(t["deck"])):
    #     for f in cardfeaturn2pop:
    #         t["deck"][i].pop(f)
    #
    # for i in state2pop: t.pop(i)
    # t2 = flatten_json(t2)
    # pp(t2)
    # # d = t.values()
    # # pp(d)
