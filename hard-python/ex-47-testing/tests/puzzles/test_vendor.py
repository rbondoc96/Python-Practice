import pytest
from typing import Callable

from ex47.puzzles.vendor import PuzzleVendor


@pytest.fixture(scope="module")
def vendor() -> PuzzleVendor:
    return PuzzleVendor().load()


def test_vendor_load(vendor: PuzzleVendor):
    assert vendor.get_all_puzzles != {}


def test_get_puzzle_by_difficulty(vendor: PuzzleVendor):
    easy = vendor.get_puzzle("easy")
    normal = vendor.get_puzzle("normal")
    hard = vendor.get_puzzle("hard")   

    assert easy and normal and hard


def test_get_puzzle_with_invalid_difficulty(vendor):
    puzzle = vendor.get_puzzle("medium")
    assert puzzle is not None


def test_get_all_puzzles(vendor):
    assert vendor.get_all_puzzles() is not {}           


def test_play_puzzle(vendor):
    easy = vendor.get_puzzle("easy")
    normal = vendor.get_puzzle("normal")
    hard = vendor.get_puzzle("hard")

    assert easy.play()
    assert normal.play()
    assert hard.play()