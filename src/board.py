UNICODE_PIECES = {
    "k": "♔", "q": "♕", "r": "♖", "b": "♗", "n": "♘", "p": "♙",
    "K": "♚", "Q": "♛", "R": "♜", "B": "♝", "N": "♞", "P": "♟",
    ".": " "
}

ANSI_WHITE = "\033[47m"
ANSI_BLACK = "\033[40m"
ANSI_RESET = "\033[0m"

class Board():
    
    def __init__(self):
        '''A chessboard is an 8x8 grid of alternating black and white squares.'''
        self.set_starting_matrix()

    def set_starting_matrix(self):
        '''
        Uppercase will be white player's pieces.
        Lowercase will be black player's pieces.
        Period will be an empty space.
        a1 is a black square.
        '''
        self.matrix = [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
        ]

    def set_matrix(self, matrix):
        self.matrix = matrix
    
    def get_piece_at_coords(self, rank_coord: int, file_coord:int) -> str:
        '''
        Coordinates are range(0, 7). 
        matrix[0][0] == "a8"
        matrix[0][1] == "b8"
        matrix[1][0] == "a7"

        :param rank_coord: first dimension of board matrix array, representing rank
        :param file_coord: second dimension of board matrix array, representing file
        '''
        return self.matrix[rank_coord][file_coord]

    def __str__(self):
        result = "   a  b  c  d  e  f  g  h\n"
        rank = 8
        for row in self.matrix:
            current = f"{rank}"
            file = "a"
            for cell in row:
                file_value = ord(file) - ord('a')
                # Alternate tile colors
                if (rank + file_value) % 2 == 0:
                    bg = ANSI_WHITE  # white
                else:
                    bg = ANSI_BLACK  # black
                current += f"{bg} {UNICODE_PIECES[cell]} {ANSI_RESET}"
                file = chr(ord(file) + 1)
            current += f"{rank}\n"
            result += current
            rank -= 1
        result += "   a  b  c  d  e  f  g  h\n"
        return result
