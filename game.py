import arcade
from tank import Tank
from projectile import Projectile
from ground import Ground
from display_service import Display_Service
from input_service import Input_Service
from velocity import Velocity
from drag import Drag
import constants

class Game(arcade.Window):

    def __init__(self, window_size_pos):
        super().__init__(constants.WINDOW_SIZE_X,
            constants.WINDOW_SIZE_Y, "Tanks")
        self._tank_1 = Tank()
        self._tank_2 = Tank()
        self._bullet_1 = Projectile()
        self._bullet_2 = Projectile()
        self._time_interval = constants.TIME_INTERVAL
        self._ground = Ground(window_size_pos)
        self._winner = 0

        self._display = Display_Service()
        self._ui = Input_Service()

        self._bullet_sound = arcade.load_sound(constants.BULLET_SOUND)
        self._music = arcade.load_sound(constants.MUSIC)
        self._win_sound = arcade.load_sound(constants.WIN_SOUND)
    
    def setup(self):
        self._display.draw_background()
        self._ground.reset(self._tank_1.get_position(), self._tank_2.get_position())
        self._tank_1.create_hitbox(constants.WIDTH_TANK, constants.HEIGHT_TANK)
        self._tank_2.create_hitbox(constants.WIDTH_TANK, constants.HEIGHT_TANK)
        arcade.play_sound(self._music, 0.5)
    
    def on_update(self, delta_time= 1/60):
        self.advance()
        self.check_and_handle_collisions()

    def on_draw(self):
        """renders the screen."""
        self.clear()
        self.display()
    
    def on_key_press(self, symbol, modifiers):
        self._ui.on_key_press(symbol, modifiers)
        self.user_input()
    
    def on_key_release(self, symbol, modifiers):
        self._ui.on_key_release(symbol, modifiers)

    def reset(self):
        """resets the game"""
        # reset bullets
        self._bullet_1.reset()
        self._bullet_2.reset()

        # reset ground and tanks
        self._ground.reset(self._tank_1.get_position(), 
            self._tank_2.get_position())

        self._tank_1.create_hitbox(constants.WIDTH_TANK, constants.HEIGHT_TANK)
        self._tank_2.create_hitbox(constants.WIDTH_TANK, constants.HEIGHT_TANK)
        
        # reset winner
        self._winner = 0
        
   
    def set_muzzel_velocity(self, vel):
        """sets the muzzle velocity for both tanks."""
        self._tank_1.set_muzzle_vel(vel)
        self._tank_2.set_muzzle_vel(vel)
    
    def set_projectile_radius_and_mass(self, radius, mass):
        """sets the radius of the projectiles."""
        self._bullet_1.set_radius(radius)
        self._bullet_2.set_radius(radius)

        self._bullet_1.set_mass(mass)
        self._bullet_2.set_mass(mass)
    
    def display(self):
        """displays the screen to the user."""
        arcade.start_render()
        # draw the ground
        self._ground.draw(self._display)

        # draw the tanks
        self._tank_1.draw(self._display, 1)
        self._tank_2.draw(self._display, 2)
            

        # draw the bullets
        self._bullet_1.draw(self._display, 1)
        self._bullet_2.draw(self._display, 2)

        # draw text for win condition
        if self._winner == 1:
            arcade.draw_text("Tank 1 wins!",
            constants.WINDOW_SIZE_X // 2 - 150, 
            constants.WINDOW_SIZE_Y // 2, 
            arcade.color.ALIZARIN_CRIMSON, 40)

        elif self._winner == 2:
            arcade.draw_text("Tank 2 wins!",
            constants.WINDOW_SIZE_X // 2 - 150, 
            constants.WINDOW_SIZE_Y // 2, 
            arcade.color.ALIZARIN_CRIMSON, 40, 800)
    

        arcade.finish_render()
    
    def user_input(self):
        """handles user input."""
        if self._winner == 0:
            # tank 1 movement
            if self._ui.tank_1_down:
                self._tank_1.small_rotation(-constants.SMALL_ROTATION)
            if self._ui.tank_1_up:
                self._tank_1.small_rotation(constants.SMALL_ROTATION)
            if self._ui.tank_1_left:
                self._tank_1.large_rotation(constants.LARGE_ROTATION)
            if self._ui.tank_1_right:
                self._tank_1.large_rotation(-constants.LARGE_ROTATION)

            # tank 2 movement
            if self._ui.tank_2_down:
                self._tank_2.small_rotation(-constants.SMALL_ROTATION)
            if self._ui.tank_2_up:
                self._tank_2.small_rotation(constants.SMALL_ROTATION)
            if self._ui.tank_2_left:
                self._tank_2.large_rotation(constants.LARGE_ROTATION)
            if self._ui.tank_2_right:
                self._tank_2.large_rotation(-constants.LARGE_ROTATION)
            
            # handle bullets being fired. Only one bullet per
            # tank is allowed
            if self._ui.tank_1_fire:
                if not self._bullet_1.flight_status:
                    # lanch projectile
                    vel = Velocity()
                    vel.compute_vel_from_total(self._tank_1._muzzle_angle.get_radians(), 
                        self._tank_1.get_muzzle_vel())

                    self._bullet_1.fire(self._tank_1.get_projectile_launch_position(),
                    self._tank_1._muzzle_angle.get_radians(), vel)
                    
                    # play launch sound
                    arcade.play_sound(self._bullet_sound)
            
            if self._ui.tank_2_fire:
                if not self._bullet_2.flight_status:
                    # launch
                    vel = Velocity()
                    vel.compute_vel_from_total(self._tank_2._muzzle_angle.get_radians(),
                    self._tank_2.get_muzzle_vel())

                    self._bullet_2.fire(self._tank_2.get_projectile_launch_position(), 
                    self._tank_2._muzzle_angle.get_radians(), vel)
                    
                    # play launch sound
                    arcade.play_sound(self._bullet_sound)

        else:
            if self._ui.tank_1_fire or self._ui.tank_2_fire:
                self.reset()

    def advance(self):
        """advances the bullets in the sky."""
        if self._bullet_1.flight_status:
            drag = Drag()
            self._bullet_1.advance(self._time_interval, drag)
        
        if self._bullet_2.flight_status:
            drag = Drag()
            self._bullet_2.advance(self._time_interval, drag)
    
    def check_and_handle_collisions(self):
        """
        checks all conditions:
        hit ground
        out of bounds left or right
        hit tank
        """
        # check if the tanks have been hit
        bullet_1_hit_tank = self._has_hit_tank(1)
        bullet_2_hit_tank = self._has_hit_tank(2)
        
        if bullet_1_hit_tank:
            self._winner = 1
            return
        
        elif bullet_2_hit_tank:
            self._winner = 2
            return

        # check if the ground has been hit
        bullet_1_hit_ground = self._has_hit_ground(1)
        bullet_2_hit_ground = self._has_hit_ground(2)

        # check if the border has been hit
        bullet_1_hit_border = self._has_hit_border(1)
        bullet_2_hit_border = self._has_hit_border(2)

        # reset bullet 1
        if bullet_1_hit_border or bullet_1_hit_ground or bullet_1_hit_tank:
            self._bullet_1.reset()
        
        # reset bullet 2
        if bullet_2_hit_border or bullet_2_hit_ground or bullet_2_hit_tank:
            self._bullet_2.reset()

    def _has_hit_ground(self, num):
        """returns true if the ground has been hit"""
        # check bullet 1
        if num == 1:
            if self._bullet_1.flight_status:
                if (self._bullet_1.get_altitude() <=
                self._ground.get_elevation_meters(self._bullet_1.get_position())):
                    return True
        
        # check bullet 2
        else:
            if self._bullet_2.flight_status:
                if (self._bullet_2.get_altitude() <= 
                self._ground.get_elevation_meters(self._bullet_2.get_position())):
                    return True
        
        return False

    def _has_hit_border(self, num):
        """checks if the bullets have hit the borders"""
        # check bullet 1
        if num == 1:
            if self._bullet_1.flight_status:
            # left side
                if self._bullet_1._position.get_pixels_x() < 0:
                    return True
                
                # right side
                elif (self._bullet_1._position.get_pixels_x() >
                constants.WINDOW_SIZE_X):
                    return True

        # check bullet 2
        else:
            if self._bullet_2.flight_status:
                # left side
                if self._bullet_2._position.get_pixels_x() < 0:
                    return True
                
                # right side
                elif (self._bullet_2._position.get_pixels_x() >
                constants.WINDOW_SIZE_X):
                    return True
            
        return False

    def _has_hit_tank(self, num):
        """checks if the bullet has hit the tank"""
        # check bullet 1
        if num == 1:
            if self._bullet_1.flight_status:

                # check if the bullet is within the hitbox
                # left to right
                if (self._bullet_1.get_position().get_pixels_x()
                >= self._tank_2.hitbox[0]
                and self._bullet_1.get_position().get_pixels_x()
                <= self._tank_2.hitbox[1]):

                    # check if the bullet is within top and bottom
                    if (self._bullet_1.get_position().get_pixels_y()
                    <= self._tank_2.hitbox[2]
                    and self._bullet_1.get_position().get_pixels_y()
                    >= self._tank_2.hitbox[3]):
                        return True
        
        # check bullet 2
        else:
            if self._bullet_2.flight_status:
                
                # check if the bullet is within the hitbox
                # left to right
                if (self._bullet_2.get_position().get_pixels_x()
                >= self._tank_1.hitbox[0]
                and self._bullet_2.get_position().get_pixels_x()
                <= self._tank_1.hitbox[1]):

                    # check if the bullet is within top and bottom
                    if (self._bullet_2.get_position().get_pixels_y()
                    <= self._tank_1.hitbox[2]
                    and self._bullet_2.get_position().get_pixels_y()
                    >= self._tank_1.hitbox[3]):
                        return True
        
        return False

