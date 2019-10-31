import arcade


WIDTH = 640
HEIGHT = 480

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
    arcade.draw_rectangle_filled(WIDTH // 2, 350, 600, 100, arcade.color.ORANGE_RED, 0)
    arcade.draw_text("HAPPY GALLOWEEEEN", 40, 325, arcade.color.WHITE, 50)
    arcade.draw_rectangle_outline(WIDTH // 2, 350, 600, 100, arcade.color.BLACK, 10)
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
