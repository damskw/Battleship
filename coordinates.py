from board import display_board
from menu import clear


def letters_to_numbers():
  dictionary = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10}
  return dictionary

def get_player_coordinates(player):
    convert = letters_to_numbers()
    selected_option = input(f"{player}, please enter coordinates: ")
    row = convert[selected_option[0].upper()]
    column = selected_option[1]
    return int(row), int(column) - 1

def get_all_ships(players_board, board_size, player_ships, max_ships, player):
  display_board(players_board, board_size)
  row, column = get_player_coordinates(player)
  place_a_ship(players_board, row, column)
  player_ships += 1
  display_board(players_board, board_size)
  clear()
  if player_ships == max_ships:
    display_board(players_board, board_size)
    input("You've completed your placement. Please acknowledge. ")
  return player_ships

def place_a_ship(board, row, column):
    board[row][column] = "X"

    return board

def end_game():
  return None
