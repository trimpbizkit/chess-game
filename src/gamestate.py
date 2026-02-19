from enum import Enum
from board import Board
from notation import board_position_to_matrix_indices

class Turn(Enum):
    WHITE = "white"
    BLACK = "black"

class GameState():
    
    def __init__(self):
        self.turn = Turn.WHITE
        self.board = Board()

    def print_state(self):
        print(f"It is {self.turn.value}'s turn")
        print(self.board.matrix_to_string())

    def get_piece_at_board_position(self, board_position):
        i, j = board_position_to_matrix_indices(board_position)
        return self.board.get_piece_at_coords(i, j)
