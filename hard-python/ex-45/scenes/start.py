from . import Scene

from random import sample
from typing import List


class Start(Scene):

    def play(self):
        Scene.print_text("""
        You rappel down a hole you found deep in some catacombs in Jerusalem.
        You're searching for the fabled Lance of Longinus, an ancient Christian
        artifact that was said to have stabbed Jesus during his crucifixion.
        
        You reach the bottom and find a stone gate 
        """)
        exit(1)