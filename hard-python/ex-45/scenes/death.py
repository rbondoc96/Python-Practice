from . import Scene

from sys import exit
from random import sample
from typing import List


class Death(Scene):

    GAME_OVER_LINES: List[str] = [
        "Better luck next time!",
        "Perhaps a bit more effort would help, no?"
    ]

    def play(self):
        Scene.print_text(
            sample(Death.GAME_OVER_LINES, 1)[0]
        )
        exit(1)