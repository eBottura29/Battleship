from shared import *


def player_ship_choice(board):
    new_board = board

    destroyer = input(f"Enter index for destroyer (size = {squares.destroyer_size}): ")
    destroyer_rotation = input("Enter rotation index for destroyer: ")

    submarine = input(f"Enter index for submarine (size = {squares.submarine_size}): ")
    submarine_rotation = input("Enter rotation index for submarine: ")

    cruiser = input(f"Enter index for cruiser (size = {squares.cruiser_size}): ")
    cruiser_rotation = input("Enter rotation index for cruiser: ")

    battleship = input(f"Enter index for battleship (size = {squares.battleship_size}): ")
    battleship_rotation = input("Enter rotation index for battleship: ")

    carrier = input(f"Enter index for carrier (size = {squares.carrier_size}): ")
    carrier_rotation = input("Enter rotation index for carrier: ")

    return new_board


def ai_ship_choice(board):
    return board


def player_move(board, pieces_left, last_move):
    return int(input("Player's Move: "))


def ai_v1(board, pieces_left, last_move):
    return 0
