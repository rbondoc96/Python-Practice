import pytest

from ex47.puzzles import Puzzle

def test_puzzle_creation():
    question = "What is the worst case time complexity of Quicksort?"
    answer = "O(n**2)"
    puzzle = Puzzle(question, answer)

    assert puzzle.question == question
    assert puzzle.answer == answer
    assert puzzle.difficulty == Puzzle.DIFF.get("NORMAL")


def test_puzzle_correctly_solve():
    question = "What is the worst case time complexity of Quicksort?"
    answer = "O(n**2)"
    puzzle = Puzzle(question, answer)

    assert puzzle.play()
    assert puzzle.is_solved()


def test_puzzle_incorrectly_solve():
    question = "What is the worst case time complexity of Quicksort?"
    answer = "O(n**2)"
    puzzle = Puzzle(question, answer)

    assert not puzzle.play()
    assert not puzzle.is_solved()


def test_puzzle_resolve():
    question = "What is the worst case time complexity of Quicksort?"
    answer = "O(n**2)"
    puzzle = Puzzle(question, answer)
    puzzle._solved = True

    assert puzzle.play()