# Overview


The game that I created was a tanks style game. In the game, two tanks
are randomly placed on either side of the map. Each player tries
to shoot the other by changing the angle of their tank cannon.

To play the game, use the following command: `py main.py` 

if that fails, try `python main.py`

The controls are simple, for player 1, the left key moves left by a
large degree, the right key moves right by a large degree, the up
and down keys move the angle by a small degree.
To fire, press space.

Player 2 uses WASD to the same effect and presses R to fire.


My Purpose for writing this software was to learn the Arcade 3rd
party library. My intention was to also learn more about how 
physics engines work by creating my own.

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the game being played and a walkthrough of the code.}

[Software Demo Video](https://youtu.be/fui0gPO04ik)

# Development Environment

Visual Studio Code: Text Editor

Python 3.10: Language
Arcade: 3rd party Library

# Useful Websites


* [Geeks for Geeks](https://www.geeksforgeeks.org/add-backgound-image-in-python-arcade/)
* [Arcade Academy](https://api.arcade.academy)

# Future Work


* Players movement is restricted by a single key press: holding down the key does not continueously change the angle.
* The acceleration of the bullet is accurate as long as the y velocity is positve. Drag should invert once the bullet starts falling.
* Sometimes the bullet moves too quickly through the tank's hitbox and will not register as a hit.