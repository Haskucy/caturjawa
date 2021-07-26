import json
from .next_moves import all_next_moves, rule1

#TODO : save to json

def base10_to_base3(num):
    """Convert base 10 integer to base 3.

    Parameters
    ----------
    num : int
        An integer in base 10

    Returns
    -------
    String :
        A string which is base 3 integer form from input
    """

    if num < 0:
        return "-" + str(base10_to_base3(num*-1))
    if num == 0:
        return "0"*9
    numbers = []
    while num:
        num, r = divmod(num, 3)
        numbers.append(str(r))
    hasil = ''.join(reversed(numbers))
    zeroes = "0"*(9-len(hasil))
    return zeroes + hasil

def num_to_letter_converter(state_num):
    """Convert state form from number(0, 1, 2) to letter (O, -, X)

    Parameters
    ----------
    state_num : str
        A string that represent state in the form of number

    Returns
    -------
    String :
        A string that represent state in the form of letter
    """

    temp = state_num.replace("0", "O")
    temp1 = temp.replace("1", "-")
    return temp1.replace("2", "X")


def generating_state_unconstrained():
    """Create all state in catur jawa board using base 3, and return
    it as a list of string. There are 19683 state possible in catur 
    jawa board.

    Parameters
    ----------
    N/A

    Returns
    -------
    List :
        a list of strings that contains all possible state of the board
    """

    state_list = []
    for i in range(3**9):
        state_num = base10_to_base3(i)
        state_letter = num_to_letter_converter(state_num)
        state_list.append(state_letter)
    
    return state_list

def generating_state():
    """Create all state constrained by 3 stone per type, (3 X stone, 
    3 O stone and 3 spaces) in catur jawa board, and return it as a 
    list of string. There are 19683 state possible in catur 
    jawa board.

    Parameters
    ----------
    N/A

    Returns
    -------
    List :
        a list of strings that contains all possible state of the board
    """

    state_list = []
    for i in range(3**9):
        state_num = base10_to_base3(i)
        state_letter = num_to_letter_converter(state_num)
        
        isConstrainedX = state_letter.count("X") == 3
        isConstrainedO = state_letter.count("O") == 3
        isConstrainedStrip = state_letter.count("-") == 3
        
        if (isConstrainedX and isConstrainedO and isConstrainedStrip):
            state_list.append(state_letter)
    
    state_list_O = []
    for i in state_list:
        new_state_letter = "O" + i
        state_list_O.append(new_state_letter)
    
    state_list_X = []
    for i in state_list:
        new_state_letter = "X" + i
        state_list_X.append(new_state_letter)
    
    state_list = state_list_O + state_list_X
    return state_list

def save_all_state_to_json(list_all_state_input, filename):
    """Creating a JSON file which contains key and value of all state
    that could happen in catur jawa board.

    Parameters
    ----------
    list_all_state_input : List(str)
    filename : str

    Returns
    -------
    N/A
    
    Notes
    -----
        This function will create JSON named "[filename].json" that will
        be saved on a folder named "data".
    """
    num_state_dict = {}
    state_num_dict = {}
    state_dict = {}
    list_all_state = list_all_state_input
    list_key = list(range(len(list_all_state)))

    for i in list_key:
        num_state_dict[str(i)] = list_all_state[i]
        state_num_dict[list_all_state[i]] = str(i)
    
    state_dict = {"num_state_dict": num_state_dict, "state_num_dict": state_num_dict}
    file_name = filename if (".json" in filename) else (filename + ".json")

    json_string = json.dumps(state_dict)
    jsonFile = open(file_name, "w")
    jsonFile.write(json_string)
    jsonFile.close()

def save_all_state_next_moves_to_json(filename):
    """Creating a JSON file which contains all state and its movesets

    Parameters
    ----------
    filename : str

    Returns
    -------
    N/A
    
    Notes
    -----
        This function will create JSON named "[filename].json" that will
        be saved on a folder named "data".
    """

    f = open('all_state.json',)
    data = json.load(f)
    f.close()

    all_state_moves_dict = {}
    list_all_state = list(data["num_state_dict"].values())

    for i in list_all_state:
        list_possible_moves = all_next_moves(i, rule1())
        all_state_moves_dict[i] = list_possible_moves
    
    file_name = filename if (".json" in filename) else (filename + ".json")

    json_string = json.dumps(all_state_moves_dict)
    jsonFile = open(file_name, "w")
    jsonFile.write(json_string)
    jsonFile.close()