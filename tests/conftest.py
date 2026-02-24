import pytest

from src.gamestate import (
    GameState,
    Player
)
from src.pieces import (
    Pawn
)

@pytest.fixture
def initial_gamestate():
    return GameState()

@pytest.fixture
def initial_white_d_pawn_valid_moves():
    gamestate = GameState()
    d_pawn = Pawn("d2", Player.WHITE)
    possible_moves_trie = d_pawn.calculate_possible_moves(gamestate)
    return possible_moves_trie