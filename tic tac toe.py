# Define the board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Function to check for a winner
def check_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical
                      (0, 4, 8), (2, 4, 6)]             # diagonal
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

# Function to check for a draw
def is_draw(board):
    return ' ' not in board

# Function to make a move
def make_move(board, position, player):
    board[position] = player

# Function to get available moves
def available_moves(board):
    return [i for i, spot in enumerate(board) if spot == ' ']

# Human player move
def player_move(board):
    move = -1
    while move not in available_moves(board):
        move = int(input("Enter your move (0-8): "))
    make_move(board, move, 'O')