#!/usr/bin/env python3

from sys import exit
from random import randint
from typing import List

from . import Scene

class Death(Scene):

    quips: List[str] = [
        "You died. You kinda suck at this.",
        "Your mom would be so proud...if she were smarter.",
        "Such a loser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes.",
    ]

    def enter(self):
        # randint() is inclusive at start and end 
        quip_idx = randint(0, len(Death.quips)-1)
        print(Death.quips[quip_idx])
        exit(1)