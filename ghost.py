import arcade


WIDTH = 640
HEIGHT = 480

window = arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")


def setup():
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(update, 1/60)
    arcade.run()


def update(delta_time):
    pass


@window.event
def on_draw():
    arcade.start_render()
    # Draw in here...
    arcade.draw_ellipse_filled(260, 200, 20, 110, arcade.color.WHITE)
    arcade.draw_ellipse_filled(280, 200, 20, 100, arcade.color.WHITE)
    arcade.draw_ellipse_filled(300, 200, 20, 100, arcade.color.WHITE)
    arcade.draw_ellipse_filled(320, 200, 20, 100, arcade.color.WHITE)
    arcade.draw_ellipse_filled(340, 200, 20, 100, arcade.color.WHITE)
    arcade.draw_ellipse_filled(360, 200, 20, 110, arcade.color.WHITE)
    arcade.draw_circle_filled(310, 290, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(280, 290, 10, arcade.color.BLACK)
    arcade.draw_circle_filled(340, 290, 10, arcade.color.BLACK)
    arcade.draw_ellipse_filled(310, 240, 20, 40, arcade.color.BLACK)




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
