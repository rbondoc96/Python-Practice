from ex47.engine import Engine
from ex47.runner import GameRunner

def main():
    runner = GameRunner()
    engine = Engine(runner)

    engine.start()


if __name__ == "__main__":
    main()