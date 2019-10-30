import arcade


WIDTH = 640
HEIGHT = 480

window = arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")


def setup():
    arcade.set_background_color(arcade.color.GRAY)
    arcade.schedule(update, 1/60)
    arcade.run()


def update(delta_time):
    pass


@window.event
def on_draw():
    arcade.start_render()
    # Draw in here...
    arcade.draw_ellipse_filled(260, 200, 80, 100, arcade.color.YELLOW_ORANGE)
    arcade.draw_ellipse_filled(280, 200, 80, 100, arcade.color.YELLOW_ORANGE)
    arcade.draw_ellipse_filled(300, 200, 80, 100, arcade.color.YELLOW_ORANGE)
    arcade.draw_ellipse_filled(320, 200, 80, 100, arcade.color.YELLOW_ORANGE)
    arcade.draw_ellipse_filled(340, 200, 80, 100, arcade.color.YELLOW_ORANGE)
    arcade.draw_ellipse_filled(360, 200, 80, 100, arcade.color.YELLOW_ORANGE)
    arcade.draw_ellipse_filled(380, 200, 80, 100, arcade.color.YELLOW_ORANGE)
    arcade.draw_rectangle_filled(320, 330, 40, 60, arcade.color.COCOA_BROWN)
    # Eyes 
    arcade.draw_triangle_filled(300, 260, 320, 285, 340, 260, arcade.color.BLACK )
    arcade.draw_triangle_filled(380, 260, 400, 285, 420, 260, arcade.color.BLACK )

    #Nose 
    arcade.draw_triangle_filled(345, 230, 365, 205, 385, 230, arcade.color.BLACK )

    # Mouth 
    arcade.draw_arc_filled(365, 150, 50, 50, arcade.color.BLACK, 0, 180, 360, 128)

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
