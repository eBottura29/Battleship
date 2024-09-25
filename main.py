from players import *
from game import *

if __name__ == "__main__":
    game = Battleship()
    game.choose_ships(player_ship_choice, ai_ship_choice)
    game.play(player_move, ai_v1, ["Player", "AI"])
