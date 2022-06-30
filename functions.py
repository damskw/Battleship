from clint.textui import colored
from board import display_two_boards

from menu import clear

def get_max_ships(board_size):
    max_ships = (board_size // 2) + 1
    return max_ships

def take_a_shot(row, column, opponent_hidden_board, opponent_visible_board, opponent_player_ships, board_size):
    sunk = "sunk"
    miss = "miss"
    retake = "retake"
    hit = "hit"
    no_adjacent = check_adjacent_spots(row, column, opponent_hidden_board, board_size)
    double_ship_is_sunk = check_if_double_ship_is_sunk(row, column, opponent_visible_board, board_size)
    if opponent_hidden_board[row][column] == "X" and opponent_visible_board[row][column] == "0" and no_adjacent:
        opponent_visible_board[row][column] = "S"
        opponent_player_ships -= 1
        action = sunk
    elif opponent_hidden_board[row][column] == "X" and opponent_visible_board[row][column] == "0" and not no_adjacent:
        if double_ship_is_sunk:
            opponent_visible_board[row][column] = "S"
            opponent_player_ships -= 1
            action = sunk
        else:
            opponent_visible_board[row][column] = "H"
            action = hit
    elif opponent_hidden_board[row][column] == "0":
        opponent_visible_board[row][column] = "M"
        action = miss
    elif opponent_visible_board[row][column] == "S" or "H" or "M":
        action = retake
    
    return action, opponent_player_ships, opponent_visible_board[row][column]

def check_if_has_ships(player_ships):
    if player_ships > 0:
        return True
    else:
        return False

def show_miss_message():
    input(colored.blue("You've missed! "))

def show_retake_message():
    input(colored.red("You've alredy guessed that spot, try again! "))

def show_sunk_message():
    input(colored.red("It's a hit and you've sunken enemy's battleship! "))

def show_hit_message():
    input(colored.yellow("You've hit enemy's battleship but it's still standing! "))

def show_coordinates_are_taken_message():
    input(colored.red("\t Error: Coordinates are already taken. "))

def show_invalid_coordinates_message():
    input(colored.red("\t Wrong coordinates, try again. "))

def show_are_adjacent_error_message():
    input(colored.red("\t Error: Ship cannot be adjacent. Corners only available. "))

def show_completed_placement_message():
    input("You've completed your placement. Please acknowledge. ")

def show_double_ship_information():
    print("You're going to place a double ship. Enter first, then second coordinates. ")

def show_double_ship_second_coordinates_information():
    print("Please enter second coordinates for a double ship. ")

def update_screen(player_one_visible_board, player_two_visible_board, board_size):
    clear()
    display_two_boards(player_one_visible_board, player_two_visible_board, board_size)

def change_player(player):
    next_player = player
    return next_player

def get_player_name():
  player_one = input("Please enter name for first player: ")
  clear()
  player_two = input("Please enter name for second player: ")
  clear()
  return player_one, player_two

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

def check_if_double_ship_is_sunk(row, column, player_board, board_size):
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
    if player_board[row][column + 1] == "H" or player_board[row + 1][column] == "H":
      return True
  elif player_input == upper_right_corner:
    if player_board[row][column - 1] == "H" or player_board[row + 1][column] == "H":
      return True
  elif player_input == bottom_left_corner:
    if player_board[row - 1][column] == "H" or player_board[row][column + 1] == "H":
      return True
  elif player_input == bottom_right_corner:
    if player_board[row - 1][column] == "H" or player_board[row][column - 1] == "H":
      return True
  elif player_input == first_row:
    if player_board[row][column - 1] == "H" or player_board[row][column + 1] == "H":
      return True
  elif player_input == first_column:
    if player_board[row][column + 1] == "H" or player_board[row - 1][column] == "H" or player_board[row + 1][column] == "H":
      return True
  elif player_input == last_row:
    if player_board[row][column - 1] == "H" or player_board[row - 1][column] == "H" or player_board[row][column + 1] == "H":
      return True
  elif player_input == last_column:
    if player_board[row][column - 1] == "H" or player_board[row + 1][column] == "H" or player_board[row - 1][column] == "H":
      return True
  else:
    if player_board[row - 1][column] == "H" or player_board[row + 1][column] == "H" or player_board[row][column - 1] == "H" or player_board[row][column + 1] == "H":
      return True
  return False