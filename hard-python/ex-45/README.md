# Exercise 45: You Make a Game

## Requirements
1. Make a different game than Exercise 43.
2. Use more than 1 file and use `import` to use them.
3. Use *one class per room* and give the classes names that fit their purpose (like GoldRoom, KoiPondRoom)
4. Your runner will need to know about these rooms, so make a class that runs them and knows about them.
    - There are plenty of ways to do this, but consider having each room return what room is next or setting a variable of what room is next.


## Bullet Ideas
1. Tomb Raider-based game


### Idea #1: Find the Treasure and Escape!

The player has entered a tomb in the Middle East in search of the Lance of Longinus, a holy artifact that pierced Jesus during his crucifiction. 

The tomb is filled with dangerous traps and reanimated angelic entities that guard the Lance and prevent anyone from taking it.

The player must navigate the tomb, avoiding its many traps and guardians to find the Lance and escape alive. The player has a limited, set inventory that they can use to fight the guardians and take care of themselves.

START
|__ LEFT
    |__ EnemyRoom
        |__ DEATH
        |__ UP
            |__ DEATH
        |__ DOWN
            |__ PuzzleTrapRoom
                |__ DEATH
                |__ LEFT
                    |__ DEATH
                |__ RIGHT
                    |__ DEATH
                |__ DOWN
                    |__ EnemyRoom
                        |__ DEATH
                        |__ DOWN
                            |__ DEATH
                        |__ LEFT
                            |__ Sepulcher

|__ MIDDLE
    |__ PuzzleTrapRoom
        |__ DEATH
        |__ UP
            |__ DEATH
        |__ DOWN
            |__ EnemyRoom    
                |__ DEATH
                |__ FORWARD
                    |__ EnemyRoom
                        |__ DEATH
                        |__ LEFT
                            |__ DEATH
                        |__ RIGHT
                            |__ Sepulcher
|__ RIGHT
    |__ DEATH