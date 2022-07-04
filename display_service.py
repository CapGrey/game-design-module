import arcade
import constants

class Display_Service():

    def __init__(self):
        self._tank_1 = arcade.load_texture(constants.TANK_1_ASSET)
        self._tank_2 = arcade.load_texture(constants.TANK_2_ASSET)
        self._cannon_1 = arcade.load_texture(constants.CANNON_1_ASSET)
        self._cannon_2 = arcade.load_texture(constants.CANNON_2_ASSET)
        self._canon_1_angle = 90
        self._cannon_2_angle = 90
        self._bullet_1 = arcade.load_texture(constants.BULLET_1)
        self._bullet_2 = arcade.load_texture(constants.BULLET_2)

        self._ground_color = constants.GROUND_COLOR
        self._background_color = constants.BACKGROUND_COLOR

    
    def update_tank(self, tank_angle, tank_num, position):
        """Updates the tank's cannon angle"""
        if tank_num == 1:
            self._canon_1_angle = tank_angle
            arcade.draw_scaled_texture_rectangle(
                position.get_pixels_x(), position.get_pixels_y(),
                self._tank_1, constants.TANK_SCALE, 0)
            
            arcade.draw_scaled_texture_rectangle(
                position.get_pixels_x(),
                position.get_pixels_y() + constants.DISTANCE_BETWEEN_CANNON_TANK,
                self._cannon_1, self._canon_1_angle)

        else:
            self._cannon_2_angle = tank_angle
            arcade.draw_scaled_texture_rectangle(
                position.get_pixels_x(), position.get_pixels_y(),
                self._tank_2, constants.TANK_SCALE, 0)
            
            arcade.draw_scaled_texture_rectangle(
                position.get_pixels_x(),
                position.get_pixels_y() + constants.DISTANCE_BETWEEN_CANNON_TANK,
                self._cannon_2, self._canon_2_angle)
        


    def draw_background(self):
        """draws the background of the game."""
        arcade.set_background_color(self._background_color)
    
    def draw_projectile(self, num, pos):
        """draws the projectile."""
        if num == 1:
            arcade.draw_scaled_texture_rectangle(
                pos.get_pixels_x(), pos.get_pixels_y(), 
                self._bullet_1,
                constants.BULLET_SCALE)
        
        else:
            arcade.draw_scaled_texture_rectangle(
                pos.get_pixels_x(), pos.get_pixels_y(), 
                self._bullet_2,
                constants.BULLET_SCALE)
    
    def draw_ground(self, x_pos, y_limit):
        """draws one section of the ground."""
        arcade.draw_rectangle_filled(x_pos, y_limit / 2, 1, y_limit,
        self._background_color)