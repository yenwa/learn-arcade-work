
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3


class Ball:
    """ This class manages a ball bouncing on the screen. """

    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        """ Constructor. """

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        # Edge hit sound
        self.hit_sound = arcade.load_sound('hit.wav')

        if self.position_x < self.radius:
            self.position_x = self.radius
            arcade.play_sound(self.hit_sound)



        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius
            arcade.play_sound(self.hit_sound)

        if self.position_y < self.radius:
            self.position_y = self.radius
            arcade.play_sound(self.hit_sound)

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius
            arcade.play_sound(self.hit_sound)



class MyGame(arcade.Window):

    def __init__(self):

        # Call the parent class's init function
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "flip-cart")
        self.background = arcade.load_texture('background.png')


        # Create a list for the balls

        self.ball = Ball(20, 50, 3, 3, 15, arcade.color.BRIGHT_PINK)

        #self.ball_1 = Ball(50, 70, 2, 4, 16, arcade.color.GO_GREEN)




        self.set_mouse_visible(False)



    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        arcade.draw_texture_rectangle(400, 300,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.ball.draw()
        #self.ball_1.draw()

    def update(self, delta_time):
            self.ball.update()
            #self.ball_1.update()

   # define keyboard input

    def on_key_press(self, key, modifiers):
        self.up_sound = arcade.load_sound('up_sound.wav')
        self.left_sound = arcade.load_sound('go_left_sound.wav')
        self.right_sound = arcade.load_sound('go_right.wav')
        self.down_sound = arcade.load_sound('down_sound.wav')
        self.mouse_press_left = arcade.load_sound('mouse_p1.wav')
        self.mouse_press_right = arcade.load_sound('mouse_p2.wav')


        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.ball.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ball.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.ball.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ball.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.change_y = 0
        if key == arcade.key.UP:
            arcade.play_sound(self.up_sound)
        if key == arcade.key.LEFT:
            arcade.play_sound(self.left_sound)
        if key == arcade.key.RIGHT:
            arcade.play_sound(self.right_sound)
        if key == arcade.key.DOWN:
            arcade.play_sound(self.down_sound)

    #def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        #self.ball_1.position_x = x
        #self.ball_1.position_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        """ Called when the user presses a mouse button. """
        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(self.mouse_press_left)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            arcade.play_sound(self.mouse_press_right)



def main():
    window = MyGame()

    arcade.run()


main()
