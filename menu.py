from clint.textui import colored


def show_logo(filenames):
  frames = []
  for name in filenames:
    with open(name, "r", encoding = "utf8") as f:
      frames.append(f.readlines())
    for frame in frames:
      print(colored.blue("".join(frame))) 
  print("\n")