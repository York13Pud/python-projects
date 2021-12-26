# Imports to be used:
from guizero import App, Box, PushButton, Text

# Functions area:
def clear_board():
    new_board = [[None,None,None],
                 [None,None,None],
                 [None,None,None]]
    for x_axis in range(3):
        for y_axis in range(3):
            button = PushButton(
                board, text = "", grid=[x_axis,y_axis], width = 3, command=choose_square, args=[x_axis,y_axis]
            )
            button.text_size = "24"
            button.text_color = "red"
            button.text = "-"
            new_board[x_axis][y_axis] = button
    return new_board

def choose_square(x_axis,y_axis):
    board_squares[x_axis][y_axis].text = turn
    board_squares[x_axis][y_axis].text_color = "red"
    board_squares[x_axis][y_axis].disable()
    toggle_player()
    check_win()
    
def toggle_player():
    global turn
    if turn == "X":
        turn = "O"
    else:
        turn = "X" 
    message.value = "It is your turn, " + turn

def check_win():
    winner = None
    
    # check vertical lines for a winner:
    if (board_squares[0][0].text == board_squares[0][1].text == board_squares[0][2].text) and board_squares[0][2].text in ["X", "O"]:
        winner = board_squares[0][0]
    elif (board_squares[1][0].text == board_squares[1][1].text == board_squares[1][2].text) and board_squares[1][2].text in ["X", "O"]:
        winner = board_squares[1][0]
    elif (board_squares[2][0].text == board_squares[2][1].text == board_squares[2][2].text) and board_squares[2][2].text in ["X", "O"]:
        winner = board_squares[2][0]
    # check horizontal lines for a winner:
    elif (board_squares[0][0].text == board_squares[1][0].text == board_squares[2][0].text) and board_squares[2][0].text in ["X", "O"]:
        winner = board_squares[0][0]
    elif (board_squares[0][1].text == board_squares[1][1].text == board_squares[2][1].text) and board_squares[2][1].text in ["X", "O"]:
        winner = board_squares[0][1]
    elif (board_squares[0][2].text == board_squares[1][2].text == board_squares[2][2].text) and board_squares[2][2].text in ["X", "O"]:
        winner = board_squares[0][2]
    # check diagonal lines for a winner:
    elif (board_squares[0][0].text == board_squares[1][1].text == board_squares[2][2].text) and board_squares[2][2].text in ["X", "O"]:
        winner = board_squares[0][0]
    elif (board_squares[0][2].text == board_squares[1][1].text == board_squares[2][0].text) and board_squares[2][0].text in ["X", "O"]:
        winner = board_squares[0][2]   
    
    if winner is not None:
        message.value = winner.text + " wins!"
    elif moves_taken() == 9:
        message.value = "It's a draw!"

def moves_taken():
    moves = 0
    for row in board_squares:
        for col in row:
            if col.text == "X" or col.text == "O":
                moves = moves + 1
    return moves
            

def reset_game():
    global turn
    turn = "X"
    message.value = "It is your turn, " + turn
    global board_squares
    board_squares = clear_board()
    
# Variables area:
app = App("Tic-Tac-Toe")
turn = "X"
board = Box(app, layout="grid")
board_squares = clear_board()

# Application area:
message = Text(app, text="It is your turn, " + turn)
message.text_color = "white"
message.text_size = "16"
#buttons_box = Box(app, width = "fill", align = "bottom")
reset_button = PushButton(app, command=reset_game, text = "Reset Game")
reset_button.bg = "red"

app.display()
