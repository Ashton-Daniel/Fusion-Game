import os

# Class
class FusionGame:
    # Initialize the board with the given number of rows and columns
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        # Creates a 2D list to represent the board
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]

    
    # A function to print the board
    def print_board(self):
        for row in self.board:
            print('|' + '|'.join(f' {cell} ' for cell in row) + '|')
        print('|', end='')
        for i in range(1, self.cols + 1):    
            print(f'{i:^3}|', end='')  
        print()

    # A function to place a piece in the board
    def place_connect_four_piece(self, col, player):
        for row in range(self.rows - 1, -1, -1):
            # Checks to see if each cell in the column is empty
            if self.board[row][col] == ' ':
                # Places the piece in the first empty cell
                self.board[row][col] = player
                return True
        return False

    def check_winner(self, player):
        # Check for vertical, horizontal, and diagonal connections
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == player:
                    # Check vertical
                    if row + 3 < self.rows and all(self.board[row + i][col] == player for i in range(4)):
                        return True
                    # Check horizontal
                    if col + 3 < self.cols and all(self.board[row][col + i] == player for i in range(4)):
                        return True
                    # Check diagonal (top-left to bottom-right)
                    if row + 3 < self.rows and col + 3 < self.cols and all(self.board[row + i][col + i] == player for i in range(4)):
                        return True
                    # Check diagonal (top-right to bottom-left)
                    if row + 3 < self.rows and col - 3 >= 0 and all(self.board[row + i][col - i] == player for i in range(4)):
                        return True
        return False
    
    # Function to check if bottom row is filled
    def is_bottom_row_filled(self):
        # If all cells in the bottom row are filled return True
        return all(self.board[self.rows - 1][col] != ' ' for col in range(self.cols))

    # Function to remove the bottom row and add a row to the top
    def shift_rows(self):
        # Remove bottom row
        self.board.pop(self.rows - 1)
        # Add a new row to the top
        self.board.insert(0, [' ' for _ in range(self.cols)])

# Function to get the size of the board
def board_size(inputType):
    while True:
        # Ask user how big the board should be
        inputValueString = input(f"How many {inputType} should the board have?")
        # If the input is empty, return the default value for a standard board
        if inputValueString == "":
            return 6
        # If the input is "exit", exit the program
        elif inputValueString == "exit":
            exit()
        # If the input is not a number, ask the user to enter a number
        elif inputValueString.isnumeric() == False:
            print("Invalid input. Please enter a number between 2 and 10.")
        # If the input is less than 2, ask the user to enter a number between 2 and 10
        elif int(inputValueString) < 2:
            print("Number is too low. Please enter a number between 2 and 10.")
        # If the input is greater than 10, ask the user to enter a number between 2 and 10
        elif int(inputValueString) > 10:
            print("Number is too high. Please enter a number between 2 and 10.")
        # If the input is a valid number, return the number
        else:            
            return int(inputValueString)
        
# Calls the function to determine the number of rows
rows = board_size("rows")
# Calls the function to determine the number of columns
columns = board_size("columns")
# Clears the terminal
os.system("cls")
# Creates a new game with the given number of rows and columns
game = FusionGame(rows, columns)
# Sets the current player to X


# Main game loop
def Main_Game_Loop():
    current_player = 'X'
    while True:
        # Calls the print board function
        game.print_board()
        # Asks the current player to choose a column
        try:
            col = int(input(f"Player {current_player}, choose a column (1 - {game.cols}): ")) - 1
            # If the column is not between 0 and the number of columns, raise a ValueError
            if not 0 <= col < game.cols:
                raise ValueError
        # If the input is not a valid column, ask the user to enter a new number
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 6.")
            continue

        # If the column is not full, place the piece
        if game.place_connect_four_piece(col, current_player):
            # Check if the current player has won
            if game.check_winner(current_player):
                # Clear the current board
                os.system("cls")
                # Print the winning board
                game.print_board()
                # Print the winning player
                print(f"Player {current_player} wins!")
                break
            
            if game.is_bottom_row_filled():
                game.shift_rows()

            # Switch players
            current_player = 'O' if current_player == 'X' else 'X'
            os.system("cls")
        else:
            print("Column is full. Try again.")
Main_Game_Loop()