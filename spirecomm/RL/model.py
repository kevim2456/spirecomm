import json
import copy
import torch

false = False
true = True

class Model:
    def __init__(self):
        self.dump_filename = None
        self.reward = 0
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
        # self.dump(json.dumps(self.combat_json, indent=4))
        self.dump("hello world")
        # self.dump("==================== reward : " + repr(self.calc_combat_reward()))
        self.calc_combat_reward()
        self.encode_decision()

    def calc_combat_reward(self):
        hp = self.combat_info["end_info"]["current_hp"] - self.combat_info["start_info"]["current_hp"]
        # max_hp = self.combat_info["end_info"]["max_hp"] - self.combat_info["start_info"]["max_hp"]
        # gold   = self.combat_info["end_info"]["gold"] - self.combat_info["start_info"]["gold"]
        # turn_n = len(self.combat_info["turns"])
        # floor  = self.combat_info["start_info"]["floor"]
        # win    = 10 if self.combat_info["win"] else 0
        # reward = (3*hp, max_hp, gold, -turn_n, 100*floor**0.33)
        return hp
        # return win

    def encode_variable_data(self, tmp, name, max_n):
        num = len(tmp[name])
        if num > max_n : return "error"
        rv = []
        for i in range(max_n):
            if i < num:
                rv.append([ True ]+[ i for i in tmp[name][i].values()])
            else:
                rv.append([ False ]+[ 0 for _ in range(len(tmp[name][0]))])
        return torch.tensor(rv)

    # def encode_card_data(self, tmp, name, mex_n):
    #     num = len(tmp[name])
    #     if num > max_n : return "error"
    #     rv = []
    #     for i in range(max_n):
    #         if i < num:
    #             rv.append([ True ]+[ i for i in tmp[name][i].values()])
    #         else:
    #             rv.append([ False ]+[ 0 for _ in range(len(tmp[name][0]))])
    #     return json.dumps(rv)


    def encode_decision(self):
        self.dump('hello world','w')
        max_monster_num = 5
        max_hand_num = 10
        for turn_k in self.combat_info["turns"].keys():
            for situ_k in self.combat_info["turns"][turn_k].keys():
                # pass
                # self.dump(json.dumps(self.combat_info["turns"][turn_k][situ_k],indent=4),end='\n\n')
                self.dump(str(turn_k)+', '+str(situ_k), end=' :\n')
                tmp = self.combat_info["turns"][turn_k][situ_k]
                # self.dump(repr(tmp["player"].values()))
                self.dump("player: " + repr( torch.tensor([i for i in tmp["player"].values()] ) ) )
                self.dump("monsters:\n" + repr( self.encode_variable_data(tmp, "monsters", max_monster_num) ) ,end='\n\n')
                # self.dump("hand: " + self.encode_variable_data(tmp,"hand",max_hand_num))
        self.dump("end a combat")

if __name__ == '__main__':
    m = Model()
    t = {
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
                    "current_hp": 80,
                    "block": 0,
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
                        "current_hp": 5,
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
                ]
            },
            "3": {
                "player": {
                    "current_hp": 80,
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
                    }
                ]
            },
            "4": {
                "player": {
                    "current_hp": 80,
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
        "2": {
            "1": {
                "player": {
                    "current_hp": 80,
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
                    "current_hp": 80,
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
                ]
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
                        "max_hp": 28,
                        "current_hp": 22,
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
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 28,
                        "current_hp": 22,
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
                    "current_hp": 78,
                    "block": 0,
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
                        "move_base_damage": -1,
                        "half_dead": false,
                        "move_adjusted_damage": -1,
                        "max_hp": 28,
                        "current_hp": 13,
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
                        "max_hp": 28,
                        "current_hp": 4,
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
                        "name": "Defend",
                        "type": "SKILL",
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
}
    m.get_data(t)
