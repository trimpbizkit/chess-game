def validate_file_first_board_position(board_position):
    if len(board_position) != 2:
        raise Exception("file first board position: incorrect length")
    file = board_position[0]
    rank = board_position[1]
    if not file.isalpha() or not rank.isdigit():
        raise Exception("file first board position: incorrect format")
    if ord(file) < 97 or ord(file) > 104:
        raise Exception("file first board position: file is invalid")
    if int(rank) < 1 or int(rank) > 8:
        raise Exception("file first board position: rank is invalid")
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
