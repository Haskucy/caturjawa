from CaturJawa import CaturJawa
from caturjawadict import dict_catur_jawa
from ternary import ternary_adapter, ternary_to_base10

print("its working")

setup = CaturJawa(0,"WBBBXXXWWW")
next = setup.change_position("BBBBXWXWXW")
setup.print_position()

catur_dict = dict_catur_jawa()
print("d")
no1 = catur_dict["index"][1]
no1.print_position()


def all_kombination():
    pass