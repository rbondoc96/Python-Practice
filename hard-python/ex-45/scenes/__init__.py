from sys import exit
from textwrap import dedent

from typing import List

class Scene:

    @staticmethod
    def print_text(string):
        print(dedent(string))

    def __init__(self, options: List[str]=[]):
        self.options: List[str] = options

    def play(self):
        pass