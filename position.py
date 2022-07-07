import constants

class Position():
    
    def __init__(self):
        self._x = 0
        self._y = 0
        self._pixels_to_meters = constants.PIXELS_TO_METERS

    def get_meters_x(self):
        """returns the x position."""
        return self._x

    def get_meters_y(self):
        """returns the y position."""
        return self._y

    def get_pixels_x(self):
        """
        converts meters into pixels and returns pixel value for x.
        """
        return round(self._x / self._pixels_to_meters)

    def get_pixels_y(self):
        """
        converts meters into pixels and returns pixel value for y.
        """
        return round(self._y / self._pixels_to_meters)

    def set_meters_x(self, meters_x):
        """sets the value for x position."""
        self._x = meters_x

    def set_meters_y(self, meters_y):
        """sets the value for y position."""
        self._y = meters_y

    def set_pixels_x(self, pixels_x):
        """sets the value for x based on pixels."""
        self._x = pixels_x * self._pixels_to_meters

    def set_pixels_y(self, pixels_y):
        """sets the value for y based on pixels."""
        self._y = pixels_y * self._pixels_to_meters

    def add_meters_x(self, meters_x):
        """adds to x based on a given distance."""
        self._x += meters_x

    def add_meters_y(self, meters_y):
        """adds to y based on a given distance."""
        self._y += meters_y
    
    def add_pixels_x(self, pixels_x):
        """adds to x based on a given pixel distance."""
        self.set_pixels_x(self.get_pixels_x() + pixels_x)
        

    def add_pixels_y(self, pixels_y):
        """adds to y based on a given pixel distance."""
        self.set_pixels_y(self.get_pixels_y() + pixels_y)

    