from distutils.command import check
from board import *
from coordinates import *
from functions import *
from menu import *


HUMAN_VS_HUMAN = 1
AI_VS_HUMAN = 2
EXIT = 3


filenames = ["logo.txt"]

def check_play_again():
  while True:
    decision = input("Would you like to play again? (y/n) ")
    if decision.lower() == "y":
      clear()
      main()
      break
    elif decision.lower() == "n":
      goodbye()
    else:
      continue

def main():
  clear()
  show_logo(filenames)
  game_mode = get_menu_option()
  clear()
  board_size = get_board_size()
  max_ships = get_max_ships(board_size)
  clear()
  sunk = "sunk"
  miss = "miss"
  retake = "retake"
  hit = "hit"
  player_one_ships = 0
  player_two_ships = 0
  is_game_running = True
  if game_mode == HUMAN_VS_HUMAN:
    player_one_hidden_board = create_board(board_size)
    player_two_hidden_board = create_board(board_size)
    player_one_visible_board = create_board(board_size)
    player_two_visible_board = create_board(board_size)
    player_one, player_two = get_player_name()
    current_player = player_one
    while player_one_ships < max_ships:
      player_one_ships = get_all_ships(player_one_hidden_board, board_size, player_one_ships, max_ships, player_one)
    clear()
    show_waiting_screen(player_one, player_two)
    while player_two_ships < max_ships:
      player_two_ships = get_all_ships(player_two_hidden_board, board_size, player_two_ships, max_ships, player_two)
    clear()
    show_shooting_phase_message()
    while is_game_running:
      while current_player == player_one:
        update_screen(player_one_visible_board, player_two_visible_board, board_size)
        row, column = get_player_coordinates(player_one, board_size)
        action, player_two_ships, player_two_visible_board[row][column] = take_a_shot(row, column, player_two_hidden_board, player_two_visible_board, player_two_ships, board_size)
        if action == sunk:
          update_screen(player_one_visible_board, player_two_visible_board, board_size)
          show_sunk_message()
          still_has_ships = check_if_has_ships(player_two_ships)
          if still_has_ships:
            current_player = change_player(player_two)
          else:
            show_winning_message(current_player)
            check_play_again()
        elif action == hit:
          update_screen(player_one_visible_board, player_two_visible_board, board_size)
          show_hit_message()
          current_player = change_player(player_two)
        elif action == miss:
          update_screen(player_one_visible_board, player_two_visible_board, board_size)
          show_miss_message()
          current_player = change_player(player_two)
        elif action == retake:
          update_screen(player_one_visible_board, player_two_visible_board, board_size)
          show_retake_message()
          current_player = change_player(player_one)

      while current_player == player_two:
        update_screen(player_one_visible_board, player_two_visible_board, board_size)
        row, column = get_player_coordinates(player_two, board_size)
        action, player_one_ships, player_one_visible_board[row][column] = take_a_shot(row, column, player_one_hidden_board, player_one_visible_board, player_one_ships, board_size)
        if action == sunk:
          update_screen(player_one_visible_board, player_two_visible_board, board_size)
          show_sunk_message()
          still_has_ships = check_if_has_ships(player_one_ships)
          if still_has_ships:
            current_player = change_player(player_one)
          else:
            show_winning_message(current_player)
            check_play_again()
        elif action == hit:
          update_screen(player_one_visible_board, player_two_visible_board, board_size)
          show_hit_message()
          current_player = change_player(player_two)
        elif action == miss:
          update_screen(player_one_visible_board, player_two_visible_board, board_size)
          show_miss_message()
          current_player = change_player(player_one)
        elif action == retake:
          update_screen(player_one_visible_board, player_two_visible_board, board_size)
          show_retake_message()
          current_player = change_player(player_two)

      


if __name__ == "__main__":
    main()
