#Board
board = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
]
current_player = ''

#display board
def display_board():
    for row in board:
        print(row)

#check player 
def validate_player(player):
    #output result
    if player == 'X' or player == 'O':
        if player == 'O':
            print(f'You are player {player} and opponent is player X')
            display_board()
        else:
            print(f'You are player {player} and opponent is player O')
            display_board()
    else:
        print('Invalid selection')

#MAKE MOVE
def move_player(selection):
    move = selection.split()
    move_row = int(move[0]) - 1
    move_column = int(move[1]) - 1
    if board[move_row][move_column] != ('X' or 'O'): 
        board[move_row][move_column] = current_player
        display_board()
    else:
        print('Position is filled')


#Select player
print('--------TIC-TAC TOE PYTHON---------')
print('Select player: X or O')

#player selection
player = input('')
validate_player(current_player)
current_player = player

print('hint: to make a selection use the numbers on the board, eg: 1 3')

def call_move():
    #move player
    selection = input()
    move_player(selection)

while True:
    if current_player == 'X':
        call_move()
        current_player = 'O'
        print(f'Player {current_player} turn to play')
    else:
        call_move()
        current_player = 'X'
        print(f'Player {current_player} turn to play')