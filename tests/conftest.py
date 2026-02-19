import pytest
from gamestate import GameState


@pytest.fixture
def initial_gamestate():
    return GameState()
