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

    0 1 2  O O O
    3 4 5  - - -
    6 7 8  X X X
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
            8 : [5, 7]}
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


#Win Condition
def game_row(string_state, row_line, check_player):
  """Checking a row of a line

    Parameters
    ----------
    string_state: 
        The string state of the board (without turns)
    
    row_line: 
        Which row that need to be checked if its created a line
    
    check_player: 
        Whose player that needed to be check if its created a line

    Returns
    -------
    Boolean :
        True or false if player creates a line outside home line
    
    Notes
    -------
    Here is some visualization for the row and column:

                           col1 col2 col3
    0 1 2  O O O     row1    0    1    2
    3 4 5  - - -     row2    3    4    5
    6 7 8  X X X     row3    6    7    8
  """  
  row = row_line*3
  return (string_state[row] == check_player) and (string_state[row+1] == check_player) and (string_state[row+2] == check_player)

def game_column(string_state, column_line, check_player):
  """Checking a column of a line

    Parameters
    ----------
    string_state: 
        The string state of the board (without turns)
    
    column_line: 
        Which column that need to be checked if its created a line
    
    check_player: 
        Whose player that needed to be check if its created a line

    Returns
    -------
    Boolean :
        True or false if player creates a line outside home line
    
    Notes
    -------
    Here is some visualization for the row and column:

                           col1 col2 col3
    0 1 2  O O O     row1    0    1    2
    3 4 5  - - -     row2    3    4    5
    6 7 8  X X X     row3    6    7    8
  """  
  column = column_line
  return (string_state[column] == check_player) and (string_state[column+3] == check_player) and (string_state[column+6] == check_player)

def generating_win_condition(data_all_state):
  """Generate WIN CONDITION for catur jawa game

    Parameters
    ----------
    data_all_state: 
        A dictionary parsed from all_state.json

    Returns
    -------
    List of Win State :
        A list of all win state possible from checking win condition
    
    Notes
    -------
    Here is some visualization for the row and column:

                           col1 col2 col3
    0 1 2  O O O     row1    0    1    2
    3 4 5  - - -     row2    3    4    5
    6 7 8  X X X     row3    6    7    8
  """
  list_state = list(data_all_state["state_num_dict"].keys())
  list_win_state = []
  

  for i in list_state:
    turn = i[0]
    string_state = i[1:]

    # X wins
    if turn == "O": # When X wins, the O turn state has X lined up
      if game_row(string_state, 0, "X") or game_row(string_state, 1, "X"):
        list_win_state.append(i)
      elif game_column(string_state, 0, "X") or game_column(string_state, 1, "X") or game_column(string_state, 2, "X"):
        list_win_state.append(i)

    if turn == "X": # When O wins, the X turn state has O lined up
      if game_row(string_state, 1, "O") or game_row(string_state, 2, "O"):
        list_win_state.append(i)
      elif game_column(string_state, 0, "O") or game_column(string_state, 1, "O") or game_column(string_state, 2, "O"):
        list_win_state.append(i)
      else:
        continue
   
  return list_win_state