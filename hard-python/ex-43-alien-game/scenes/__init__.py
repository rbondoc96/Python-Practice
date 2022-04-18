#!/usr/bin/env python3

from sys import exit
from typing import List

class Scene:

    def enter(self):
        print("This scene is not yet configured")
        print("Subclass it and implement enter()")
        exit(1)