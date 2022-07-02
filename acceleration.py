import math

class Acceleration():


    def __init__(self):
        self._ddx = 0
        self._ddy = 0
        self._gravity_table = [
		[ 0, 9.807 ],
		[ 1000, 9.804 ],
		[ 2000, 9.801 ],
		[ 3000, 9.797 ],
		[ 4000, 9.794 ],
		[ 5000, 9.791 ],
		[ 6000, 9.788 ],
		[ 7000, 9.785 ],
		[ 8000, 9.782 ],
		[ 9000, 9.779 ],
		[ 10000,9.776 ],
		[ 15000, 9.761 ],
		[ 20000, 9.745 ],
		[ 25000, 9.730 ]
        ]

    def get_ddx(self):
        return self._ddx

    def get_ddy(self):
        return self._ddy

    def set_ddx(self, ddx):
        self._ddx = ddx
    
    def set_ddy(self, ddy):
        self._ddy = ddy
    
    def compute_acceleration(self, force, mass, altitude, angle):
        """
        Computes the acceleration of an object due to force, mass
        and the altiude of the object.

        acceleration = force / mass

        altitude is used to determine the force that gravity exerts.
        angle is used to detemine horizontal and vertical components
        """
        total_accel = force / mass
        gravity = self._compute_gravity_accel(altitude)

        self._ddx = self._compute_horz_component(angle, total_accel)
        self._ddy = self._compute_vert_component(angle, total_accel)
        self._ddy -= gravity

    def _compute_interpolation(self, points):
        """
        Determines the interpolation between two points and 
        some value between those points.
        Formula:
            (r - r0)   (r1 - ro)
        -------- = ---------
        (d - d0)   (d1 - d0)
        
                    OR
            d = d0 + (((r - r0) * (d1 - d0)) / (r1 - r0))
        
        INPUT
            points: a vector of all the values in the formula
        OUTPUT
            the value for d
        """
        r0 = points[0]
        r = points[1]
        r1 = points[2]

        d0 = points[3]
        d1 = points[4]

		# check to see if points are equal
        if r0 == r1:
            return d0
        
        else:    
            return (((r - r0) * (d1 - d0)) / (r1 - r0)) + d0


    def _look_up_table(self, table, value):
        """
         Determines the two closest points in a table by a given
         value.
        
         INPUT
        	table: a 2D array that is a data table
        	value: the value to be searched for
         OUTPUT
        	an array containing the two closest points and the value
        	in the form of [r0, r, r1, d0, d1]
        """
        # determine bounds on array
        upper_limit = len(table) - 1
        lower_limit = 0
        
        search = True

        # find the midpoint of the array
        while search:
            midpoint = (upper_limit + lower_limit) // 2
            mid_element = table[midpoint][0]

            # if the exact value is found
            if mid_element == value:
                return [
                    table[midpoint][0],
                    value,
                    table[midpoint][0],
                    table[midpoint][1],
                    table[midpoint][1]
                    ]

            elif value > mid_element:

                if lower_limit + 1 == upper_limit:
                    # check the value at the end of the array
                    if upper_limit == len(table) - 1:
                        if table[upper_limit][0] <= value:
                            return [
                                table[upper_limit][0],
                                table[upper_limit][0],
                                table[upper_limit][0],
                                table[upper_limit][1],
                                table[upper_limit][1]
                            ]
                        
                    search = False
                
                # if the value is greater, change the lower limit
                else:
                    lower_limit = midpoint

            elif value < mid_element:

                if lower_limit + 1 == upper_limit:
                    if lower_limit == 0:
                        if table[lower_limit][0] >= value:
                            return [
                                table[lower_limit][0],
                                table[lower_limit][0],
                                table[lower_limit][0],
                                table[lower_limit][1],
                                table[lower_limit][1]
                            ]
                    
                    search = False
                
                # if the value is smaller, change the upper limit
                else:
                    upper_limit = midpoint
            
            if lower_limit == upper_limit:
                upper_limit += 1
        
        return [
            table[lower_limit][0],
            value,
            table[upper_limit][0],
            table[lower_limit][1],
            table[upper_limit][1]
        ]

    def _compute_gravity_accel(self, altitude):
        """returns the acceleration of gravity"""
        gravity_points = self._look_up_table(self._gravity_table, altitude)
        return self._compute_interpolation(gravity_points)
    
    def _compute_horz_component(self, angle, total):
        """returns the horizontal acceleration"""
        return math.sin(angle) + total

    def _compute_vert_component(self, angle, total):
        """returns the vertical acceleration"""
        return math.cos(angle) + total
    



