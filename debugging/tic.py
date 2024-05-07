#!/usr/bin/python3
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board):
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid input. Row and column must be between 0 and 2.")
                continue
            if board[row][col] == " ":
                board[row][col] = player
                if player == "X":
                    player = "O"
                else:
                    player = "X"
            else:
                print("That spot is already taken! Try again.")
        except ValueError:
            print("Invalid input. Row and column must be integers.")

    print_board(board)
    print("Player " + player + " wins!")

# Test all user inputs
def test_user_inputs():
    # Test invalid inputs
    invalid_inputs = [("a", "b"), (1.5, 2.5), (-1, 2), (3, 2), (0, 3)]
    for row, col in invalid_inputs:
        print("\nTesting invalid inputs:", row, col)
        board = [[" "]*3 for _ in range(3)]
        board[1][1] = "X"  # Simulate a move
        try:
            tic_tac_toe()
        except ValueError as e:
            print(e)

    # Test valid inputs
    valid_inputs = [(0, 0), (1, 2), (2, 1)]
    for row, col in valid_inputs:
        print("\nTesting valid inputs:", row, col)
        board = [[" "]*3 for _ in range(3)]
        board[1][1] = "X"  # Simulate a move
        board[row][col] = "O"  # Simulate another move
        tic_tac_toe()

if __name__ == "__main__":
    test_user_inputs()
