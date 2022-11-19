class Board:
    def __init__(self):
        self.board = [[None]*3 for i in range(3)]
    
    # check if board is full
    def is_full(self):
        a = 0
        for i in range(3):
            if not None in self.board[i]:
                a+=1
        if a == 3:
            return True
        return False

    # check for winner where three in a row/column/diagonal is same
    # 00 01 02
    # 10 11 12
    # 20 21 22
    def has_got_winner(self):
        for i in range(3):
            j=0
            if (not None in self.board[i]) and (self.board[i][j] == self.board[i][j+1] == self.board[i][j+2] or self.board[j][i] == self.board[j+1][i] == self.board[j+2][i]):
                return True
            
        if (not self.board[1][1] == None) and (self.board[0][0] == self.board[1][1] == self.board[2][2] or self.board[2][0] == self.board[1][1] == self.board[0][2]):
            return True
        return False
        
    def print_board(self):
        for i in range(3):
            for j in range(3):
                value = "_" if self.board[i][j] is None else self.board[i][j]
                print(value, end=" ")
            print('\n')
            
    def update_board(self, x, y, sign):
        if self.board[x][y] == None:
            self.board[x][y] = sign
        else:
            raise ValueError('Choose from the available slot i.e where value is "None"')
        
    def check_for_result(self, current_player):
        if self.has_got_winner():
            print('{} won the match'.format(current_player))
        else:
            print('Draw Match')
        self.print_board()