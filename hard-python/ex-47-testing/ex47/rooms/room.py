from time import sleep
from textwrap import dedent

from typing import Dict

class Room:

    def __init__(self, name: str, description: str, prev: "Room"=None):
        self.name = name
        self.description = description
        self.paths: Dict[str, "Room"] = {}
        if prev:
            self.paths["back"] = prev


    def print_room(self):
        print(f" {self.name} ".center(30, "="))
        print(f"[{self.name}]: ", end="")
        print(dedent(self.description))
        sleep(1)

    
    def play(self) -> None:
        """If the Room is solvable, returns True if the Room is solved,
        False otherwise. If the Room is not solvable, always returns True
        """
        self.print_room()
        return True


    def choose_path(self) -> "Room":
        print("\nThe following paths appear before you.")
        print(self.name)
        print(self.paths)
        paths = self.paths.keys()
        for path in paths:
            print(path)

        ans = input("Which direction will you go? > ")
        if ans in paths:
            return self.go(ans)
        else:
            print("That path does not exist.")
            return self.choose_path()


    def go(self, direction: str) -> "Room":
        return self.paths.get(direction, None)


    def add_paths(self, paths: Dict[str, "Room"]) -> None:
        self.paths.update(paths)


    def remove_path(self, path: str) -> bool:
        """Returns True if the path is successfully removed."""
        try:
            self.paths.pop(path)
            return True
        except KeyError:
            return False