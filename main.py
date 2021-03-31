''' This is the main'''

from CaturJawa import CaturJawa
from caturjawadict import dict_catur_jawa

print("its working")

setup = CaturJawa(0,"WBBBXXXWWW")
setup.change_position("BBBBXWXWXW")
setup.print_position()

catur_dict = dict_catur_jawa()
no1 = catur_dict["regex"]["WBBBWWWXXX"]
no1obj = catur_dict["index"][no1]

no1_nextmove = no1obj.nextmove

for i in no1_nextmove:
    print("")
    i.print_position()
    print(i.regex)
