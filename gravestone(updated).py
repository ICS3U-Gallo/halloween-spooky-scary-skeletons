import arcade


WIDTH = 640
HEIGHT = 480
X1 = WIDTH // 2 - 57
Y1 = HEIGHT // 2 - 50



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
    arcade.draw_text("R.I.P.", X1, Y1, arcade.color.BLACK, 50)
    
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
