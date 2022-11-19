from board import Board

#let user select 'o' or 'x'
o = input('Enter name for player "o": ')
x = input('Enter name for player "x": ')

# check if both username are different
if o == x:
    raise ValueError('Name of both the players should not be same')

def rotate_turns(player, sign):
    if sign == 'o':
        sign = 'x'
        player = x
    else:
        sign = 'o'
        player = o
    return sign, player

sign = 'x'
board = Board()
while(board.has_got_winner() or board.is_full()):
    sign, current_player = rotate_turns(current_player, sign)
    board.print_board()
        
    # take their input
    box = input('Player {} select your box for {}: '.format(current_player,sign))
    
    # update the board 
    board.update_board(int(box[0]), int(box[1]), sign)
    
board.check_for_result(current_player)