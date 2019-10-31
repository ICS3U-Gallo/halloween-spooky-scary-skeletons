import arcade


WIDTH = 640
HEIGHT = 480

window = arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")


def setup():
    arcade.set_background_color(arcade.color.SMOKY_BLACK)
    arcade.schedule(update, 1/60)
    arcade.run()


def update(delta_time):
    pass


@window.event
def on_draw():
    arcade.start_render()
    # Draw in here...

    #shelf
    arcade.draw_rectangle_filled(150, 300, 200, 300, arcade.color.DARK_BROWN, 0)
    arcade.draw_rectangle_filled(150, 370, 10, 200, arcade.color.LIGHT_BROWN, 90)
    arcade.draw_rectangle_filled(150, 300, 10, 200, arcade.color.LIGHT_BROWN, 90)

    #books
    arcade.draw_rectangle_filled(70, 400, 25, 50, arcade.color.GREEN, 0)
    arcade.draw_rectangle_filled(100, 400, 25, 50, arcade.color.GREEN_YELLOW, 0)
    arcade.draw_rectangle_filled(130, 400, 25, 50, arcade.color.PURPLE, 0)
    arcade.draw_rectangle_filled(160, 400, 25, 50, arcade.color.BLUE, 0)
    arcade.draw_rectangle_filled(190, 400, 25, 50, arcade.color.ASH_GREY, 0)

    arcade.draw_rectangle_filled(70, 330, 25, 50, arcade.color.GREEN_YELLOW, 0)
    arcade.draw_rectangle_filled(100, 330, 25, 50, arcade.color.PURPLE, 0)
    arcade.draw_rectangle_filled(130, 330, 25, 50, arcade.color.PURPLE, 0)
    arcade.draw_rectangle_filled(160, 330, 25, 50, arcade.color.ASH_GREY, 0)
    arcade.draw_rectangle_filled(220, 330, 25, 50, arcade.color.BLUE, 145)

    # Body of pumpkin
    arcade.draw_rectangle_filled(360, 230, 110, 130, arcade.color.ORANGE)
    arcade.draw_ellipse_filled(300, 225, 150, 100, arcade.color.ORANGE, 90, 60)
    arcade.draw_ellipse_filled(425, 225, 150, 100, arcade.color.ORANGE, 90, 60)

    # Stem of Pumpkin
    arcade.draw_rectangle_filled(360, 320, 20, 50, arcade.color.BROWN)

    # Face of Pumpkin
    # Eyes
    arcade.draw_triangle_filled(300, 260, 320, 285, 340, 260, arcade.color.BLACK)
    arcade.draw_triangle_filled(380, 260, 400, 285, 420, 260, arcade.color.BLACK)

    # Nose
    arcade.draw_triangle_filled(345, 230, 365, 205, 385, 230, arcade.color.BLACK)

    # Mouth
    arcade.draw_arc_filled(364.4, 150, 50, 50, arcade.color.BLACK, 0, 180, 360, 128)

    #ghost
    arcade.draw_ellipse_filled(50, 100, 20, 110, arcade.color.WHITE)
    arcade.draw_ellipse_filled(70, 100, 20, 100, arcade.color.WHITE)
    arcade.draw_ellipse_filled(90, 100, 20, 100, arcade.color.WHITE)
    arcade.draw_ellipse_filled(110, 100, 20, 100, arcade.color.WHITE)
    arcade.draw_ellipse_filled(130, 100, 20, 100, arcade.color.WHITE)
    arcade.draw_ellipse_filled(150, 100, 20, 110, arcade.color.WHITE)
    arcade.draw_circle_filled(100, 190, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(80, 190, 10, arcade.color.BLACK)
    arcade.draw_circle_filled(130, 190, 10, arcade.color.BLACK)
    arcade.draw_ellipse_filled(100, 140, 20, 40, arcade.color.BLACK)

    #blood
    arcade.draw_ellipse_filled(330, 100, 50, 300, arcade.color.RED_DEVIL, 90)
    arcade.draw_rectangle_filled(330, 100, 5, 50, arcade.color.WHITE_SMOKE, 65)
    arcade.draw_rectangle_filled(400, 100, 5, 35, arcade.color.WHITE_SMOKE, 20)

    #Banner
    arcade.draw_rectangle_filled(430, 400, 350, 100, arcade.color.ORANGE_RED, 0)
    arcade.draw_text("HAPPY GALLOWEEEEN", 290, 380, arcade.color.WHITE, 25)
    arcade.draw_rectangle_outline(430, 400, 350, 100, arcade.color.BLACK, 10)

    # Balloon strings
    arcade.draw_rectangle_filled(550, 150, 2, 350, arcade.color.WHITE)
    arcade.draw_ellipse_filled(550, 275, 125, 100, arcade.color.FERRARI_RED, 90)
@window.event
def on_key_press(key, modifiers):
    pass


@window.event
def on_key_release(key, modifiers):
    pass


@window.event
def on_mouse_press(x, y, button, modifiers):
    pass


if __name__ == '__main__':
    setup()
