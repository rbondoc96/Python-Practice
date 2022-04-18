#!/usr/bin/env python3

from typing import List

class Song:

    def __init__(self, lyrics: List):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

def main():
    happy_bday = Song([
        "Happy birthday to you",
        "I don't want to get sued",
        "So I'll stop right there"
    ])

    bull_on_parade = Song([
        "They rally around tha family",
        "With pockets full of shells"
    ])

    happy_bday.sing_me_a_song()
    bull_on_parade.sing_me_a_song()

    print(getattr(Song,"__annotations__", None))

if __name__ == "__main__":
    main()