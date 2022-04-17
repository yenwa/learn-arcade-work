
import random
import arcade

SPRITE_SCALING = 3

COIN_COUNT = 40

SCALING_COIN = 0.18

BAD_SPRITE_SCALING_COIN = 0.19
BAD_COIN_COUNT = 5


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Flying witch"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 200

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.1

# How fast the character moves
PLAYER_MOVEMENT_SPEED = 7


class Coin_bad(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 18

    def update(self):

        # Move the bad coin
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If we are out-of-bounds, then 'bounce'
        if self.left < 0:
            self.change_x *= -1

        if self.right > 1200:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > 1550:
            self.change_y *= -1


class MyGame(arcade.Window):
    """ Main application class. """
    done = False


    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)


        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.coin_list = None
        self.bad_coin_list = None

        # Score
        self.score = 0

        # Set up the player
        self.player_sprite = None
        self.coin_sprite = None


        self.physics_engine = None

        # Used in scrolling
        self.view_bottom = 0
        self.view_left = 0

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        self.camera_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bad_coin_list = arcade.SpriteList()


        # Set up the player
        " Character from kenney.com"
        self.player_sprite = arcade.Sprite("character_2.gif",
                                           scale=0.1)
        self.player_sprite.center_x = 256
        self.player_sprite.center_y = 512
        self.player_list.append(self.player_sprite)

        # -- Set up several columns of walls
        " wall and block from kenney.com"
        for x in range(200, 1650, 210):
            for y in range(0, 1600, 64):
                # Randomly skip a box so the player can find a way through
                if random.randrange(5) > 0:
                    wall = arcade.Sprite("tile.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y


                    self.wall_list.append(wall)

        for y in (-80, 1560, -80):
            # Loop for each box going across
            for x in range(170, 1470, 50):
                block_wall = arcade.Sprite("block_wall.png",
                                     SPRITE_SCALING)
                block_wall.left = x
                block_wall.bottom = y
                self.wall_list.append(block_wall)


        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0

        # Create the coins
        " coins from kenney.com "
        for i in range(COIN_COUNT):
            # Create the coin instance

            coin = arcade.Sprite('coin_1.png', SCALING_COIN)

            coin_palce_right = False

            while not coin_palce_right:

             # Position the coin

               coin.center_x = random.randrange(1700)
               coin.center_y = random.randrange(1500)

               # check coin and wall collision
               wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)

            # See if the coin is hitting another coin
               coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

               if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:

                  coin_palce_right = True

            # Add the coin to the lists
            self.coin_list.append(coin)

        # create bad coin
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
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        self.clear()

        # Select the camera we'll use to draw all our sprites
        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.coin_list.draw()
        self.bad_coin_list.draw()

        # Select the (unscrolled) camera for our GUI
        self.camera_gui.use()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.BLUE, 14)

        output = f"Coins Left: {COIN_COUNT - self.score + BAD_COIN_COUNT}"
        arcade.draw_text(output, 10, 50, arcade.color.PINK, 14)

        output = f"Welcome to the flying Witch"
        arcade.draw_text(output, 10, 580, arcade.color.AQUA, 14)

        output = f"Use the arrow keys to navigate the witch"
        arcade.draw_text(output, 10, 560, arcade.color.AQUA, 14)

        output = f"Collect all the stable coins"
        arcade.draw_text(output, 10, 540, arcade.color.ORANGE, 14)

        output = f"While avoiding the coins in motion"
        arcade.draw_text(output, 10, 520, arcade.color.RED, 14)

        output = f"GOOD LUCK :)"
        arcade.draw_text(output, 10, 500, arcade.color.GREEN, 14)


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False
    def on_update(self, delta_time):
        """ Movement and game logic """


        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()
        self.coin_list.update()
        self.bad_coin_list.update()




        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in coin_hit_list:
            # remove coin from list
            coin.remove_from_sprite_lists()

            # add score when hit a good coin
            self.score += 1

            # add sound when hit a good coin
            " sound from kenney.com"
            self.collect_coin_sound = arcade.load_sound('collect_coin.wav')

            arcade.play_sound(self.collect_coin_sound)

        bad_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bad_coin_list)

        for bad_coin in bad_hit_list:
            # remove coin from list
            bad_coin.remove_from_sprite_lists()

            # remove score when hit a bad coin
            self.score -= 1

            # Add bad hit sound
            " sound from kenney.com"
            self.hit_sound = arcade.load_sound('hit.wav')
            arcade.play_sound(self.hit_sound)




        # Scroll the screen to the player
        self.scroll_to_player()

    def scroll_to_player(self):
        """
        Scroll the window to the player.
        This method will attempt to keep the player at least VIEWPORT_MARGIN
        pixels away from the edge.

        if CAMERA_SPEED is 1, the camera will immediately move to the desired position.
        Anything between 0 and 1 will have the camera move to the location with a smoother
        pan.
        """

        # --- Manage Scrolling ---

        # Scroll left
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left

        # Scroll right
        right_boundary = self.view_left + self.width - VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary

        # Scroll up
        top_boundary = self.view_bottom + self.height - VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary

        # Scroll down
        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom

        # Scroll to the proper location
        position = self.view_left, self.view_bottom
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):
        """
        Resize window
        Handle the user grabbing the edge and resizing the window.
        """
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()