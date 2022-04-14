try:
    import simplejson as json
except ImportError:
    import json

from os import path
from random import sample
from typing import TypeVar, Dict, List, Any

from settings import ROOT_DIR
from ex47.puzzles import Puzzle


Self = TypeVar("Self", bound="PuzzleVendor")

class PuzzleVendor:

    def load(self) -> Self:
        """Load puzzles from a JSON file located in the docs/ directory"""

        filename = path.join(ROOT_DIR, "docs", "puzzles.json")
        
        with open(filename, "r") as file:
            self._puzzles: Dict[str, List[Dict[str, str]]] = json.load(file)
        return self


    def get_puzzle(self, difficulty: str="normal"):
        """Get a puzzle of a given difficulty and return as a Puzzle object"""

        difficulty = difficulty.lower()
        p_list = self._puzzles.get(difficulty, None)
        
        if p_list:
            p = sample(p_list, 1)[0]
            return Puzzle(
                p.get("question", ""),
                p.get("answer", ""),
                difficulty
            )
        default = sample(list(self._puzzles.keys()), 1)[0]
        return self._puzzles.get(default)


    def get_all_puzzles(self):
        """Returns a dictionary of all puzzles."""

        return self._puzzles