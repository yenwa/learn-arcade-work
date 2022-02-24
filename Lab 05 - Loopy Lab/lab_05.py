import arcade
COLUMN_SPACING = 10
ROW_SPACING = 10
LEFT_MARGIN = 6
BOTTOM_MARGIN = 6

def draw_section_outlines():
    # Drawing squares on bottom
    arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, arcade.color.BLACK)

    # Drawing squares on top
    arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLACK)


def draw_section_1():
    for row in range(30):
        for column in range(30):
            x = COLUMN_SPACING * column + LEFT_MARGIN
            y = ROW_SPACING * row + BOTTOM_MARGIN
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_2():
    for row in range(30):
        for column in range (30):
            if column % 2 == 0:
                x = column * COLUMN_SPACING + LEFT_MARGIN + 300

                y = row * ROW_SPACING + BOTTOM_MARGIN

                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            else:
                x = column * COLUMN_SPACING + LEFT_MARGIN + 300

                y = row * ROW_SPACING + BOTTOM_MARGIN

                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)




def draw_section_3():
    for row in range(30):
        for column in range (30):
            if row % 2 == 0:
             x = column * COLUMN_SPACING + LEFT_MARGIN + 600
             y = row * ROW_SPACING + BOTTOM_MARGIN

             arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            else:
                x = column * COLUMN_SPACING + LEFT_MARGIN + 600
                y = row * ROW_SPACING + BOTTOM_MARGIN
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)




def draw_section_4():
    for row in range(30):
        for column in range (30):
            if column % 2 and row % 2 == 0:
             x = column * COLUMN_SPACING + LEFT_MARGIN + 900
             y = row * ROW_SPACING + BOTTOM_MARGIN
             arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            else:
                x = column * COLUMN_SPACING + LEFT_MARGIN + 900
                y = row * ROW_SPACING + BOTTOM_MARGIN
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)



def draw_section_5():
    for column in range(30):
        for row in range(column):
            x = column * COLUMN_SPACING + LEFT_MARGIN
            y = row * ROW_SPACING + BOTTOM_MARGIN + 300
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_6():
    for row in range(30):
        for column in range(30 - row):
            x = column * COLUMN_SPACING + LEFT_MARGIN + 300
            y = row * ROW_SPACING + BOTTOM_MARGIN + 300
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)



def draw_section_7():
    for row in range(30):
        for column in range(row + 1):
            x = column * COLUMN_SPACING + LEFT_MARGIN + 600
            y = row * ROW_SPACING + BOTTOM_MARGIN + 300
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_8():
    for row in range(30):
        for column in range(row + 1):
            column = 29 - column
            x = column * COLUMN_SPACING + LEFT_MARGIN + 900
            y = row * ROW_SPACING + BOTTOM_MARGIN + 300
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)



def main():
    # Window creation
    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    # outline drawing
    draw_section_outlines()

    # section drawing
    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()

    arcade.finish_render()

    arcade.run()


main()
