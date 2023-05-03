def rule1():
    """Catur Jawa Original Rule, No Diagonal.

    Parameters
    ----------
    N/A

    Returns
    -------
    Dict :
        A Dictionary which contains movesets for a certain position for
        no diagonal rule.
    
    Notes
    -------
    Here is some visualization for the position:

    6 7 8  X X X
    3 4 5  - - -
    0 1 2  O O O
    """

    NO_DIAGONAL_DICT_RULE = {
            0 : [1,3],
            1 : [0, 2, 4],
            2 : [1, 5],
            3 : [0, 4, 6],
            4 : [1, 3, 5, 7],
            5 : [2, 4, 8],
            6 : [3, 7],
            7 : [4, 6, 8],
            8 : [5, 8]}
    return NO_DIAGONAL_DICT_RULE

def swap(state_string, num1, num2):
    """Swap 2 character based on their index

    Parameters
    ----------
    state_string : str
    The string which its char going to be swapped.

    num1 : int
        index of first character to be swapped
    
    num2 : int
        index of second character to be swapped

    Returns
    -------
    String :
        A new string which its two character has been swapped
    """

    temp1 = state_string[num1]
    temp2 = state_string[num2]
    state_string = state_string[:num1] + temp2 + state_string[num1 + 1:]
    state_string = state_string[:num2] + temp1 + state_string[num2 + 1:]
    return state_string

def all_next_moves(state_string, dict_rule):
    """find all possible moves from a board state

    Parameters
    ----------
    state_string : str
    The board state which are going to be checked its moveset

    dict_rule : dict
        A dictionary which contains rule for particular catur jawa game

    Returns
    -------
    List (String) :
        A list which contains all possible moves from input state
    """

    old_state = state_string[1:]
    whose_turn = state_string[0]
    list_new_moves = []

    next_turn = "X"
    if whose_turn == "X":
        next_turn = "O"

    for i in range(len(old_state)):
        if old_state[i] == "-":
            for j in dict_rule[i]:
                if old_state[j] == whose_turn:
                    new_move = next_turn + swap(old_state, i, j)
                    list_new_moves.append(new_move)
    
    return list_new_moves