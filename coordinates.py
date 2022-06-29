from board import display_board
from menu import clear
from clint.textui import colored


def letters_to_numbers():
  dictionary = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10}
  return dictionary

def get_player_coordinates(player, board_size):
    wrong = False
    max_value = board_size - 1
    convert = letters_to_numbers()
    while True:
      if not wrong:
        selected_option = input(f"{player}, please enter coordinates: ")
      else:
        selected_option = input(colored.red("Wrong value! Please try again. "))
      try:
        row = int(convert[selected_option[0].upper()])
        column = int(selected_option[1]) - 1
        if row <= max_value and column <= max_value and row >= 0 and column >= 0:
          break
        else:
          wrong = True
          continue
      except:
        wrong = True
        continue
    return row, column

def get_all_ships(player_board, board_size, player_ships, max_ships, player):
  display_board(player_board, board_size)
  while True:
    row, column = get_player_coordinates(player, board_size)
    no_adjacent = check_adjacent_spots(row, column, player_board)
    if no_adjacent:
      place_a_ship(player_board, row, column)
      player_ships += 1
      break
    else:
      print(colored.red("\t Error: Ship cannot be adjacanet. Corners only available. "))
      continue
  display_board(player_board, board_size)
  clear()
  if player_ships == max_ships:
    display_board(player_board, board_size)
    input("You've completed your placement. Please acknowledge. ")
  return player_ships

def place_a_ship(board, row, column):
    board[row][column] = "X"

    return board

def check_adjacent_spots(row, column, player_board):
  if player_board[row -1][column] == "X":
    return False
  elif player_board[row][column + 1] == "X":
    return False
  elif player_board[row][column - 1] == "X":
    return False
  elif player_board[row + 1][column] == "X":
    return False
  return True