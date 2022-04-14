from sys import exit

from ex47.rooms import Room

class DeathRoom(Room):

    def __init__(self):
        name = "DeathRoom"
        description = "Oh no, you died! Better luck next time."
        super().__init__(name, description)