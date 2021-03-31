import copy

def searchX(board):
    listX = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X" :
                listX.append([i,j])
    return listX

def find_turn_stone(turns, listF, board):
    first_list = []
    for coor in listF:
        second_list = []
        oldi = coor[0]
        oldj = coor[1]
        try:
            i = oldi-1
            j = oldj
            if board[i][j] == turns and i>=0 and j>=0:
                second_list.append([i, j])
        except :
            pass
        try:
            i = oldi
            j = oldj+1
            if board[i][j] == turns and i>=0 and j>=0:
                second_list.append([i, j])
        except:
            pass
        try:
            i = oldi+1
            j = oldj
            if board[i][j] == turns and i>=0 and j>=0:
                second_list.append([i, j])
        except:
            pass
        try:
            i = oldi
            j = oldj-1
            if board[i][j] == turns and i>=0 and j>=0:
                second_list.append([i, j])
        except:
            pass
        first_list.append(second_list)
    return first_list

def all_possible_swap(listF, turn, boardq):
    all_near_stone = find_turn_stone(turn, listF, boardq)
    listboard = []
    for indexi in range(len(all_near_stone)):
        coorx = listF[indexi]
        nearstone = all_near_stone[indexi]
        for coorstone in nearstone:
            newboard = copy.deepcopy(boardq)
            tempturn = newboard[coorstone[0]][coorstone[1]]
            newboard[coorx[0]][coorx[1]] = tempturn
            newboard[coorstone[0]][coorstone[1]] = "X"
            listboard.append(copy.deepcopy(newboard))
    return listboard

def find_all_next_moves(board, turn):
    listF = searchX(board)
    nextturn = "B" if turn == "W" else "W"
    nextmove = all_possible_swap(listF, turn, board)
    list_regex = []
    for every_board in nextmove:
        board_regex = board_to_regex(every_board, nextturn)
        list_regex.append(board_regex)
    return list_regex

def board_to_regex(board, turn):
    regex = turn
    for i in range(3):
        for j in range(3):
            regex = regex + board[i][j]
    return regex

def regex_to_board(regex):
    fixregex = regex[1:]
    tempboard = [["O", "O", "O"],["O", "O", "O"],["O", "O", "O"]]
    for i in range(3):
        for j in range(3):
            tempboard[i][j] = fixregex[3*i+j]
    return tempboard