import math

class Direction():
    def __init__(self):
        self._radians = math.pi / 2
    
    def _normalize_radians(self, radians):
        """
        Normalizes the passed in radians to a value between 0 and 2pi
        """

        multiple = math.floor(abs(radians / (2 * math.pi)))

        # if the value is greater than 1 full circle:
        if radians >= 2 * math.pi:
            return radians - (multiple * 2 * math.pi)

        # if the value is less than 0.
        elif radians < 0:
            return radians + (multiple * 2 * math.pi) + (2 * math.pi)
    
        # if the value is alread within bounds.
        else:
            return radians

    def set_radians(self, radians):
        """sets the values of radians after normalizing."""
        self._radians = self._normalize_radians(radians)
        

    def reverse(self):
        """Reverses the value of the radians."""
        self._radians = self._normalize_radians(self._radians + math.pi)

    def get_radians(self):
        """returns the value of the angle in radians."""
        return self._radians
