from board import create_board, display_two_boards
from menu import show_logo



filenames = ["logo.txt"]

def main():
  show_logo(filenames)
  board1 = create_board(5)
  board2 = create_board(5)
  display_two_boards(board1, board2, 5)




if __name__ == "__main__":
    main()
