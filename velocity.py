from direction import Direction
import math


class Velocity():

    def __init__(self):
        self._dx = 0
        self._dy = 0

    def get_dx(self):
        """returns the horizontal component of velocity."""
        return self._dx

    def get_dy(self):
        """returns the vertical component of velocity."""
        return self._dy

    def get_speed(self):
        """
        determines the speed of the velocity.

              dx
           -------
           |     /
        dy |    /
           |   /
           |  /   speed/total
           | /
           |/

        dx^2 + dx^2 = speed^2

        speed = sqrt(dx^2 + dy^2)

        returns the speed.
        """
        return math.sqrt((self._dx ** 2) + (self._dy ** 2))
        
    def get_direction(self):
        """
        determines the direction of the velocity.
        Formula:
            tan(a) = Opp / adj
            tan(a) = dx / dy
            a = arctan(dx / dy)
        """
        direction = Direction()
        if self._dx > 0:
            angle = math.atan(self._dx / self._dy)
        
        elif self._dx < 0:
            angle = math.atan(self._dx / self._dy) + math.pi
        
        direction.set_radians(angle)
        return direction

    def set_dx(self, dx):
        """sets the value for horizontal component"""
        self._dx = dx

    def set_dy(self, dy):
        """sets the value for vertical component"""
        self._dy = dy

    def set_dx_dy(self, dx, dy):
        """sets both horizontal and vertical components"""
        self._dx = dx
        self._dy = dy

    def add_dx(self, dx):
        """adds the passed in value to the horizontal component."""
        self._dx += dx

    def add_dy(self, dy):
        """adds the passed in value to the vertical component."""
        self._dy += dy

    def add_vel(self, vel):
        """adds the values from a passed in Velocity object to
        both horizontal and vertical components. """
        self._dx += vel._dx
        self._dy += vel._dy

    def reverse(self):
        """reverses the velocity"""
        self._dx = -1 * self._dx
        self._dy = -1 * self._dy

"""
vel = Velocity()

vel.set_dx(300)
vel.set_dy(300)
direction = vel.get_direction()
print(f"The angle is: {direction.get_radians()}")
# pi / 4 = 0.78539816

vel.set_dx_dy(-300, 300)
direction = vel.get_direction()
print(f"The angle is: {direction.get_radians()}")
#  3pi / 4 = 2.35619449

vel.set_dx_dy(-300, -300)
direction = vel.get_direction()
print(f"The angle is: {direction.get_radians()}")
# 5pi / 4 = 3.926990

vel.set_dx_dy(300, -300)
direction = vel.get_direction()
print(f"The angle is: {direction.get_radians()}")
# 7pi / 4 = 5.4977871
"""