import pytest

from ex47.engine import Engine
from ex47.runner import GameRunner


@pytest.fixture(scope="module")
def control():
    runner = GameRunner()
    return {
        "runner": runner,
        "engine": Engine(runner),
    }


def test_path_generation(control):
    runner = control["runner"]
    engine = control["engine"]

    start = runner.get_first_room()
    engine.generate_paths_for(start)

    assert len(start.paths) > 0


def test_game(control):
    engine = control["engine"]
    try:
        engine.start()
    except Exception as e:
        assert False, "There was a failure"