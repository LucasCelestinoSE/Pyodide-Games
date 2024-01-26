import pyspiel
from js import document
game = pyspiel.load_game("tic_tac_toe")
state = game.new_initial_state()

while not state.is_terminal():
  print("Current player: ", state.current_player())
  print("Legal actions: ", state.legal_actions())
  action = int(input("Enter action: "))
  state.apply_action(action)
  print(state)
  print("Returns: ", state.returns())
