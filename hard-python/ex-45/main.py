#!/usr/bin/env python3
from engine import Engine
from runner import SceneRunner

def main():
    runner = SceneRunner()
    engine = Engine(runner)
    engine.start()

if __name__ == "__main__":
    main()