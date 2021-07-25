def print_snapshot(string_state):
    """Prints the state of boards visually

    Parameters
    ----------
    string_state : str
        Strings that describe the state of board
    
    Returns
    -------
    N/A
    """
    
    if len(string_state) != 9:
        print("failed to process " + string_state)
        print("Input state too short or too long.")
        return
    
    UPROW = string_state[0:3]
    MIDROW = string_state[3:6]
    DOWNROW = string_state[6:9]
    SPACE = " | "

    print("String State: " + string_state)
    print(UPROW[0] + SPACE + UPROW[1] + SPACE + UPROW[2])
    print(MIDROW[0] + SPACE + MIDROW[1] + SPACE + MIDROW[2])
    print(DOWNROW[0] + SPACE + DOWNROW[1] + SPACE + DOWNROW[2])
    print()
