import itertools
import datetime
import sys

from spirecomm.communication.coordinator import Coordinator
from spirecomm.ai.agent import SimpleAgent
from spirecomm.spire.character import PlayerClass
from spirecomm.RL.model import Model


if __name__ == "__main__":
    agent = SimpleAgent()
    agent.set_dump() # you can place your path/file to dump
    brain = Model()
    agent.register_push_data_callback(brain.get_data)
    coordinator = Coordinator()
    coordinator.set_dump() # you can place your path/file to dump
    coordinator.signal_ready()
    coordinator.register_command_error_callback(agent.handle_error)
    coordinator.register_state_change_callback(agent.get_next_action_in_game)
    coordinator.register_out_of_game_callback(agent.get_next_action_out_of_game)

    # Play games forever with ironclad
    agent.change_class(PlayerClass.IRONCLAD)
    # while(True):
    result = coordinator.play_one_game(PlayerClass.IRONCLAD)
