import itertools
import datetime
import sys

from spirecomm.communication.coordinator import Coordinator
from spirecomm.ai.agent import SimpleAgent
from spirecomm.spire.character import PlayerClass
from spirecomm.RL.model import Model

def dump(s, end='\n', method='a'):
    dump_filename = "C:\\Users\\kevinliu.cs08\\Documents\\GitHub\\spirecomm\\record.txt"
    f = open(dump_filename, method)
    try: f.write(s)
    except:
        try: f.write(repr(s))
        except: f.write("dump None str object")
    f.write(end)
    f.close()

if __name__ == "__main__":
    agent = SimpleAgent()
    agent.set_dump() # you can place your path/file to dump
    brain = Model()
    agent.register_push_data_callback(brain.get_data)
    agent.register_get_action_callback(brain.give_action)

    coordinator = Coordinator()
    coordinator.set_dump() # you can place your path/file to dump
    coordinator.signal_ready()
    coordinator.register_command_error_callback(agent.handle_error)
    coordinator.register_state_change_callback(agent.get_next_action_in_game)
    coordinator.register_out_of_game_callback(agent.get_next_action_out_of_game)

    # Play games forever with ironclad
    agent.change_class(PlayerClass.IRONCLAD)
    dump('test test',method='w')
    while(True):
        result = coordinator.play_one_game(PlayerClass.IRONCLAD)
        dump(result)
