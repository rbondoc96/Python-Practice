#!/usr/bin/env python3

from typing import Dict

from scenes import Scene
from scenes.death import Death
from scenes.corridor import CentralCorridor
from scenes.armory import LaserWeaponArmory
from scenes.bridge import TheBridge
from scenes.escape import EscapePod
from scenes.finish import Finished

class Map:

    scenes: Dict[str, Scene] = {
        "central_corridor": CentralCorridor(),
        "laser_weapon_armory": LaserWeaponArmory(),
        "the_bridge": TheBridge(),
        "escape_pod": EscapePod(),
        "death": Death(),
        "finished": Finished(),
    }

    def __init__(self, start_scene: str):
        self.start_scene = start_scene

    def get_scene(self, scene_name: str) -> Scene:
        return Map.scenes.get(scene_name)

    def next_scene(self, next_scene_name: str) -> Scene:
        return self.get_scene(next_scene_name)

    def opening_scene(self) -> Scene:
        return self.get_scene(self.start_scene)
