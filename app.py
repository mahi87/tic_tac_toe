from board import Board
from player import Player

#let user select 'o' or 'x'
o = input('Enter name for player "o": ')
x = input('Enter name for player "x": ')

# check if both username are different
if o == x:
    raise ValueError('Name of both the players should not be same')

player1 = Player(o, 'o')
player2 = Player(x, 'x')

def rotate_turns(player):
    if player == player1:
        return player2
    return player1

board = Board()
current_player = player2
while(board.has_got_winner() or board.is_full()):
    current_player = rotate_turns(current_player)
    board.print_board()
        
    # take their input
    box = input('Player {} select your box for {}: '.format(current_player.name,current_player.sign))
    
    # update the board 
    board.update_board(int(box[0]), int(box[1]), current_player.sign)
    
board.check_for_result(current_player)