import arcade


WIDTH = 640
HEIGHT = 480
X1 = WIDTH - 400
Y1 = HEIGHT // 2 - 20
X2 = X1 + 75
Y2 = Y1
X3 = X2 + 25
Y3 = Y2

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
# Gravestone
    arcade.draw_rectangle_filled(WIDTH // 2, HEIGHT // 4, WIDTH // 3 - 13, (HEIGHT + 20) // 2, arcade.color.LIGHT_GRAY,180)
    arcade.draw_ellipse_filled(WIDTH // 2, HEIGHT // 2 - 10, 200, 200, arcade.color.LIGHT_GRAY, 180, 120)
# Cross
    arcade.draw_rectangle_filled(WIDTH // 2, HEIGHT - 90, 20, 120, arcade.color.GRAY, 0)
    arcade.draw_rectangle_filled(WIDTH // 2, HEIGHT - 80, 20, 80, arcade.color.GRAY, 90)
# RIP
    # R
    arcade.draw_line(X1, Y1, X1, Y1 - 100, arcade.color.BLACK, 5)
    arcade.draw_line(X1, Y1, X1 + 50, Y1, arcade.color.BLACK, 5)
    arcade.draw_line(X1 + 50, Y1, X1 + 50, Y1 - 40, arcade.color.BLACK, 5)
    arcade.draw_line(X1, Y1 - 40, X1 + 50, Y1 - 40, arcade.color.BLACK, 5)
    arcade.draw_line(X1, Y1 - 40, X1 + 50, Y1 - 100, arcade.color.BLACK, 5)

    # I
    arcade.draw_line(X2, Y2, X2, Y2 - 100, arcade.color.BLACK, 5)

    # P
    arcade.draw_line(X3, Y3, X3, Y3 - 100, arcade.color.BLACK, 5)
    arcade.draw_line(X3, Y3, X3 + 50, Y3, arcade.color.BLACK, 5)
    arcade.draw_line(X3 + 50, Y3, X3 + 50, Y3 - 40, arcade.color.BLACK, 5)
    arcade.draw_line(X3, Y3 - 40, X3 + 50, Y3 - 40, arcade.color.BLACK, 5)
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
