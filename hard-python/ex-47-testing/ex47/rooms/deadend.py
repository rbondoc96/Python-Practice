from ex47.rooms import Room

from typing import Callable

class DeadEndRoom(Room):
    
    def __init__(self, prev: Room):
        name = "DeadEndRoom"
        description = """
        There's nothing in this room. Let's turn back.
        """
        
        super().__init__(name, description, prev)