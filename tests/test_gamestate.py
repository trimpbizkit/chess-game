def test_get_piece_at_board_position_white(initial_gamestate):
    piece = initial_gamestate.get_piece_at_board_position("a1")
    assert "R" == piece
    piece = initial_gamestate.get_piece_at_board_position("b1")
    assert "N" == piece
    piece = initial_gamestate.get_piece_at_board_position("c1")
    assert "B" == piece
    piece = initial_gamestate.get_piece_at_board_position("d1")
    assert "Q" == piece
    piece = initial_gamestate.get_piece_at_board_position("e1")
    assert "K" == piece
    piece = initial_gamestate.get_piece_at_board_position("f1")
    assert "B" == piece
    piece = initial_gamestate.get_piece_at_board_position("g1")
    assert "N" == piece
    piece = initial_gamestate.get_piece_at_board_position("h1")
    assert "R" == piece

def test_get_piece_at_board_position_black(initial_gamestate):
    piece = initial_gamestate.get_piece_at_board_position("a8")
    assert "r" == piece
    piece = initial_gamestate.get_piece_at_board_position("b8")
    assert "n" == piece
    piece = initial_gamestate.get_piece_at_board_position("c8")
    assert "b" == piece
    piece = initial_gamestate.get_piece_at_board_position("d8")
    assert "q" == piece
    piece = initial_gamestate.get_piece_at_board_position("e8")
    assert "k" == piece
    piece = initial_gamestate.get_piece_at_board_position("f8")
    assert "b" == piece
    piece = initial_gamestate.get_piece_at_board_position("g8")
    assert "n" == piece
    piece = initial_gamestate.get_piece_at_board_position("h8")
    assert "r" == piece

def test_get_piece_at_board_position_empty_center(initial_gamestate):
    piece = initial_gamestate.get_piece_at_board_position("d5")
    assert "." == piece
    piece = initial_gamestate.get_piece_at_board_position("d4")
    assert "." == piece
    piece = initial_gamestate.get_piece_at_board_position("e5")
    assert "." == piece
    piece = initial_gamestate.get_piece_at_board_position("e4")
    assert "." == piece
