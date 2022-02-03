import arcade

arcade.open_window(800, 600, 'RAINING ON A SUN SET')


arcade.set_background_color(arcade.color.CADET)

arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.csscolor.BURLYWOOD)

# MAKING THE RIVER
arcade.draw_arc_filled(280, 180, 780, 70, arcade.color.AQUA, 0, 180)

# DRAWING THE SUN
arcade.draw_arc_filled(400, 600, 400, 400, arcade.color.SUNSET_ORANGE, 0, 360)

# DRAWING THE TREES
arcade.draw_rectangle_filled(120, 100, 20, 170, arcade.color.ASH_GREY)

arcade.draw_arc_filled(121, 130, 70, 220, arcade.color.AO, 0, 180)

arcade.draw_rectangle_filled(400, 200, 20, 170, arcade.color.ASH_GREY)

arcade.draw_arc_filled(401, 230, 70, 220, arcade.color.AO, 0, 180)

arcade.draw_rectangle_filled(600, 120, 20, 170, arcade.color.ASH_GREY)

arcade.draw_arc_filled(601, 160, 70, 220, arcade.color.AO, 0, 180)

arcade.draw_rectangle_filled(740, 230, 20, 100, arcade.color.ASH_GREY)

arcade.draw_arc_filled(741, 240, 70, 200, arcade.color.AO, 0, 180)

# DRAWING THE CLAUD
arcade.draw_arc_filled(90, 400, 200, 100, arcade.color.ALICE_BLUE, 0, 180)

# DRAWING THE RAIN
arcade.draw_rectangle_filled(35, 380, 5, 20, arcade.color.AQUA)

arcade.draw_rectangle_filled(10, 350, 5, 20, arcade.color.AQUA)

arcade.draw_rectangle_filled(40, 340, 5, 20, arcade.color.AQUA)

arcade.draw_rectangle_filled(85, 360, 5, 20, arcade.color.AQUA)

arcade.draw_rectangle_filled(110, 350, 5, 20, arcade.color.AQUA)

arcade.draw_rectangle_filled(25, 320, 5, 20, arcade.color.AQUA)

arcade.draw_rectangle_filled(65, 350, 5, 20, arcade.color.AQUA)

arcade.draw_rectangle_filled(135, 300, 5, 20, arcade.color.AQUA)

arcade.draw_rectangle_filled(45, 310, 5, 20, arcade.color.AQUA)

arcade.draw_rectangle_filled(180, 345, 5, 20, arcade.color.AQUA)


arcade.finish_render()

arcade.run()
