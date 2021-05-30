from spirecomm.spire.game import Game
from spirecomm.spire.character import Intent, PlayerClass
import spirecomm.spire.card
from spirecomm.spire.screen import RestOption
from spirecomm.communication.action import *
import json

def a_fetch(game):
    str = "C:\\Users\\kevinliu.cs08\\Documents\\GitHub\\spirecomm\\test.json"
    f = open(str,'w')
    f.write("in a.py\n")
    f.write(json.dumps(game.json_state, indent=4, sort_keys=True))
    f.close()
