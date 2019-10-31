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
    # Draw in here...

    #shelf
    arcade.draw_rectangle_filled(300, 300, 200, 300, arcade.color.DARK_BROWN, 0)
    arcade.draw_rectangle_filled(300, 370, 10, 200, arcade.color.LIGHT_BROWN, 90)
    arcade.draw_rectangle_filled(300, 300, 10, 200, arcade.color.LIGHT_BROWN, 90)

    #books
    arcade.draw_rectangle_filled(230, 400, 25, 50, arcade.color.GREEN, 0)
    arcade.draw_rectangle_filled(260, 400, 25, 50, arcade.color.GREEN_YELLOW, 0)
    arcade.draw_rectangle_filled(290, 400, 25, 50, arcade.color.PURPLE, 0)
    arcade.draw_rectangle_filled(320, 400, 25, 50, arcade.color.BLUE, 0)
    arcade.draw_rectangle_filled(350, 400, 25, 50, arcade.color.ASH_GREY, 0)

    arcade.draw_rectangle_filled(230, 330, 25, 50, arcade.color.GREEN_YELLOW, 0)
    arcade.draw_rectangle_filled(260, 330, 25, 50, arcade.color.PURPLE, 0)
    arcade.draw_rectangle_filled(290, 330, 25, 50, arcade.color.PURPLE, 0)
    arcade.draw_rectangle_filled(320, 330, 25, 50, arcade.color.ASH_GREY, 0)
    arcade.draw_rectangle_filled(370, 330, 25, 50, arcade.color.BLUE, 145)



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
