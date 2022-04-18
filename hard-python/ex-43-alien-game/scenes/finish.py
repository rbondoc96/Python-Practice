#!/usr/bin/env python3

from sys import exit
from random import randint
# Strips leading white-space from beginning of lines in a multi-line string
from textwrap import dedent 
from typing import List

from . import Scene


class Finished(Scene):
    
    def enter(self):
        print("You won! Good job.")
        return "finished"