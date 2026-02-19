def test_get_piece_at_coords_white(initial_gamestate):
    piece = initial_gamestate.board.get_piece_at_coords(7, 0) # a1
    assert "R" == piece
    piece = initial_gamestate.board.get_piece_at_coords(7, 1) # b1
    assert "N" == piece
    piece = initial_gamestate.board.get_piece_at_coords(7, 2) # c1
    assert "B" == piece
    piece = initial_gamestate.board.get_piece_at_coords(7, 3) # d1
    assert "Q" == piece
    piece = initial_gamestate.board.get_piece_at_coords(7, 4) # e1
    assert "K" == piece
    piece = initial_gamestate.board.get_piece_at_coords(7, 5) # f1
    assert "B" == piece
    piece = initial_gamestate.board.get_piece_at_coords(7, 6) # g1
    assert "N" == piece
    piece = initial_gamestate.board.get_piece_at_coords(7, 7) # h1
    assert "R" == piece

def test_get_piece_at_coords_black(initial_gamestate):
    piece = initial_gamestate.board.get_piece_at_coords(0, 0) # a8
    assert "r" == piece
    piece = initial_gamestate.board.get_piece_at_coords(0, 1) # b8
    assert "n" == piece
    piece = initial_gamestate.board.get_piece_at_coords(0, 2) # c8
    assert "b" == piece
    piece = initial_gamestate.board.get_piece_at_coords(0, 3) # d8
    assert "q" == piece
    piece = initial_gamestate.board.get_piece_at_coords(0, 4) # e8
    assert "k" == piece
    piece = initial_gamestate.board.get_piece_at_coords(0, 5) # f8
    assert "b" == piece
    piece = initial_gamestate.board.get_piece_at_coords(0, 6) # g8
    assert "n" == piece
    piece = initial_gamestate.board.get_piece_at_coords(0, 7) # h8
    assert "r" == piece

def test_get_piece_at_coords_empty_center(initial_gamestate):
    piece = initial_gamestate.board.get_piece_at_coords(3, 3) #d5
    assert "." == piece
    piece = initial_gamestate.board.get_piece_at_coords(4, 3) #d4
    assert "." == piece
    piece = initial_gamestate.board.get_piece_at_coords(3, 4) #e5
    assert "." == piece
    piece = initial_gamestate.board.get_piece_at_coords(4, 4) #e4
    assert "." == piece
