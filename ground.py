import math
import random
import constants
from position import Position

class Ground():

    def __init__(self, screen_size_pos):
        self._ground = [0 for x in range(math.ceil(screen_size_pos.get_pixels_x()))]
        self._screen_size = screen_size_pos
        self._itank_1 = 0
        self._itank_2 = 0

    def reset(self, pos_tank_1, pos_tank_2):
        """resets the current map with new ground and positioning.
        returns the new positions for the two tanks."""
        
        # determine the width of the screen
        width = math.floor(self._screen_size.get_pixels_x())

        # determing the positions of the tanks
        self._itank_1 = math.floor(pos_tank_1.get_pixels_x)
        if self._itank_1 > width / 2:
            self._itank_2 = random.randint(1, math.floor(width / 2))
        
        else:
            self._itank_2 = random.randint(math.ceil(width / 2), math.floor(self._screen_size.get_pixels_x))
        
        # determine the altitude limits
        min_pos = Position()
        min_pos.set_meters_x(0)
        min_pos.set_meters_y(constants.MIN_ALTITUDE)

        max_pos = Position()
        max_pos.set_meters_x(self._screen_size.get_meters_x())
        max_pos.set_meters_y(constants.MAX_ALTITUDE)

        # set the elevation for the ground at each location
        self._ground[0] = min_pos.get_pixels_y()  # the initial elevation is low
        dy = constants.MAX_SLOPE / 2  # the initial slope is heavily biased to up
        for i in range(1, width):
            # put the tanks on flat ground
            if (i > self._itank_1 - constants.WIDTH_TANK / 2 and
                i < self._itank_1 + constants.WIDTH_TANK / 2):
                self._ground[i] = self._ground[i - 1]
            
            elif (i > self._itank_2 - constants.WIDTH_TANK / 2 and
                i < self._itank_2 + constants.WIDTH_TANK / 2):
                self._ground[i] = self._ground[i - 1]

            else:
                # what percentage of the elevation were we at?
                percent = (self._ground[i - 1] - min_pos.get_pixels_y()) / (max_pos.get_pixels_y() - min_pos.get_pixels_y())

                # set the slope of the ground
                dy += (1.0 - percent) * random.randint(0.0, constants.LUMPINESS) + (percent) * random(-constants.LUMPINESS, 0.0)
                if dy > constants.MAX_SLOPE:
                    dy = constants.MAX_SLOPE
                if dy < -constants.MAX_SLOPE:
                    dy = -constants.MAX_SLOPE

                # determine the elevation according to the slope
                self._ground[i] = self._ground[i - 1] + dy + random.randrange(-constants.TEXTURE, constants.TEXTURE)
        

        # set the tanks positioning.
        pos_tank_1.set_pixels_x(self._itank_1)
        pos_tank_1.set_pixels_y(self._ground[self._itank_1])

        pos_tank_2.set_pixels_x(self._itank_2)
        pos_tank_2.set_pixels_y(self._ground[self._itank_2])

        return (pos_tank_1, pos_tank_2)


    #come back and fix this after making display class
    """
    def draw(self, display):
        #  put the meter markers along the side
        for y_pos in range(0, math.ceil(self._screen_size.get_pixels_y()), 1000):
            
            left_pos = Position()
            left_pos.set_meters_x(0)
            left_pos.set_meters_y(y_pos)

            right_pos = Position()
            right_pos.set_meters_x(0)
            right_pos.set_meters_y(y_pos)


            posRight.setPixelsX(posUpperRight.getPixelsX());
            gout.drawLine(posLeft, posRight, 0.85, 0.85, 0.85);


        // iterate through the entire ground and draw it all
        int width = (int)posUpperRight.getPixelsX();
        for (int i = 0; i < width; i++)
        {
            Position posBottom;
            Position posTop;
            posBottom.setPixelsX((double)i);
            posTop.setPixelsX((double)i + 1.0);
            posTop.setPixelsY(ground[i]);
            gout.drawRectangle(posBottom, posTop, 0.6 /*red*/, 0.4 /*green*/, 0.2 /*blue*/);
        }

        // draw the target
        Position posTarget = getTarget();
        gout.drawTarget(posTarget);

        // put the kilometer markers along the bottom
        for (Position pos(1000.0, 0.0); pos.getPixelsX() < posUpperRight.getPixelsX(); pos.addMetersX(1000.0))
        {
            Position posBottom(pos);
            Position posTop(pos);
            posTop.addPixelsY(10);
            gout.drawLine(posTop, posBottom, 0.6, 0.6, 0.6);
        }

        // put the kilometer labels along the bottom
        for (Position pos(5000.0, 0.0); pos.getPixelsX() < posUpperRight.getPixelsX(); pos.addMetersX(5000.0))
        {
            Position posText(pos);
            posText.addPixelsY(15);
            posText.addPixelsX(-10);

            gout = posText;
            gout << (int)(pos.getMetersX() / 1000.0) << "km";
        }

        // draw the altitude labels along the side
        for (Position pos(0.0, 2000.0); pos.getPixelsY() < posUpperRight.getPixelsY(); pos.addMetersY(2000.0))
        {
            Position posText(pos);
            posText.addPixelsX(5);
            posText.addPixelsY(-2);

            gout = posText;
            gout << (int)(pos.getMetersY()) << "m";
        }
    """
    def get_elevation_meters(self, position):
        """returns the elevation of the ground."""
        pos_elevation = Position()
        pos_elevation.set_meters_x(position.get_meters_x())
        pos_elevation.set_meters_y(position.get_meters_y())

        if (position.get_pixels_x() >= 0 and 
            position.get_pixels_x() < self._screen_size.get_pixels_x()):
            pos_elevation.set_pixels_y(self._ground[math.floor(position.get_pixels_x())]) 
        
        else:
            pos_elevation.set_pixels_y(0)
        
        return pos_elevation.get_meters_y()

    def get_tank_1_position(self):
        """returns the position of tank 1"""
        pos_tank_1 = Position()
        pos_tank_1.set_pixels_x(self._itank_1)
        pos_tank_1.set_pixels_y(self._ground[self._itank_1])
        return pos_tank_1
    
    def get_tank_2_position(self):
        """returns the position of tank 2"""
        pos_tank_2 = Position()
        pos_tank_2.set_pixels_x(self._itank_2)
        pos_tank_2.set_pixels_y(self._ground[self._itank_2])
        return pos_tank_2
