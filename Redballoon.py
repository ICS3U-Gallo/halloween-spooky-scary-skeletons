import arcade


WIDTH = 640
HEIGHT = 480
X1 = WIDTH // 2
Y1 = HEIGHT // 2

window = arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")


def setup():
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)
    arcade.run()


def update(delta_time):
    pass


@window.event
def on_draw():
    arcade.start_render()
# Balloon strings
    arcade.draw_line(X1, Y1, X1, Y1 - 175, arcade.color.BLACK, 5)
    arcade.draw_ellipse_filled(X1, 275, 125, 100, arcade.color.FERRARI_RED, 90)

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

