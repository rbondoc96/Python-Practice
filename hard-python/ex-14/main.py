#!/usr/bin/env python3

from sys import argv

def main():
    script, user = argv
    prompt = "> "

    print(f"Hi {user}, I'm the {script} script.")
    print("I'd like to ask you a few questions.")
    print(f"Do you like me {user}?")
    likes_me = input(prompt)

    print(f"Where do you live, {user}?")
    lives = input(prompt)

    print("What kind of computer do you have?")
    comp = input(prompt)

    print(f"""Alright, so you said {likes_me} about liking me.
You live in {lives}. Not sure where that is.
And you have a {comp} computer. Nice.""")

if __name__ == "__main__":
    main()