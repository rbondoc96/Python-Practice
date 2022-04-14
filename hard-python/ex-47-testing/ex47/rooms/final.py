from ex47.rooms import Room

class FinalRoom(Room):
    
    def __init__(self):
        name = "FinalRoom"
        description = """
        You walk into a room littered with skeletons. You investigate the
        skeletons and find one of them holding a shiny, silver rod. You
        grab it and realize that it's the Lance of Longinous!
        """
        super().__init__(name, description)

    def play(self):
        self.print_room()
        print("Congratulations! You won!")
        return True