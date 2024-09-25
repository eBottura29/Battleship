from shared import *


def evaluate_hit(target_board, index):
    if (
        target_board[index] == squares.destroyer
        or target_board[index] == squares.submarine
        or target_board[index] == squares.cruiser
        or target_board[index] == squares.battleship
        or target_board[index] == squares.carrier
    ):
        return True
    return False


class Battleship:
    def __init__(self):
        self.board_1 = [squares.sea for _ in range(100)]  # 100 comes from 10x10 (standard board size)
        self.board_2 = [squares.sea for _ in range(100)]

        self.player1_guess_board = [csquares.not_shot for _ in range(100)]
        self.player2_guess_board = [csquares.not_shot for _ in range(100)]

        self.pieces_left = 5

        self.p1_last_move = None
        self.p2_last_move = None

        self.game_over = False

    def choose_ships(self, player1_choice, player2_choice):
        self.board_1 = player1_choice(self.board_1)
        self.board_2 = player2_choice(self.board_2)

    def play(self, player1, player2, symbols):
        self.turn = True  # A boolean because it is easier to work with. True is player1 and False is player2

        while not self.game_over:
            print(f"{symbols[not self.turn]}'s turn...")
            if self.turn:
                choice = player1(self.player1_guess_board, self.pieces_left, self.p1_last_move)  # Lets the player choose an index

                if evaluate_hit(self.board_2, choice):
                    self.player1_guess_board[choice] = csquares.hit  # If hit, set guess board to hit
                else:
                    self.player1_guess_board[choice] = csquares.miss  # If not hit, set guess board to miss

                self.p1_last_move = choice
            elif not self.turn:
                choice = player2(self.player2_guess_board, self.pieces_left, self.p2_last_move)  # Lets the player choose an index

                if evaluate_hit(self.board_1, choice):
                    self.player2_guess_board[choice] = csquares.hit  # If hit, set guess board to hit
                else:
                    self.player2_guess_board[choice] = csquares.miss  # If not hit, set guess board to miss

                self.p2_last_move = choice

            self.turn = not self.turn
