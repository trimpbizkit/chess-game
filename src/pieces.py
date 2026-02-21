
class Piece:

    def __init__(self):
        pass

    def list_valid_moves(self):
        raise NotImplementedError(f"must implement *list_valid_moves*")


class Pawn(Piece):
    pass

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
