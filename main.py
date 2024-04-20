import random


def print_board(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("-----------")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("-----------")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])


def check_win(board, player):
    wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for i, j, k in wins:
        if board[i] == board[j] == board[k] == player:
            return True
    return False


def check_draw(board):
    return " " not in board


def get_player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == " ":
                return move
            else:
                print("That space is already occupied. Choose another.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")


def get_computer_move(board):
    available_moves = [i for i, x in enumerate(board) if x == " "]
    return random.choice(available_moves)


def play_game():
    board = [" " for _ in range(9)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
    while True:
        # Player's move
        player_move = get_player_move(board)
        board[player_move] = "X"
        print_board(board)
        if check_win(board, "X"):
            print("Congratulations! You win!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break

        # Computer's move
        print("Computer's turn:")
        computer_move = get_computer_move(board)
        board[computer_move] = "O"
        print_board(board)
        if check_win(board, "O"):
            print("Computer wins! Better luck next time.")
            break
        elif check_draw(board):
            print("It's a draw!")
            break


play_game()
