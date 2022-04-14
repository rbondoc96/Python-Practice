import pytest

from ex47.rooms.puzzle import PuzzleRoom


def test_puzzleroom() -> None:
    gold = PuzzleRoom("hard")

    assert gold.paths == {}
    assert gold.puzzle is not None
    assert gold._difficulty == "hard"


def test_puzzleroom_with_invalid_difficulty() -> None:
    gold = PuzzleRoom("veryhard")

    assert gold.paths == {}
    assert gold.puzzle is not None