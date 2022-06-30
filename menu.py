from os import name, system
import os
import sys
from clint.textui import colored

filenames = ["logo.txt"]

def ask_for_any_key():
  os.system('pause')

def clear():
  if name == 'nt':
    _ = system('cls')

def show_logo(filenames):
  frames = []
  for name in filenames:
    with open(name, "r", encoding = "utf8") as f:
      frames.append(f.readlines())
    for frame in frames:
      print(colored.blue("".join(frame))) 
  print("\n")

def goodbye():
  goodbye = ("Goodbye!")
  print(colored.yellow(goodbye))
  sys.exit()

def get_menu_option():
  available_options = ["1","2", "3"]
  selected_option = input("Please choose one of the following options:\n"
                    "1. Human vs Human\n"
                    "2. AI vs Human\n"
                    "3. Exit game\n")
  if selected_option.lower() == "quit" or selected_option == "3":
    goodbye()
  while selected_option not in available_options:
    clear()
    show_logo(filenames)
    selected_option = input("Please choose one of the following options:\n"
                    "1. Human vs Human\n"
                    "2. AI vs Human\n"
                    "3. Exit game\n" + 
                    colored.red("\tError: wrong input! "))
    if selected_option.lower() == "quit" or selected_option == "3":
      goodbye()
  return int(selected_option)

def get_board_size():
  available_options = ["5", "6", "7", "8", "9", "10"]
  selected_option = input("Please enter board size: (5-10)\n")
  while selected_option not in available_options:
    clear()
    selected_option = input("Please enter board size: (5-10)\n" + 
                    colored.red("\tError: wrong board size! "))
  if selected_option.lower() == "quit":
    goodbye()
  return int(selected_option)

def show_waiting_screen(player_one, player_two):
  print(colored.yellow(f"{player_one} placement has ended. Now it\'s turn for {player_two}\n"
                      "Please acknowledge. "))
  ask_for_any_key()
  clear()

def show_shooting_phase_message():
  input(colored.red("\t\tTime for shooting phase!\n Please press Enter to continue. "))
  clear()

def show_winning_message(player):
  input(f"{player} has won. ")

def check_play_again():
  decision = input("Would you like to play again? ")
  return decision