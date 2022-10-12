# Honeybee Game
### A game inspired by the classic Snake game created with Python (Pygame). 
The up, down, left, and right arrow keys are used to play.

Python 3.10.7  |  Pygame 2.1.2 

## Table of contents
* [Introduction](#introduction)
* [Snake (Bee) Class](#snake-class)
* [Snack (Honey) Class](#snack-class)
* [Game Class Setup](#game-class-setup)
* [Sources](#sources)

### Introduction
I decided to create a fun mini-game based on the classic Snake game, but with a slightly different themed concept in order to create something that differs from the original.  I wanted to practice my application of Python and teach myself how to use PyGame while still creating a project with a degree of complexity.  I focused my attention on object-oriented programming, practicing the utilization of classes and objects.  I created this application using PyCharm and exported it for accessebility.

I started with initializing my necessary variables.  SIZE is set to 40 because both sprites (bee and honey) are set to have dimensions of 40x40.  WIDTH and HEIGHT are set to 800 and 600, respectively, as they determine the size of the game window and the boundaries for where the player will lose the game when hitting the window walls.  The color white was also initialized as it was used multiple times to style all of the text encompassed in the game.  Lastly, both sprites were imported as .png files.

### Snake (Bee) Class
I began by creating a class for the “snake” of the game, defining aspects of movement and length.  I imported the .png sprite file and changed its dimensions in order to fit the logic of the code.  The movement is controlled by the user, but like the original Snake game, the “snake” continues to automatically move in the direction of the arrow key that the user has pressed.  Additionally, the “snake” will increase in length for every “snack” that it collides with - in this case, the more honey that is collected by the user, the more bees it will attract hence the increase in length.

### Snack (Honey) Class
I then created a class for the “snack” of the game.  Again, I imported the .png file and changed the dimensions of the sprite.  The “snack” first spawns in the same coordinate location at the beginning of the game, just as the “snake” does.  Every time a collision occurs, the “snack” is removed and another is created in a randomly determined coordinate which repeats every time.

### Game Class Setup
Lastly, I created a class for the entire game and included the logic of running the game as well.  This class includes the creation of the game window, the proper utilization of the “snake” and “snack”, the logic behind the collisions, the imported background image, the score system, the implementation of the game ending, the sprites resetting, and the actual run of the game.  I defined the collisions in order to use this when programming instances where the “snake” collides with the “snack” in order to increase the score, and included sound effects that play each time this collision occurs.  I also implemented the idea of the “snake” colliding with itself and the “snake” colliding with the walls of the game window, which ultimately ends the game.  These two ideas were seemingly similar and therefore use the same sound effect when the collision occurs.

The score is placed on the top right corner of the game window and uses the length of the “snake” to determine the score, but subtracts 1 in order for the game to start with an initial score of 0.  When the game is over due to an unwanted collision, everything on the screen is covered by a new rendered background and text is displayed in the window.  This gives the user their total score for that round of the game, and prompts them to press ENTER to play again in which everything is reset, or press ESC to stop and exit the game.

The final portion of the program is the running of the game itself.  I began by implementing the movement of the “snake” when certain keys are pressed by the user, and used event.key instead of keys_pressed so that the user can only press one key at a time instead allowing the user to move in diagonal directions.  The pause feature was a small addition to make sure that the user is not able to press any keys with effect when the game is not in play.  An exception is raised when the game is over, and Exception as e is used because it is meant to only accept the exception that is meant to be caught from the game_over function.

#### Sources
This game was based on and inspired by the snake game tutorials from freecodecamp.org, and Youtubers TechWithTim and LeMaster Tech.
