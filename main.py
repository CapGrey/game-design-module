import arcade
from game import Game
from position import Position
import constants

def main():
    # setup game players
    window_size_pos = Position()
    window_size_pos.set_pixels_x(constants.WINDOW_SIZE_X)
    window_size_pos.set_pixels_y(constants.WINDOW_SIZE_Y)
    game = Game(window_size_pos)

    # setup bullets and tanks
    game.set_muzzel_velocity(constants.MUZZLE_VELOCITY)
    game.set_projectile_radius_and_mass(constants.PROJECTILE_RADIUS,
        constants.PROJECTILE_MASS)

    # play game
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()