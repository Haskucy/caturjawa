import CaturJawa
from CaturJawa import CaturJawa
from ternary import ternary_adapter, ternary_to_base10

def list_regex():
    pert = []
    for i in range(39366):
        position = ternary_adapter(i)
        position = position.replace('0', 'W')
        position = position.replace('1', 'B')
        position = position.replace('2', 'X')
        pert.append(position)
    return pert

def filtered_list_regex():
    all_regex = list_regex()
    filtered_list = []
    for i in all_regex:
        without_turn = i[1:]
        if without_turn.count('B') == 3 and without_turn.count('W') == 3 and without_turn.count('X') == 3:
            filtered_list.append(i)
    return filtered_list
        
def dict_catur_jawa():
    all_regex = filtered_list_regex()

    dict_catur_index = {}
    dict_catur_regex = {}
    for i in range(len(all_regex)):
        dict_catur_index[i] = CaturJawa(i,all_regex[i])
        dict_catur_regex[all_regex[i]] = i

    dict_catur = {
        "index" : dict_catur_index,
        "regex" : dict_catur_regex
    }
    return dict_catur

"""
pert = []
def permutations(start, end=[]):
    if len(start) == 0:
        pert.append(end)
    else:
        for i in range(len(start)):
            permutations(start[:i] + start[i+1:], end + start[i:i+1])

def list_regex():
    permutations(['B','B','B','X','X','X','W','W','W'])

    for i in range(len(pert)):
        pert[i] = "".join(pert[i])

    list_all_combination = list(set(pert))
    
    return list_all_combination
"""

