from distutils.command import check
from board import create_board, display_board, display_two_boards
from coordinates import get_all_ships, get_player_coordinates, place_a_ship
from functions import check_if_has_ships, get_max_ships, change_player, show_miss_message, show_retake_message, show_sunk_message, take_a_shot, update_screen
from menu import check_play_again, clear, get_board_size, get_menu_option, goodbye, show_logo, show_shooting_phase_message, show_waiting_screen, show_winning_message
from clint.textui import colored


HUMAN_VS_HUMAN = 1
AI_VS_HUMAN = 2


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
  sunk = "sunk"
  miss = "miss"
  retake = "retake"
  player_one_ships = 0
  player_two_ships = 0
  current_player = "Player one"
  player_one = "Player one"
  player_two = "Player two"
  is_game_running = True
  show_logo(filenames)
  game_mode = get_menu_option()
  clear()
  board_size = get_board_size()
  max_ships = get_max_ships(board_size)
  clear()
  if game_mode == HUMAN_VS_HUMAN:
    player_one_hidden_board = create_board(board_size)
    player_two_hidden_board = create_board(board_size)
    player_one_visible_board = create_board(board_size)
    player_two_visible_board = create_board(board_size)
    while player_one_ships != max_ships:
      player_one_ships = get_all_ships(player_one_hidden_board, board_size, player_one_ships, max_ships, player_one)
    clear()
    show_waiting_screen("Asia", "Kasia")
    while player_two_ships != max_ships:
      player_two_ships = get_all_ships(player_two_hidden_board, board_size, player_two_ships, max_ships, player_two)
    clear()
    show_shooting_phase_message()
    while is_game_running:
      while current_player == player_one:
        update_screen(player_one_visible_board, player_two_visible_board, board_size)
        row, column = get_player_coordinates(player_one, board_size)
        action, player_two_ships, player_two_visible_board[row][column] = take_a_shot(row, column, player_two_hidden_board, player_two_visible_board, player_two_ships)
        if action == sunk:
          update_screen(player_one_visible_board, player_two_visible_board, board_size)
          show_sunk_message()
          still_has_ships = check_if_has_ships(player_two_ships)
          if still_has_ships:
            current_player = change_player(player_two)
          else:
            show_winning_message(current_player)
            check_play_again()
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
        action, player_one_ships, player_one_visible_board[row][column] = take_a_shot(row, column, player_one_hidden_board, player_one_visible_board, player_one_ships)
        if action == sunk:
          update_screen(player_one_visible_board, player_two_visible_board, board_size)
          show_sunk_message()
          still_has_ships = check_if_has_ships(player_one_ships)
          if still_has_ships:
            current_player = change_player(player_one)
          else:
            show_winning_message(current_player)
            check_play_again()
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
