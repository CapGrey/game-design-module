from math import fabs
import arcade

class Input_Service(arcade.Window):
    def __init__(self):
        self.tank_1_up = False
        self.tank_1_down = False
        self.tank_1_left = False
        self.tank_1_right = False
        self.tank_1_fire = False

        self.tank_2_up = False
        self.tank_2_down = False
        self.tank_2_left = False
        self.tank_2_right = False
        self.tank_2_fire = False

    def on_key_press(self, symbol, modifier):
        """Notifies game if movement or fire keys are pressed"""
        # check key presses for tank 1.
        if symbol == arcade.key.UP:
            self.tank_1_up = True
        
        elif symbol == arcade.key.DOWN:
            self.tank_1_down = True
        
        elif symbol == arcade.key.LEFT:
            self.tank_1_left = True
        
        elif symbol == arcade.key.RIGHT:
            self.tank_1_right = True
        
        elif symbol == arcade.key.SPACE:
            self.tank_1_fire = True

        # check key presses for tank 2.
        elif symbol == arcade.key.W:
            self.tank_2_up = True
        
        elif symbol == arcade.key.S:
            self.tank_2_down = True
        
        elif symbol == arcade.key.A:
            self.tank_2_left = True
        
        elif symbol == arcade.key.D:
            self.tank_2_right = True
        
        elif symbol == arcade.key.R:
            self.tank_2_fire = True
        
    def on_key_release(self, symbol, modifier):
        """Notifies game if movement or fire keys are released"""
        # check key presses for tank 1.
        if symbol == arcade.key.UP:
            self.tank_1_up = False
        
        elif symbol == arcade.key.DOWN:
            self.tank_1_down = False
        
        elif symbol == arcade.key.LEFT:
            self.tank_1_left = False
        
        elif symbol == arcade.key.RIGHT:
            self.tank_1_right = False
        
        elif symbol == arcade.key.SPACE:
            self.tank_1_fire = False

        # check key presses for tank 2.
        elif symbol == arcade.key.W:
            self.tank_2_up = False
        
        elif symbol == arcade.key.S:
            self.tank_2_down = False
        
        elif symbol == arcade.key.A:
            self.tank_2_left = False
        
        elif symbol == arcade.key.D:
            self.tank_2_right = False
        
        elif symbol == arcade.key.R:
            self.tank_2_fire = False

        


"""
# Importing arcade module
import arcade
  
# Creating MainGame class       
class MainGame(arcade.Window):
    def __init__(self):
        super().__init__(600, 600, title="Keyboard Inputs")
  
    # Creating on_draw() function to draw on the screen
    def on_draw(self):
        arcade.start_render()
          
    # Creating function to check button is pressed
    # or not
    def on_key_press(self, symbol,modifier):
  
        # Checking the button pressed
        # is up arrow key or not
        if symbol == arcade.key.UP:
            print("Upper arrow key is pressed")
  
    # Creating function to check button is released
    # or not
    def on_key_release(self, symbol, modifier):
  
        # Checking the button pressed
        # is up arrow key or not
        if symbol == arcade.key.UP:
            print("Upper arrow key is released\n")
          
# Calling MainGame class       
MainGame()
arcade.run()
"""