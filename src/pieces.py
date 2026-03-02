from enum import Enum

from data_structures import Trie
from gamestate import (
    GameState, 
    Player
)

class PieceType(Enum):
    PAWN = "pawn"
    ROOK = "rook"
    KNIGHT = "knight"
    BISHOP = "bishop"
    QUEEN = "queen"
    KING = "king"


class Piece:

    def __init__(self, position: str, player: Player, piece_type: PieceType):
        self.position = position
        self.player = player
        self.piece_type = PieceType
        self.has_moved = False

    def get_current_file(self):
        return self.position[0]
    
    def get_current_rank(self):
        return self.position[1]

    def calculate_forward_rank_position(self, num_ranks: int, from_position: str):
        rank_modifier = 1
        if self.player == Player.BLACK:
            rank_modifier = -1

        new_rank = int(from_position[1]) + (num_ranks * rank_modifier)

        if new_rank < 1 or new_rank > 8:
            raise ValueError(f"calculated forward position: {self.player.value} {self.piece_type.value} moving {num_ranks} ranks is invalid")

        return f"{from_position[0]}{new_rank}"
    
    def calculate_forward_file_position(self, num_files: int, to_higher: bool, from_position: str):
        file_modifier = 1
        if to_higher is False:
            file_modifier = -1

        new_file = ord(from_position[0]) + (num_files * file_modifier)

        if new_file < 97 or new_file > 104:
            direction = "higher" if to_higher else "lower"
            raise ValueError(f"calculated forward position: {self.player.value} {self.piece_type.value} moving {num_files} files {direction} is invalid")

        return f"{chr(new_file)}{from_position[1]}"

    def list_possible_moves(self):
        raise NotImplementedError(f"must implement *list_possible_moves*")


class Pawn(Piece):
    
    def __init__(self, position, player):
        super().__init__(position, player, PieceType.PAWN)

    def list_possible_moves(self, gamestate: GameState):
        possible_moves_trie = self.calculate_possible_moves(gamestate)
        return possible_moves_trie.list_full_entries()
    
    def calculate_possible_moves(self, gamestate: GameState):
        possible_moves = Trie()

        # check move 1
        move_one_position = super().calculate_forward_rank_position(1, self.position)
        if not gamestate.is_space_occupied(move_one_position):
            possible_moves.insert(move_one_position)

        # check move 2
        if not self.has_moved:
            move_two_position = super().calculate_forward_rank_position(2, self.position)
            if not gamestate.is_space_occupied(move_two_position):
                possible_moves.insert(move_two_position)

        # check capture lower
        capture_lower_position = super().calculate_forward_file_position(1, False, move_one_position)
        if gamestate.is_space_occupied(capture_lower_position):
            if gamestate.whose_piece_is_at_board_position(capture_lower_position) != self.player:
                possible_moves.insert(capture_lower_position)

        # check capture higher
        capture_higher_position = super().calculate_forward_file_position(1, True, move_one_position)
        if gamestate.is_space_occupied(capture_higher_position):
            if gamestate.whose_piece_is_at_board_position(capture_higher_position) != self.player:
                possible_moves.insert(capture_higher_position)
        
        # check en passant capture
        # check puts self in check at every move

        return possible_moves

class King(Piece):
    '''
    During castling, the king is shifted two squares toward a rook of the same color on the same rank,
    and the rook is transferred to the square crossed by the king

    Castling is permitted provided all of the following conditions are met:

    Neither the king nor the rook has previously moved.
    There are no pieces between the king and the rook.
    The king is not currently in check.
    The king does not pass through or finish on a square that is attacked by an enemy piece.
    '''
    pass

class Bishop(Piece):
    pass

class Rook(Piece):
    pass

class Queen(Piece):
    pass

class Knight(Piece):
    pass
