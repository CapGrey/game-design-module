from position import Position
from velocity import Velocity
from acceleration import Acceleration


class Projectile():

    def __init__(self):
        self._mass = 0
        self._radius = 0
        self._position = Position()
        self._vel = Velocity()
        self._angle = 0
        self.flight_status = False
    
    def reset(self):
        """resets the projectile to be fired again."""
        # reset position
        self._position.set_pixels_x(0)
        self._position.set_pixels_y(0)

        # reset velocity
        self._vel.set_dx_dy(0, 0)

        # reset angle
        self._angle = 0
        self.flight_status = False

    def fire(self, position, angle, velocity):
        """Launches the projectile from the tank's position"""
        self._position = position
        self._angle = angle
        self._vel = velocity
        self.flight_status = True

    def advance(self, time, drag):
        """Moves the projectile based time elapsed and drag force."""
        # compute the drag force
        drag_force = drag.compute_drag_force(self._radius, 
            self._vel.get_speed(), self._position.get_meters_y())
        
        # calculate the acceleration of the projectile
        accel = Acceleration()
        accel.compute_acceleration(drag_force, self._mass, 
            self._position.get_meters_y(), self._angle)
        
        # update velocity due to acceleration and time.
        self._vel.add_dx(accel.get_ddx() * time)
        self._vel.add_dy(accel.get_ddy() * time)

        # update position
        self._position.add_meters_x(
            (self._vel.get_dx() * time) + (0.5 * accel.get_ddx() * (time ** 2))
        )
        
        self._position.add_meters_y(
            (self._vel.get_dy() * time) + (0.5 * accel.get_ddy() * (time ** 2))
        )

    def draw(self, display, num):
        """draws the projectile."""
        display.draw_projectile(num, self._position)

    def get_altitude(self):
        """returns the projectile's altitude in meters"""
        return self._position.get_meters_y()

    def get_position(self):
        """returns the projectile's position."""
        return self._position

    def set_mass(self, mass):
        """Sets the mass of the projectile in kg."""
        self._mass = mass

    def set_radius(self, radius):
        """sets the radius of the projectile in meters."""
        self._radius = radius

