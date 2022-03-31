
import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.2
GOOD_SPRITE_SCALING_COIN = 0.18
BAD_SPRITE_SCALING_COIN = 0.19
GOOD_COIN_COUNT = 10
BAD_COIN_COUNT = 5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Coin_good(arcade.Sprite):
    """
    This class represents the coins on the screen.
    It is a child class of the arcade library's "Sprite" class.
    """

    def reset_pos(self):
        # Reset the coin to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        # Move the coin
        self.center_y -= 1

        # See if the coin has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            self.reset_pos()


class Coin_bad(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 18

    def update(self):

        # Move the coin
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If we are out-of-bounds, then 'bounce'
        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Flying Witch")

        # Variables that will hold sprite lists
        self.player_list = None
        self.good_coin_list = None
        self.bad_coin_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BUBBLE_GUM)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.good_coin_list = arcade.SpriteList()
        self.bad_coin_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player

        self.player_sprite = arcade.Sprite("character_2.gif", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(GOOD_COIN_COUNT):
            # Create the coin instance

            good_coin = Coin_good("coin_1.png", GOOD_SPRITE_SCALING_COIN)

            # Position the coin
            good_coin.center_x = random.randrange(SCREEN_WIDTH)
            good_coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.good_coin_list.append(good_coin)

        for i in range(BAD_COIN_COUNT):
            bad_coin = Coin_bad("coin.gif", BAD_SPRITE_SCALING_COIN)

            # Position the coin
            bad_coin.center_x = random.randrange(SCREEN_WIDTH)
            bad_coin.center_y = random.randrange(SCREEN_HEIGHT)
            bad_coin.change_x = random.randrange(2, 5, 2)
            bad_coin.center_y = random.randrange(2, 5, 2)

            # Add the coin to the lists
            self.bad_coin_list.append(bad_coin)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.good_coin_list.draw()
        self.player_list.draw()
        self.bad_coin_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):

        """ Movement and game logic """

        # Call update on all sprites

        self.good_coin_list.update()

        self.bad_coin_list.update()

        good_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.good_coin_list)
        for good_coin in good_hit_list:
            # remove coin from list
            good_coin.remove_from_sprite_lists()

            # add score when hit a good coin
            self.score += 1

            # add sound when hit a good coin
            self.collect_coin_sound = arcade.load_sound('collect_coin.wav')

            arcade.play_sound(self.collect_coin_sound)

        bad_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bad_coin_list)

        for bad_coin in bad_hit_list:
            # remove coin from list
            bad_coin.remove_from_sprite_lists()

            # remove score when hit a bad coin
            self.score -= 1

            # Add bad hit sound
            self.hit_sound = arcade.load_sound('hit.wav')
            arcade.play_sound(self.hit_sound)


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()