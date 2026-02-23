
class AlgebraicNotation():

    def __init__(self, move):
        # piece
        # capture
        # disambiguation
        # promotion
        # castling
        # check
        pass


def validate_file_first_board_position(board_position):
    if len(board_position) != 2:
        raise ValueError("file first board position: incorrect length")
    file = board_position[0]
    rank = board_position[1]
    if not file.isalpha() or not rank.isdigit():
        raise ValueError("file first board position: incorrect format")
    if ord(file) < 97 or ord(file) > 104:
        raise ValueError("file first board position: file is invalid")
    if int(rank) < 1 or int(rank) > 8:
        raise ValueError("file first board position: rank is invalid")
    return file, rank
    
def board_position_to_matrix_indices(board_position):
    '''
    Convert the board position in file-first notation to the indices of the matrix
    
    :param board_position: Description
    '''
    file, rank = validate_file_first_board_position(board_position)
    i = 8 - int(rank)
    j = ord(file) - ord('a')
    return i, j

def parse_algebraic_notation(move):
    '''
    Standard algebraic notation indicates piece uppercase letter and destination square.
    For pawn moves, only the destination square is given.
    When a piece makes a capture, and x is inserted immediately before the destination.
    Pawn captures indicate departing file (en passant also does this).
    When a pawn promotes, the piece promoted to is indicated at the end.
    Castling is indicated by the special notations O-O (kingside) and O-O-O (queenside)
    A move that places the opponent's king in check has the symbol + appended
    Checkmate is represented by the symbol # appended
    Draw (and therefore stalemate) is represented by the symbol = appended

    Disambiguation follows piece when identical pieces can move to the same square prioritzes:
    1. the file of departure (if they differ)
    2. the rank of departure (if the files are the same but the ranks differ)
    3. if neither file nor rank alone is sufficient, both are specified
    '''
    named_pieces = ["K", "Q", "R", "B", "N"]
    pass
