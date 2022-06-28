from distutils.command import check
from board import create_board, display_board, display_two_boards
from coordinates import get_all_ships, get_player_coordinates, place_a_ship
from functions import get_max_ships
from menu import check_play_again, clear, get_board_size, get_menu_option, goodbye, show_logo, show_shooting_phase_message, show_waiting_screen, show_winning_message


HUMAN_VS_HUMAN = 1
AI_VS_HUMAN = 2


filenames = ["logo.txt"]

def main():
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
        clear()
        display_two_boards(player_one_visible_board, player_two_visible_board, board_size)
        row, column = get_player_coordinates(player_one)
        if player_two_hidden_board[row][column] == "X":
          player_two_visible_board[row][column] = "S"
          player_two_ships -= 1
          clear()
          display_two_boards(player_one_visible_board, player_two_visible_board, board_size)
          if player_two_ships > 0:
            input("It's a hit, ship is sunk. ")
          else:
            is_game_running = False
            show_winning_message(player_one)
            decision = check_play_again()
            if decision.lower() == "y":
              clear()
              main()
            else:
              goodbye()
        else:
          player_two_visible_board[row][column] = "M"
          clear()
          display_two_boards(player_one_visible_board, player_two_visible_board, board_size)
          input("You\'ve missed. ")
        current_player = player_two

      while current_player == player_two:
        clear()
        display_two_boards(player_one_visible_board, player_two_visible_board, board_size)
        row, column = get_player_coordinates(player_two)
        if player_one_hidden_board[row][column] == "X":
          player_one_visible_board[row][column] = "S"
          player_one_ships -= 1
          clear()
          display_two_boards(player_one_visible_board, player_two_visible_board, board_size)
          if player_one_ships > 0:
            input("It's a hit, ship is sunk. ")
          else:
            is_game_running = False
            show_winning_message(player_two)
            decision = check_play_again()
            if decision.lower() == "y":
              clear()
              main()
            else:
              goodbye()
        else:
          player_one_visible_board[row][column] = "M"
          clear()
          display_two_boards(player_one_visible_board, player_two_visible_board, board_size)
          input("You\'ve missed. ")
        current_player = player_one

      


if __name__ == "__main__":
    main()
