from random import sample

from ex47.rooms import Room
from ex47.puzzles import Puzzle
from ex47.puzzles.vendor import PuzzleVendor

from typing import List


class PuzzleRoom(Room):

    vendor: PuzzleVendor = PuzzleVendor().load()

    quips: List[str] = [
        """
        As you walk in the room, you see a Hebrew inscription on the wall.
        You bring out your trusty language handbook and you find that it
        speaks of a puzzle that you must solve before it opens the path
        to the next room.
        """,
        """
        You see a path across a bridge as you enter the room. As you approach
        the bridge, it suddenly collapses and a stone tablet erects from the
        ground. You approach the tablet and see characters etched into the
        stone. It translates to "In order to pass, you must solve my puzzle."
        """,
        """
        As you enter the room, you see some paths at the end of the room. You
        approach the paths and all of a sudden, a portion of the ceiling drops
        down and blocks your path. On the stone, there is an inscription that
        reads "To open the path forward, you must solve my puzzle."
        """,
    ]


    def __init__(self, difficulty: str=None):
        name = "PuzzleRoom"
        description = sample(PuzzleRoom.quips, 1)[0]
        super().__init__(name, description)

        if not difficulty:
            key, diff = sample(list(Puzzle.DIFF.items()), 1)[0]
            self._difficulty = diff
        else:
            self._difficulty = difficulty

        self.set_puzzle()

    
    def play(self) -> str:
        self.print_room()

        if self.puzzle.play():
            print("That's correct! You may pass.")
            return True
        return False


    def set_puzzle(self) -> None:
        self.puzzle = PuzzleRoom.vendor.get_puzzle(self._difficulty)

    
    def is_solved(self) -> bool:
        return self.puzzle.is_solved()