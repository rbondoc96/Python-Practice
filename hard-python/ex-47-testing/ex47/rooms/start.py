from ex47.rooms import Room

class StartRoom(Room):
    
    def __init__(self):
        name = "StartRoom"
        description = f"""
        Your feet touch the ground as you finish your
        descent. The fabled Lance of Longinous is rumored to be hidden
        somewhere deep in these caverns. You find an ominous, blue-lit corridor
        that splits into 3 paths to chose from.
        """
        super().__init__(name, description)