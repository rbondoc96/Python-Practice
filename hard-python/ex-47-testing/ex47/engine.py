from random import sample

from ex47.rooms import Room
from ex47.rooms.empty import EmptyRoom
from ex47.rooms.deadend import DeadEndRoom
from ex47.rooms.puzzle import PuzzleRoom
from ex47.rooms.death import DeathRoom
from ex47.rooms.final import FinalRoom

from ex47.runner import GameRunner

from typing import Dict, List, Callable


class Engine:

    directions: List[str] = [
        "up",
        "down",
        "left",
        "forward",
        "right",
    ]    

    possible_rooms: Dict[str, Callable] = {
        "empty": EmptyRoom,
        "puzzle": PuzzleRoom,
        "deadend": DeadEndRoom,
        "death": DeathRoom,
        "final": FinalRoom,
    }    


    def __init__(self, runner: GameRunner):
        self.runner = runner


    def generate_paths_for(self, _room: Room) -> None:
        if len(_room.paths) >= 4 or _room.name == "DeadEndRoom":
            return

        generate_count = 4 - len(_room.paths)
        
        rooms = sample(list(Engine.possible_rooms.keys()), generate_count)
        directions = sample(Engine.directions, generate_count)

        paths = {}
        for i in range(generate_count):
            constructor = Engine.possible_rooms.get(rooms[i])
            if constructor == DeadEndRoom:
                paths[directions[i]] = constructor(_room)
            else:
                paths[directions[i]] = constructor()

        _room.add_paths(paths)


    def start(self):
        current = self.runner.get_first_room()
        while current.name != "FinalRoom" and current.name != "DeathRoom":
            if current.play():
                self.generate_paths_for(current)
                current = current.choose_path()

        current.play()