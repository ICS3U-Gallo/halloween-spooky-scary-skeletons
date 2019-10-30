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
# Gravestone
    arcade.draw_rectangle_filled(WIDTH // 2, HEIGHT // 4, 200, 250, arcade.color.LIGHT_GRAY, 180)
    arcade.draw_ellipse_filled(WIDTH // 2, 230, 100, 100, arcade.color.LIGHT_GRAY, 180, 120)
# Cross
    arcade.draw_rectangle_filled(WIDTH // 2, 390, 20, 120, arcade.color.GRAY, 0)
    arcade.draw_rectangle_filled(WIDTH // 2, 400, 20, 80, arcade.color.GRAY, 90)
# RIP 
    # R
    arcade.draw_line(240, 220, 240, 120, arcade.color.BLACK, 1)
    arcade.draw_line(240, 220, 290, 220, arcade.color.BLACK, 1)
    arcade.draw_line(290, 220, 290, 180, arcade.color.BLACK, 1)
    arcade.draw_line(240, 180, 290, 180, arcade.color.BLACK, 1)
    arcade.draw_line(240, 180, 290, 120, arcade.color.BLACK, 1)

    # I
    arcade.draw_line(315, 220, 315, 120, arcade.color.BLACK, 1 )

    # P 
    arcade.draw_line(340, 220, 340, 120, arcade.color.BLACK, 1)
    arcade.draw_line(340, 220, 390, 220, arcade.color.BLACK, 1)
    arcade.draw_line(390, 220, 390, 180, arcade.color.BLACK, 1)
    arcade.draw_line(340, 180, 390, 180, arcade.color.BLACK, 1)
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
