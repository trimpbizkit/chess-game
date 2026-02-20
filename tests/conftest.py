import pytest

from src.gamestate import GameState


@pytest.fixture
def initial_gamestate():
    return GameState()
