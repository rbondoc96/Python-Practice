import pytest

from ex47.rooms import Room
from ex47.rooms.death import DeathRoom

@pytest.fixture
def path():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north.")
    south = Room("South", "Test room in the south.")

    center.add_paths({
        "north": north,
        "south": south,
    })
    
    return center


def test_room() -> None:
    gold = Room(
        "GoldRoom",
        """This room has gold in it you can grab. There's a door
        to the north.""")

    assert gold.name == "GoldRoom"
    assert gold.paths == {}


def test_room_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Tset room in the north.")
    south = Room("South", "Test room in the south.")

    center.add_paths({
        "north": north,
        "south": south,
    })

    assert center.go("north") == north
    assert center.go("south") == south


def test_go_back_to_previous():
    start = Room("Start", "This is the start room")
    forward = Room("Forward", "This is the forward room", start)
    start.add_paths({
        "forward": forward
    })

    assert start.play()
    current = start.choose_path()

    assert current == forward
    assert current.play()
    current = current.choose_path()

    assert start == current


def test_removal_of_existent_path(path):
    assert path.remove_path("south") == True


def test_removal_of_nonexistent_path(path):
    assert path.remove_path("east") == False


def test_map():
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees", "There are trees here, you can go East.")
    down = Room("Dungeon", "It's dark down here, you can go Up.")

    start.add_paths({
        "west": west,
        "down": down,
    })
    west.add_paths({
        "east": start,
    })
    down.add_paths({
        "up": start
    })

    assert start.go("west") == west
    assert start.go("west").go("east") == start
    assert start.go("down").go("up") == start
