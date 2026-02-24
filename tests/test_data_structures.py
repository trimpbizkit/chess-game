def test_initial_white_d_pawn_moves(initial_white_d_pawn_valid_moves):
    valid_moves_list = initial_white_d_pawn_valid_moves.list_full_entries()
    assert len(valid_moves_list) == 2
    assert initial_white_d_pawn_valid_moves.has_entry("d3") == True
    assert initial_white_d_pawn_valid_moves.has_entry("d4") == True
