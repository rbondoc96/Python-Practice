from ex47.rooms import Room

class EmptyRoom(Room):

    def __init__(self):
        name = "EmptyRoom"
        description = """
        You walk in the room and...there's nothing here! 
        You can clearly see the path ahead.
        """
        super().__init__(name, description)