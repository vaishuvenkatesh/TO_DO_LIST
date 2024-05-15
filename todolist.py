import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def get_player_move(board, player):
    while True:
        try:
            row = int(input(f"Player {player}, enter the row (0, 1, 2): "))
            col = int(input(f"Player {player}, enter the column (0, 1, 2): "))

            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                return row, col
            else:
                print("Invalid move. Try again.")

        except ValueError:
            print("Invalid input. Please enter a number.")

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = random.choice(players)

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        row, col = get_player_move(board, current_player)
        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_tic_tac_toe()
