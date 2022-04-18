#!/usr/bin/env python3

# Strips leading white-space from beginning of lines in a multi-line string
from textwrap import dedent 

from . import Scene


class CentralCorridor(Scene):
    
    # Returns the next scene
    def enter(self) -> str:
        print(dedent("""
        The Gothons of Planet Percal #25 have invaded your ship and destroyed
        your entire crew. You are the last surviving member and your last is
        to get the neutron destruct bomb from the Weapons Armory, put it in
        the bridge, and blow up the ship after getting into an escape pod.

        You're running down the central corridor to the Weapons Armory when a
        Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown 
        costume flowing around his hate filled body. He's blocking the door to the Armory and about to pull a weapon to blast you.
        """))

        action = input("> ")

        if action == "shoot":
            print(dedent("""
            Quick on the draw, you yank out your blaster and fire it at the
            Gothon. His clown costume is flowing and moving around his
            body, which throws off your aim. Your laser hits his costume
            but misses him entirely. This completely ruins his brand new
            costume his mother bought him, which makes him fly into
            an insane rage and blast you repeatedly in the face until you
            are dead. Then he eats you.
            """))
        
            return "death"

        elif action == "dodge":
            print(dedent("""
            Like a world class boxer you dodge, weave, slip, and slide right as
            the Gothon's blaster cranks a laser past your head. In the middle
            of your artful dodge, your foot slips and you bang your head on the
            metal wall and pass out. You wake up shortly after, only to die
            as the Gothon stomps on your head and eats you.
            """))

            return "death"

        elif action == "tell a joke":
            print(dedent("""
            Lucky for you, they made you learn Gothon insults in the academy.
            You tell the one Gothon joke you know: Lbhe zbgure vf fb sng, jura
            fur fvgf nebhaq gur ubhfr, fur fvgf nebgur ubhfr. The Gothon stops,
            tries not to laugh, then busts out laughing and can't move. While
            he's laughing, you run up and shoot him square in the head putting
            him down, then jump through the Weapon Armory door.
            """))

            return "laser_weapon_armory"

        else:
            print("DOES NOT COMPUTE.")
            return "central_corridor"