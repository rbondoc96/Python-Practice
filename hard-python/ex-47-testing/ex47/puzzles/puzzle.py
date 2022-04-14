from typing import Dict, Optional

class Puzzle:

    DIFF: Dict[str, str] = {
        "EASY": "easy",
        "NORMAL": "normal",
        "HARD": "hard",
    }    

    def __init__(self, q, a, diff: Optional[str]=None):
        self.question = q
        self.answer = a
        self.difficulty = diff or Puzzle.DIFF["NORMAL"]
        self._solved = False

    
    def is_solved(self) -> bool:
        return self._solved


    def play(self) -> bool:
        if self._solved:
            print("You've already solved this puzzle.")
            return True

        print("Question:", self.question)
        ans = input("> ")

        if ans == str(self.answer):
            self._solved = True
            return True
        return False