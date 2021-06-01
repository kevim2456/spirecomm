import ast
from pprintpp import pprint as pp
import json

if __name__ == '__main__':
    f_Colorless_Cards = open("Colorless_Cards.txt",'r')
    f_ironclad_card = open("ironclad_card.txt",'r')
    f_Curse_Cards = open("Curse_Cards.txt",'r')
    f_Status_Cards = open("Status_Cards.txt",'r')

    Colorless_Cards = ast.literal_eval(f_Colorless_Cards.read())
    ironclad_card = ast.literal_eval(f_ironclad_card.read())
    Curse_Cards = ast.literal_eval(f_Curse_Cards.read())
    Status_Cards = ast.literal_eval(f_Status_Cards.read())

    with_upgrade = Colorless_Cards + ironclad_card + [ i+'+' for i in Colorless_Cards + ironclad_card]
    # pp(with_upgrade)
    print(len(with_upgrade))

    possi_card = with_upgrade + Curse_Cards + Status_Cards
    rlt = { k:v for v,k in enumerate(possi_card,start=1) }

    for i in Curse_Cards:
        print(i,rlt[i])
    # print(json.dumps(possi_card,indent=4))
    f = open("possi_card.json",'w')
    f.write(json.dumps(rlt,indent=4))
    f.close()

    f_Colorless_Cards.close()
    f_ironclad_card.close()
    f_Curse_Cards.close()
    f_Status_Cards.close()
