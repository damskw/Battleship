from clint.textui import colored
from board import display_two_boards
from coordinates import check_adjacent_spots

from menu import clear

def get_max_ships(board_size):
    max_ships = (board_size // 2) + 1
    return max_ships

def take_a_shot(row, column, opponent_hidden_board, opponent_visible_board, opponent_player_ships):
    sunk = "sunk"
    miss = "miss"
    retake = "retake"
    hit = "hit"
    no_adjacent = check_adjacent_spots(row, column, opponent_hidden_board)
    if opponent_hidden_board[row][column] == "X" and opponent_visible_board[row][column] == "0" and no_adjacent:
        opponent_visible_board[row][column] = "S"
        opponent_player_ships -= 1
        action = sunk
    elif opponent_hidden_board[row][column] == "X" and opponent_visible_board[row][column] == "0" and not no_adjacent:
        opponent_visible_board[row][column] = "H"
        opponent_player_ships -= 1
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
    input(colored.red("You've missed! "))

def show_retake_message():
    input(colored.red("You've alredy guessed that spot, try again! "))

def show_sunk_message():
    input(colored.red("It's a hit, you've sunken enemy's battleship! "))

def show_hit_message():
    input(colored.red("You've hit enemy's battleship but it's still standing! "))

def update_screen(player_one_visible_board, player_two_visible_board, board_size):
    clear()
    display_two_boards(player_one_visible_board, player_two_visible_board, board_size)

def change_player(player):
    next_player = player
    return next_player

def get_player_name():
  player_one = input("Enter your nickname: ")
  player_two = input("Enter your nickname: ")
  return player_one, player_two