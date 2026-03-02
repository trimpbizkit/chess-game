from enum import Enum

from board import Board
from notation import board_position_to_matrix_indices

class Player(Enum):
    WHITE = "white"
    BLACK = "black"

class GameState():
    
    def __init__(self):
        self.turn = Player.WHITE
        self.board = Board()

    def set_puzzle_state(self, turn, matrix):
        # todo; should this determine board matrix from the chess algebraic notation?
        pass

    def get_piece_at_board_position(self, board_position):
        i, j = board_position_to_matrix_indices(board_position)
        return self.board.get_piece_at_coords(i, j)
    
    def is_space_occupied(self, board_position):
        return self.get_piece_at_board_position(board_position) != "."
    
    def whose_piece_is_at_board_position(self, board_position):
        if not self.is_space_occupied(board_position):
            raise ValueError(f"there is no piece at {board_position}")
        piece = self.get_piece_at_board_position(board_position)
        return Player.WHITE if piece.isupper() else Player.BLACK
    
    def change_turn(self):
        if self.turn == Player.WHITE:
            self.turn = Player.BLACK
            return
        self.turn = Player.WHITE
        
    def print_state(self):
        print(f"It is {self.turn.value}'s turn")
        print(self.board)
