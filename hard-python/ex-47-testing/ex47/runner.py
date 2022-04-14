from random import sample

from ex47.rooms import Room
from ex47.rooms.start import StartRoom
from ex47.rooms.empty import EmptyRoom
from ex47.rooms.deadend import DeadEndRoom
from ex47.rooms.puzzle import PuzzleRoom
from ex47.rooms.death import DeathRoom
from ex47.rooms.final import FinalRoom

from typing import Dict, List

class GameRunner:
    
    def __init__(self):
        self.start = StartRoom()
        self.final = FinalRoom()
        self.level = 1


    def get_first_room(self) -> Room:
        return self.start


    def get_last_room(self) -> Room:
        return self.final

    
    def increment_level(self) -> None:
        self.level += 1


    def decrement_level(self) -> None:
        self.level -= 1