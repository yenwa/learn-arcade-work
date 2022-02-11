import arcade

def land():
    # making the land
    arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.csscolor.BURLYWOOD)

def clouds(x, y):
    arcade.draw_point(x, y, arcade.color.CADET, 6)
    # making clouds
    arcade.draw_arc_filled(0 + x, 0 + y, 200, 100, arcade.color.ALICE_BLUE, 0, 180)

def rain(x, y):
    arcade.draw_point(x, y, arcade.color.RED, 5)
    # draw rain
    arcade.draw_rectangle_filled(0 + x, 0 + y, 5, 20, arcade.color.AQUA)

def rain_pond(x,y):
    arcade.draw_point(x, y, arcade.color.BURLYWOOD, 5)
    # MAKING THE pond
    arcade.draw_arc_filled(0 + x, 0 + y, 200, 70, arcade.color.AQUA, 0, 360)

def tree(x,y):
    arcade.draw_point(x, y, arcade.color.BURLYWOOD, 6)
    # DRAWING TREE
    arcade.draw_rectangle_filled(120 + x, 100 + y, 20, 170, arcade.color.ASH_GREY)

    arcade.draw_arc_filled(121 + x, 130 + y, 70, 220, arcade.color.AO, 0, 180)

def main():
    arcade.open_window(800, 600, 'DRAWING WITH FUNCTION')

    arcade.set_background_color(arcade.color.CADET)

    arcade.start_render()

    land()
    # cloud_1
    clouds(200, 400)
    # cloud_2
    clouds(530, 320)
    # cloud_3
    clouds(440, 480)
    # cloud_1 rain
    rain(200, 370)
    rain(200, 300)
    rain(120, 370)
    rain(150, 310)
    rain(180, 350)
    rain(110, 360)
    rain(135, 280)
    rain(156, 170)
    rain(175, 295)
    rain(130, 270)
    rain(230, 320)
    rain(250, 300)

    # cloud_2 rain
    rain(580, 260)
    rain(520, 120)
    rain(490, 200)
    rain(570, 220)
    rain(610, 180)
    rain(320, 125)
    rain(400, 280)
    rain(500, 210)
    rain(156, 170)
    rain(175, 295)
    rain(130, 270)
    rain(230, 320)
    rain(250, 300)
# cloud_3 rain
    rain(420, 400)
    rain(390, 410)
    rain(480, 460)
    rain(360, 420)
    rain(350, 350)
    rain(500, 420)
    rain(490, 280)
    rain(390, 170)
    rain(450, 295)
    rain(360, 270)
    rain(415, 320)
    rain(370, 450)

# pond_1
    rain_pond(159, 95)

    # pond_2
    rain_pond(460, 150)

# first_tree
    tree(100, 25)

    # second_tree
    tree(600, 30)

    arcade.finish_render()

    arcade.run()



# calling mail function
main()
