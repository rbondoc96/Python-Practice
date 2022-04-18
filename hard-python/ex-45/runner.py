from scenes import Scene
from scenes.death import Death

from typing import Dict

class SceneRunner:

    SCENES: Dict[str, Scene] = {
        "start": None,
        "enemy_room": None,
        "puzzle_trap_room": None,
        "fork": None,
        "sepulcher": None,
        "final": None,
        "death": Death(),
    }

    def __init__(self):
        pass

    def get_scene(self, scene_name):
        return SceneRunner.SCENES.get(scene_name)

    def start_scene(self) -> Scene:
        return SceneRunner.SCENES.get("start")

    def final_scene(self) -> Scene:
        return SceneRunner.SCENES.get("final")