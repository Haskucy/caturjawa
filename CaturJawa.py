class CaturJawa:
    index = -1
    board = [["O", "O", "O"],["O", "O", "O"],["O", "O", "O"]]
    regex = "OOOOOOOOO"

    def __init__(self, index, regex):
        self.index = index
        self.regex = regex
        self.board = self.regex_to_board()
    
    def change_position(self, regex):
        self.regex = regex
        self.regex_to_board()

    def print_position(self):
        print(self.board[0])
        print(self.board[1])
        print(self.board[2])
    
    def print_regex(self):
        print(self.regex)

    def regex_to_board(self):
        fixregex = self.regex[1:]
        tempboard = [["O", "O", "O"],["O", "O", "O"],["O", "O", "O"]]
        for i in range(3):
            for j in range(3):
                tempboard[i][j] = fixregex[3*i+j]
        return tempboard