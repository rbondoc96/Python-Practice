#!/usr/bin/env python3

from sys import exit
from random import randint
# Strips leading white-space from beginning of lines in a multi-line string
from textwrap import dedent 
from typing import List

from . import Scene


class EscapePod(Scene):
    
    def enter(self):
        print(dedent("""
        You rush through the ship desparately trying to make it to the escape
        pod before the whole ship explodes. It seems like hardly any Gothons
        are on the ship, so your run is clear of interference. You get to the
        chamber with the escape pods, adn now need to pick one to take. Some
        of them could be damaged, but you don't have time to look. There
        are 5 pods, which one do you take?
        """))

        good_pod = randint(1, 5)
        print("Good pod", good_pod)
        guess = input("[pod #] > ")

        if int(guess) == good_pod:
            print(dedent(f"""
            You jump into pod {guess} and hit the eject button. The pod easily
            slides out into space, heading to the planet below. As it flies to
            the planet, you look and see your ship implode then explode like a
            bright star, takingg out the Gothon ship at the same time. You won!
            """))

            return "finished"

        else:
            print(dedent(f"""
            You jump into pod {guess} and hit the eject button. The pod escapes
            out into the void of space, then implodes as the hull ruptrues, 
            crushing your body into jam jelly.
            """))

            return "death"