#!/usr/bin/env python3

from gamemap import Map
from engine import Engine

def main():
    game_map = Map("central_corridor")
    game = Engine(game_map)
    game.play()

if __name__ == "__main__":
    main() 