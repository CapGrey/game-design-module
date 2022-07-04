from position import Position
from direction import Direction
import math

class Tank():

    def __init__(self):
        self._pos = Position()
        self._muzzle_velocity = 0
        self._muzzle_angle = Direction()
        self.hitbox = []


    def draw(self, display, tank_num):
        """draws the tank."""
        display.update_tank(self._muzzle_angle.get_degrees(), 
            tank_num, self._pos)

    def get_position(self):
        """returns the position of the tank"""
        return self._pos

    def get_muzzle_vel(self):
        """returns the muzzle velocity of the tank"""
        return self._muzzle_velocity

    def set_muzzle_vel(self, vel):
        """sets the value for the muzzle velocity"""
        self._muzzle_velocity = vel

    def set_pos(self, position):
        """sets the position by passed in position object."""
        self._pos.set_meters_x(position.get_meters_x())
        self._pos.set_meters_y(position.set_meters_y())


    def large_rotation(self, radians):
        """rotates the muzzle by a larger angle in radians"""
        self._muzzle_angle.add_radians(radians)

    def small_rotation(self, radians):
        """rotates the muzzle by a smaller angle in radians"""
        self._muzzle_angle.add_radians(radians)

    def create_hitbox(self, size_in_pixels_x, size_in_pixels_y):
        """
        creates the hitbox for the tank
        Aurgs:
            sizel_in_pixels_x-- the horizontal size of the hitbox
            size_in_pixels_y-- the vertical size of the hitbox
        """
        side_in_pixels = math.floor(size_in_pixels_x / 2)

        left_border = self._pos.get_pixels_x() - side_in_pixels
        right_border = self._pos.get_pixels_x() + side_in_pixels

        top_border = self._pos.get_pixels_y() + size_in_pixels_y
        bottom_border = self._pos.get_pixels_y()

        self.hitbox = [left_border, right_border, 
            top_border, bottom_border]



