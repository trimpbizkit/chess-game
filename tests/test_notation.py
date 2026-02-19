from notation import board_position_to_matrix_indices

def test_board_position_to_matrix_indices_basic():
    i, j = board_position_to_matrix_indices("h8")
    assert (0, 7) == (i, j)
    i, j = board_position_to_matrix_indices("g7")
    assert (1, 6) == (i, j)
    i, j = board_position_to_matrix_indices("f6")
    assert (2, 5) == (i, j)
    i, j = board_position_to_matrix_indices("e5")
    assert (3, 4) == (i, j)
    i, j = board_position_to_matrix_indices("d4")
    assert (4, 3) == (i, j)
    i, j = board_position_to_matrix_indices("c3")
    assert (5, 2) == (i, j)
    i, j = board_position_to_matrix_indices("b2")
    assert (6, 1) == (i, j)
    i, j = board_position_to_matrix_indices("a1")
    assert (7, 0) == (i, j)
    