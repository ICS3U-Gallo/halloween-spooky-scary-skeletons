import arcade


WIDTH = 900
HEIGHT = 600

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

    #shelf done
    arcade.draw_rectangle_filled(150, 300, 300, 350, arcade.color.DARK_BROWN, 0)
    arcade.draw_rectangle_filled(150, 370, 10, 300, arcade.color.LIGHT_BROWN, 90)
    arcade.draw_rectangle_filled(150, 300, 10, 300, arcade.color.LIGHT_BROWN, 90)

    #books
    arcade.draw_rectangle_filled(20, 400, 25, 50, arcade.color.GREEN, 0)
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
    arcade.draw_rectangle_filled(530, 250, 150, 170, arcade.color.ORANGE)
    arcade.draw_ellipse_filled(450, 249, 175, 100, arcade.color.ORANGE, 90, 60)
    arcade.draw_ellipse_filled(600, 249, 175, 100, arcade.color.ORANGE, 90, 60)

    # Stem of Pumpkin
    arcade.draw_rectangle_filled(520, 360, 20, 50, arcade.color.BROWN)

    # Face of Pumpkin
    # Eyes
    arcade.draw_triangle_filled(460, 290, 480, 315, 500, 290, arcade.color.BLACK)
    arcade.draw_triangle_filled(540, 290, 560, 315, 580, 290, arcade.color.BLACK)

    # Nose
    arcade.draw_triangle_filled(500, 265, 520, 240, 540, 265, arcade.color.BLACK)

    # Mouth
    arcade.draw_arc_filled(520, 180, 50, 50, arcade.color.BLACK, 0, 180, 360, 128)

    #ghost
    arcade.draw_ellipse_filled(50, 100, 30, 110, arcade.color.WHITE)
    arcade.draw_ellipse_filled(70, 100, 30, 100, arcade.color.WHITE)
    arcade.draw_ellipse_filled(90, 100, 30, 100, arcade.color.WHITE)
    arcade.draw_ellipse_filled(110, 100, 30, 100, arcade.color.WHITE)
    arcade.draw_ellipse_filled(130, 100, 30, 100, arcade.color.WHITE)
    arcade.draw_ellipse_filled(150, 100, 30, 110, arcade.color.WHITE)
    arcade.draw_circle_filled(100, 190, 80, arcade.color.WHITE)
    arcade.draw_circle_filled(80, 190, 20, arcade.color.BLACK)
    arcade.draw_circle_filled(130, 190, 20, arcade.color.BLACK)
    arcade.draw_ellipse_filled(100, 140, 30, 40, arcade.color.BLACK)

    #blood
    arcade.draw_ellipse_filled(500, 80, 100, 500, arcade.color.RED_DEVIL, 90)
    arcade.draw_rectangle_filled(330, 100, 5, 50, arcade.color.WHITE_SMOKE, 65)
    arcade.draw_rectangle_filled(400, 100, 5, 35, arcade.color.WHITE_SMOKE, 20)

    #Banner
    arcade.draw_rectangle_filled(WIDTH // 2, 530, 800, 100, arcade.color.ORANGE_RED, 0)
    arcade.draw_text("HAPPY GALLOWEEEEN", 170, 500, arcade.color.WHITE, 50)

    # Balloon strings
    arcade.draw_rectangle_filled(800, 150, 2, 500, arcade.color.WHITE)
    arcade.draw_ellipse_filled(800, 350, 200, 150, arcade.color.FERRARI_RED, 90)
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
