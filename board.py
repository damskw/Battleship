def create_board(board_size):
  clean_board = []
  for size in range(board_size):
    clean_board.append(["0"] * board_size)
  return clean_board


def letters_dictionary():
  dictionary = {0: "A", 1: "B", 2: "C", 3: "D", 4:"E", 5:"F", 6: "G", 7: "H"}
  return dictionary



def display_board(board, board_size):
  show_column_numbers("   ", board_size)
  print("\r")
  show_rows_for_one_board(board, board_size)


def show_column_numbers(blank, board_size):
  show_space = True
  for number in range(board_size):
    if show_space:
      print(blank + str(number + 1), end = "  ")
      show_space = False
    else:
      print(str(number + 1), end = "  ")

def show_player_names_above_boards(player_one, player_two):
  print("    "+ player_one, end = "\t\t")
  print(player_two, end = "\t")
  print("\r")

def show_rows_for_one_board(board, board_size):
    numbers_to_letters = letters_dictionary()
    column = 0
    new_row = True
    
    for row in range(board_size):
      letter = numbers_to_letters[row]

      while column != board_size:
        if new_row:
          print(letter + "  " + board[row][column], end = " ")
          new_row = False
          column += 1
        else:
          print(" " + board[row][column], end = " ")
          column += 1
      new_row = True
      print("\r")
      column = 0
      new_row = True


def display_two_boards(board1, board2, board_size, player_one, player_two):
  show_player_names_above_boards(player_one, player_two)
  show_column_numbers("   ", board_size)
  show_column_numbers("    ", board_size)
  print("\r") 
  show_rows_for_two_boards(board1, board2, board_size)


def show_rows_for_two_boards(board1, board2, board_size):
    numbers_to_letters = letters_dictionary()
    column_board_1 = 0
    column_board_2 = 0
    new_row = True
    for row in range(board_size):
      letter = numbers_to_letters[row]

      while column_board_1 != board_size:
        if new_row:
          print(letter + "  " + board1[row][column_board_1], end = " ")
          new_row = False
          column_board_1 += 1
        else:
          print(" " + board1[row][column_board_1], end = " ")
          column_board_1 += 1
      new_row = True

      while column_board_2 != board_size:
        if new_row:
          print("  " + letter + "  " + board2[row][column_board_2], end = " ")
          column_board_2 += 1
          new_row = False
        else:
          print(" " + board2[row][column_board_2], end = " ")
          column_board_2 += 1


      print("\r")
      column_board_1 = 0
      column_board_2 = 0
      new_row = True