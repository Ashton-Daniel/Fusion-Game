class FusionGame:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]

    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print('-' * (2 * self.cols - 1))

    def place_connect_four_piece(self, col, player):
        for row in range(self.rows - 1, -1, -1):
            if self.board[row][col] == ' ':
                self.board[row][col] = player
                return True
        return False
        move_checker()

    def move_checker(self, row, col, new_row, new_col, player):
        if self.is_valid_move(row, col, new_row, new_col, player):
            self.board[new_row][new_col] = player
            self.board[row][col] = ' '
            return True
        return False

    def is_valid_move(self, row, col, new_row, new_col, player):
        if not (0 <= new_row < self.rows and 0 <= new_col < self.cols):
            return False
        if self.board[new_row][new_col] != ' ':
            return False
        if player == 'X':
            return abs(new_row - row) == 1 and abs(new_col - col) == 1
        elif player == 'O':
            return abs(new_row - row) == 1 and abs(new_col - col) == 1 and self.board[row][col] == 'O'
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
    def is_bottom_row_filled(self):
        return all(self.board[self.rows - 1][col] != ' ' for col in range(self.cols))

    def shift_rows(self):
        self.board.pop(self.rows - 1)
        self.board.insert(0, [' ' for _ in range(self.cols)])
    

game = FusionGame(rows=6, cols=7)
current_player = 'X'

while True:
    game.print_board()

    col = int(input(f"Player {current_player}, choose a column (0-{game.cols - 1}): "))
    if game.place_connect_four_piece(col, current_player):
        if game.check_winner(current_player):
            game.print_board()
            print(f"Player {current_player} wins!")
            break
        
        if game.is_bottom_row_filled():
            game.shift_rows()

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

    else:
        print("Column is full. Try again.")

    # Implement the checker movement logic here (similar to Checkers)
    # You can prompt the user for input and update the board accordingly.
    # Remember to check for a winner!

    # Break the loop when there's a winner or the board is full.
    # You can add your own winning conditions.
    

print("Game over!")