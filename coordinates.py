from turtle import right
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
  amount_of_double_ships = get_amount_of_double_ships(board_size)
  number_of_coordinates_for_double_ships = amount_of_double_ships * 2
  amount_of_single_ships = get_amount_of_single_ships(board_size)
  single_ship_counter = 0
  place_a_double_ship(player_board, board_size, player, number_of_coordinates_for_double_ships, amount_of_double_ships)
  player_ships += amount_of_double_ships
  while single_ship_counter != amount_of_single_ships:
    clear()
    display_board(player_board, board_size)
    row, column = get_player_coordinates(player, board_size)
    no_adjacent = check_adjacent_spots(row, column, player_board, board_size)
    if no_adjacent:
      are_coordinates_taken = check_if_coordinates_are_taken(player_board, row, column)
      if not are_coordinates_taken:
        place_a_ship(player_board, row, column)
        player_ships += 1
        single_ship_counter += 1
      else:
        input(colored.red("\t Error: Coordinates are already taken. "))
    else:
      input(colored.red("\t Error: Ship cannot be adjacanet. Corners only available. "))
  display_board(player_board, board_size)
  clear()
  if player_ships >= max_ships:
    display_board(player_board, board_size)
    input("You've completed your placement. Please acknowledge. ")
  return player_ships

def place_a_double_ship(player_board, board_size, player, number_of_coordinates_for_double_ships, amount_of_double_ships):
  double_ship_coordinates_counter = 0
  step_counter = 0
  while double_ship_coordinates_counter != number_of_coordinates_for_double_ships:
    if step_counter == 0:
      used_coordinates = []
      row, column = get_player_coordinates(player, board_size)
      are_coordinates_taken = check_if_coordinates_are_taken(player_board, row, column)
      if not are_coordinates_taken:
        place_a_ship(player_board, row, column)
        used_coordinates.append(row)
        used_coordinates.append(column)
        double_ship_coordinates_counter += 1
        step_counter += 1
      else:
        input(colored.red("\t Error: Coordinates are already taken. "))
    if step_counter == 1:
      clear()
      display_board(player_board, board_size)
      row, column = get_player_coordinates(player, board_size)
      valid_coordinates = check_long_ship_next_coordinates(used_coordinates, row, column)
      if valid_coordinates:
        are_coordinates_taken = check_if_coordinates_are_taken(player_board, row, column)
        if not are_coordinates_taken:
          place_a_ship(player_board, row, column)
          double_ship_coordinates_counter += 1
          step_counter += 1
        else: 
          input(colored.red("\t Error: Coordinates are already taken. "))
      else:
        input(colored.red("\t Wrong coordinates, try again. "))
    clear()
    display_board(player_board, board_size)

def place_a_ship(board, row, column):
  board[row][column] = "X"

  return board

def check_long_ship_next_coordinates(used_coordinates, row, column):
  old_row = used_coordinates[0]
  old_column = used_coordinates[1]
  max_row = old_row + 1
  max_column = old_column + 1
  if row > max_row or column > max_column:
    return False
  return True


def check_adjacent_spots(row, column, player_board, board_size):
  player_input = [row, column]
  last_spot = board_size - 1
  upper_left_corner = [0, 0]
  upper_right_corner = [0, last_spot]
  bottom_left_corner = [last_spot, 0]
  bottom_right_corner = [last_spot, last_spot]
  first_row = [0, column]
  first_column = [row, 0]
  last_row = [last_spot, column]
  last_column = [row, last_spot]

  if player_input == upper_left_corner:
    if player_board[row][column + 1] == "X" or player_board[row + 1][column] == "X":
      return False
  elif player_input == upper_right_corner:
    if player_board[row][column - 1] == "X" or player_board[row + 1][column] == "X":
      return False
  elif player_input == bottom_left_corner:
    if player_board[row - 1][column] == "X" or player_board[row][column + 1] == "X":
      return False
  elif player_input == bottom_right_corner:
    if player_board[row - 1][column] == "X" or player_board[row][column - 1] == "X":
      return False
  elif player_input == first_row:
    if player_board[row][column - 1] == "X" or player_board[row][column + 1] == "X":
      return False
  elif player_input == first_column:
    if player_board[row][column + 1] == "X" or player_board[row - 1][column] == "X" or player_board[row + 1][column] == "X":
      return False
  elif player_input == last_row:
    if player_board[row][column - 1] == "X" or player_board[row - 1][column] == "X" or player_board[row][column + 1] == "X":
      return False
  elif player_input == last_column:
    if player_board[row][column - 1] == "X" or player_board[row + 1][column] == "X" or player_board[row - 1][column] == "X":
      return False
  else:
    if player_board[row - 1][column] == "X" or player_board[row + 1][column] == "X" or player_board[row][column - 1] == "X" or player_board[row][column + 1] == "X":
      return False
  return True

def get_amount_of_double_ships(board_size):
  amount_of_double_ships = board_size // 3
  return amount_of_double_ships

def get_amount_of_single_ships(board_size):
  amount_of_single_ships = board_size // 2
  return amount_of_single_ships

def check_if_coordinates_are_taken(player_board, row, column):
  if player_board[row][column] == "X":
    return True
  return False