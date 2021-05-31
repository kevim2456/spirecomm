import json
import copy

class Model:
    def __init__(self):
        self.dump_filename = None
        self.set_dump()

    def set_dump(self, s = "C:\\Users\\kevinliu.cs08\\Documents\\GitHub\\spirecomm\\model.json"):
        self.dump_filename = s
        self.dump("test test",'w')

    def dump(self,s,method='a'):
        f = open(self.dump_filename,method)
        try: f.write(s)
        except:
            try: f.write(repr(s))
            except: f.write("dump None str object")
        f.write("\n")
        f.close()

    def get_data(self, combat_info):
        self.combat_info = copy.deepcopy(combat_info)
        # self.dump(json.dumps(self.combat_json, indent=4))
        self.dump("reward : " + repr(self.calc_combat_reward()))

    def calc_combat_reward(self):
        hp = self.combat_info["end_info"]["current_hp"] - self.combat_info["start_info"]["current_hp"]
        max_hp = self.combat_info["end_info"]["max_hp"] - self.combat_info["start_info"]["max_hp"]
        gold   = self.combat_info["end_info"]["gold"] - self.combat_info["start_info"]["gold"]
        turn_n = len(self.combat_info["turns"])
        floor  = self.combat_info["start_info"]["floor"]
        # win    = 10 if self.combat_info["win"] else 0
        reward = (3*hp, max_hp, gold, -turn_n, 100*floor**0.33)
        return (floor, reward, sum(reward))
        # return win
