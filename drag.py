import math

class Drag():


    def __init__(self):
        self._drag_coef = 0
        self._air_pressure = 0
        self._surface_area = 0

        self._drag_table = [
            [0.300, 0.1629],
            [0.500,	0.1659],
            [0.700,	0.2031],
            [0.890,	0.2597],
            [0.920, 0.3010],
            [0.960, 0.3287],
            [0.980,	0.4002],
            [1.000,	0.4258],
            [1.020,	0.4335],
            [1.060,	0.4483],
            [1.240,	0.4064],
            [1.530,	0.3663],
            [1.990,	0.2897],
            [2.870,	0.2297],
            [2.890,	0.2306],
            [5.000,	0.2656]
            ]

        self._density_table = [
            [0,	1.2250000 ],
            [1000, 1.1120000],
            [2000, 1.0070000],
            [3000, 0.9093000],
            [4000, 0.8194000],
            [5000, 0.7364000],
            [6000, 0.6601000],
            [7000, 0.5900000],
            [8000, 0.5258000],
            [9000, 0.4671000],
            [10000, 0.4135000],
            [15000, 0.1948000],
            [20000, 0.0889100],
            [25000,	0.0400800],
            [30000,	0.0184100],
            [40000,	0.0039960],
            [50000,	0.0010270],
            [60000,	0.0003097],
            [70000,	0.0000828],
            [80000, 0.0000185]
            ]

        self._sound_table = [
            [ 0, 340 ],
            [ 1000, 336 ],
            [ 2000, 332 ],
            [ 3000, 328 ],
            [ 4000, 324 ],
            [ 5000, 320 ],
            [ 6000, 316 ],
            [ 7000, 312 ],
            [ 8000, 308 ],
            [ 9000, 303 ],
            [ 10000, 299 ],
            [ 15000, 295 ],
            [ 20000, 295 ],
            [ 25000, 295 ],
            [ 30000, 305 ],
            [ 40000, 324 ]
        ]
    
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

    
    def _compute_surface_area(self, radius):
        """
        Determines the surface area of a circle.
        """
        self._surface_area = radius * radius * math.pi

    
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


    def compute_drag_force(self, radius, velocity, altitude):
        """
         Determines the drag force acting on a projectile
         FORMULA:
        	d = 0.5 * c * p * v^2 * a
            
            c: drag coefficient
            p: density of fluid/gas
            v: velocity of the projectile
            a: surface area
            d: drag force in newtons
        
         INPUT
        	radius: the radius of the projectile
        	velocity: the velocity of the projectile
        	altitude: the altitude of the projectile
         OUTPUT
        	the drag force acting on the projectile
        """

        # setup the surface area
        self._compute_surface_area(radius)

        # determine air pressure
        air_pressure_points = self._look_up_table(self._density_table, altitude)
        self._air_pressure = self._compute_interpolation(air_pressure_points)

        # determine speed of sound
        sound_points = self._look_up_table(self._sound_table, altitude)
        sound_vel = self._compute_interpolation(sound_points)
        mach = abs(velocity) / sound_vel

        # determine drag coefficient
        drag_points = self._look_up_table(self._drag_table, mach)
        self._drag_coef = self._compute_interpolation(drag_points)

        return 0.5 * self._drag_coef * self._air_pressure * velocity * velocity * self._surface_area

