from visualizer.visualizer_cli import print_snapshot

#TODO : save to json

def base10_to_base3(num):
    """Convert base 10 integer to base 3.

    Parameters
    ----------
    num : int
        An integer in base 10

    Returns
    -------
    String
        A string which is base 3 integer form from num
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
    String
        A string that represent state in the form of letter
    """

    temp = state_num.replace("0", "O")
    temp1 = temp.replace("1", "-")
    return temp1.replace("2", "X")


def generating_state():
    """Create all state in catur jawa board using base 3, and return
    it as a list of string. There are 19683 state possible in catur 
    jawa board.

    Parameters
    ----------
    N/A

    Returns
    -------
    List
        a list of strings that contains all possible state of the board
    """

    state_list = []
    for i in range(3**9):
        state_num = base10_to_base3(i)
        state_letter = num_to_letter_converter(state_num)
        state_list.append(state_letter)
    
    return state_list
        

print(generating_state())