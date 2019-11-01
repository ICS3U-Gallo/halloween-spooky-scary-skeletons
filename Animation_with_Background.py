import arcade
import pymunk
import random
import math

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Candle Man"

press_num = 0
updownspd = 1.5

#Pymunk
pcs_num = 16
pcs_coords = []
pcs_list = []
pcs_size = 45

#Pymunk Space
space = pymunk.Space()
space.gravity = 0, -1000

#Exploding Pumpkin
physics_calc = False
exploded = False

#Floor
floor = pymunk.Segment(space.static_body, (0 , 0), (1000, 0), 20)
floor.elasticity = 0.8
floor.friction = 0.7
space.add(floor)

def tri_ang(startpointx, startpointy, angle, xlen, height):
    angle = math.radians(angle)
    startpointy += 4

    x1 = height * math.sin(angle) + startpointx
    y1 = height * math.cos(angle) + startpointy

    x2 = (xlen / 2) * math.sin(angle + 90) + startpointx
    y2 = (xlen / 2) * math.cos(angle + 90) + startpointy

    x3 = (xlen / 2) * math.sin(angle - 90) + startpointx
    y3 = (xlen / 2) * math.cos(angle - 90) + startpointy

    return x1, y1, x2, y2, x3, y3

def location_lister(x, y, space, height, size):
    xrand = random.randint(x - space/2 + size, x + space/2 - size)
    yrand = random.randint(y - height/2 + size, y + height/2 - size)
    return xrand, yrand


#Class PhysicsPieces
class Piece:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        global pcs_size

        arcade.draw_ellipse_filled(self.x, self.y, pcs_size, pcs_size, (255-(press_num*20), 85-(press_num*20), 0))

    def move(self, a, b):

        self.x = a
        self.y = b

class Candles:
    def __init__(self, x, y, truex, truey, scale, tallness, rnum, yspd, baseyincr, up):
        self.x = x
        self.y = y
        self.truex = truex
        self.truey = truey
        self.scale = scale
        self.tallness = tallness
        self.rnum  = rnum
        self.yspd = yspd
        self.baseyincr = baseyincr
        self.up = up

    def display(self):
        arcade.draw_rectangle_filled(self.x, self.y, 10 * self.scale, 30 * self.scale, (255, 255, 255), 0)
        arcade.draw_rectangle_filled(self.x, self.y + 30 + 3*self.scale, 2 * self.scale, 6 * self.scale, (100, 100, 100), 0)
        arg_holder = []
        arg_holder2 = []
        for i in range(6):
            arg_holder.append(tri_ang(self.x, self.y + (30 * self.scale)/2 + 6 * self.scale, 180, 20, 5)[i])
        arcade.draw_triangle_filled(arg_holder[0], arg_holder[1], arg_holder[2], arg_holder[3], arg_holder[4], arg_holder[5], (226, 88, 34))
        for i in range(6):
            arg_holder2.append(tri_ang(self.x, self.y + (30 * self.scale)/2 + 6 * self.scale + 8, 0, 20, 30)[i])
        arcade.draw_triangle_filled(arg_holder2[0], arg_holder2[1], arg_holder2[2], arg_holder2[3], arg_holder2[4], arg_holder2[5], (226, 88, 34))

    def move(self):

        topmost = self.truey + (self.rnum / 2)
        botmost = self.truey - (self.rnum / 2)
        intychange = 0.01 * self.yspd

        if self.baseyincr <= 0:
            self.up = not self.up
            self.baseyincr = updownspd

        if self.up is True and self.y < topmost:
            self.y += self.baseyincr
        if self.up is True and self.y >= topmost and self.baseyincr != 0:
            self.y += self.baseyincr
            self.baseyincr -= intychange
        if self.up is False and self.y > botmost:
            self.y -= self.baseyincr
        if self.up is False and self.y <= botmost and self.baseyincr != 0:
            self.y -= self.baseyincr
            self.baseyincr -= intychange


class Bossman:
    def __init__(self, x, y, truex, truey, scale, wideness, tallness, rnum, yspd, baseyincr, up, space):
        global updownspd
        self.x = x
        self.y = y
        self.truex = truex
        self.truey = truey
        self.scale = scale
        self.wideness = wideness
        self.tallness = tallness
        self.rnum = rnum
        self.yspd = yspd
        self.baseyincr = baseyincr
        self.up = up
        self.space = space

    def display(self):
        global press_num

        recth = 15 * self.scale

        arcade.draw_rectangle_filled(self.x, self.y + (90 * self.scale + self.tallness) / 2 + recth / 2, 7 * self.scale, recth, (83, 212, 36))
        for i in range(4):
            space = -(i*13.3*self.scale*self.space)
            arcade.draw_ellipse_filled(self.x-10+space+i*3, self.y, 35*self.scale+self.wideness, 100*self.scale+self.tallness-(i*10), (255-(press_num*20), 85-(press_num*20), 0))
        for i in range(4):
            space = i*13.3*self.scale*self.space
            arcade.draw_ellipse_filled(self.x+10+space-i*3, self.y, 35*self.scale+self.wideness, 100*self.scale+self.tallness-(i*10), (255-(press_num*20), 85-(press_num*20), 0))
        arcade.draw_ellipse_filled(self.x, self.y, 50 * self.scale + self.wideness, 100 * self.scale + self.tallness, (255-(press_num*20), 85-(press_num*20), 0))

        #Outer triangle
        arcade.draw_triangle_filled(self.x + 15 * self.scale, self.y + 5 * self.scale, self.x + 45 * self.scale, self.y + 5 * self.scale, self.x + 30 * self.scale, self.y + 15 * self.scale, (0, 0, 0))
        arcade.draw_triangle_filled(self.x - 15 * self.scale, self.y + 5 * self.scale, self.x - 45 * self.scale, self.y + 5 * self.scale, self.x - 30 * self.scale, self.y + 15 * self.scale, (0, 0, 0))
        #Inner triangle
        arcade.draw_triangle_filled(self.x + 20 * self.scale, self.y + 7 * self.scale, self.x + 40 * self.scale, self.y + 7 * self.scale, self.x + 30 * self.scale, self.y + 13 * self.scale, (255, 153, 51))
        arcade.draw_triangle_filled(self.x - 20 * self.scale, self.y + 7 * self.scale, self.x - 40 * self.scale, self.y + 7 * self.scale, self.x - 30 * self.scale, self.y + 13 * self.scale, (255, 153, 51))
        #Mouth
        arcade.draw_triangle_filled(self.x, self.y - 30 * self.scale, self.x - 20 * self.scale, self.y - 20 * self.scale, self.x + 20 * self.scale, self.y - 20 * self.scale, (0, 0, 0))
        arcade.draw_triangle_filled(self.x, self.y - 28 * self.scale, self.x - 14 * self.scale, self.y - 22 * self.scale, self.x + 14 * self.scale, self.y - 22 * self.scale, (255, 153, 51))

    def move(self):

        topmost = self.truey + (self.rnum/2)
        botmost = self.truey - (self.rnum/2)
        intychange = 0.01*self.yspd

        if self.baseyincr <= 0:
            self.up = not self.up
            self.baseyincr = updownspd

        if self.up is True and self.y < topmost:
            self.y += self.baseyincr
        if self.up is True and self.y >= topmost and self.baseyincr != 0:
            self.y += self.baseyincr
            self.baseyincr -= intychange
        if self.up is False and self.y > botmost:
            self.y -= self.baseyincr
        if self.up is False and self.y <= botmost and self.baseyincr != 0:
            self.y -= self.baseyincr
            self.baseyincr -= intychange


class Mouse:
    def __init__(self, x, y):
        global mouse_loc

        self.x = x
        self.y = y

    def display_loc(self):

        arcade.draw_ellipse_filled(self.x, self.y, 10, 10, (255,255,255))


colorlist = [arcade.color.GREEN_YELLOW, arcade.color.PURPLE, arcade.color.PURPLE, arcade.color.ASH_GREY, arcade.color.BLUE]

class MyGame(arcade.Window):
    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        self.set_update_rate(1 / 100)

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BLACK)

        self.pumpkin = Bossman(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 2, 0, 0, 40, 20, updownspd, True, 0.85)
        self.mouse = Mouse(300, 300)
        self.candle = Candles(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 2, 0, 40, 20, updownspd, True)

        self.shapes = arcade.ShapeElementList()
        shape = arcade.create_ellipse_filled_with_colors(self.candle.x, self.candle.y + (30 * self.candle.scale)/2 + 6 * self.candle.scale + 14, 90, 90, inside_color=(255, 153, 51), outside_color=(0,0,0))
        self.shapes.append(shape)

    def on_mouse_release(self, x, y, button, modifiers):
        global press_num, physics_calc
        loc = [self.pumpkin.x, self.pumpkin.y]
        mouse_loc = [self.mouse.x, self.mouse.y]
        space = 8*13.3*self.pumpkin.scale
        height = 100*self.pumpkin.scale

        if button == arcade.MOUSE_BUTTON_LEFT and loc[0] + space/2 > mouse_loc[0] and loc[0] - space/2 < mouse_loc[0] and loc[1] + height/2 > mouse_loc[1] and loc[1] - height/2 < mouse_loc[1]:
            press_num += 1
            if press_num == 3:
                physics_calc = True

    def on_update(self, delta_time):
        global press_num, physics_calc
        space.step(delta_time)

        if press_num == 3 and physics_calc is True:
            for i in range(pcs_num):
                circle_moment = pymunk.moment_for_circle(1, 0, pcs_size/2)
                circle_body = pymunk.Body(1, circle_moment)
                circle_body.position = location_lister(int(self.pumpkin.x), int(self.pumpkin.y), int(8 * 13.3 * self.pumpkin.scale), int(100 * self.pumpkin.scale), pcs_size)[0], location_lister(int(self.pumpkin.x), int(self.pumpkin.y), int(8 * 13.3 * self.pumpkin.scale), int(100 * self.pumpkin.scale), pcs_size)[1]
                circle_shape = pymunk.Circle(circle_body, pcs_size/2)
                circle_shape.elasticity = 0.4
                circle_shape.friction = 0.7
                space.add(circle_body, circle_shape)
                pcs_coords.append(circle_body)

        if press_num == 3:
            for i in range(pcs_num):
                pcs_list.append(Piece(pcs_coords[i].position.x, pcs_coords[i].position.y))
            for body in space.bodies:
                if body.position.y < -30 or body.position.y > 630 or body.position.x > 1030 or body.position.x < -30:
                    space.remove(body, body.shapes)

    def on_mouse_motion(self, x, y, dx, dy):
        self.mouse.x = x
        self.mouse.y = y

    def on_draw(self):
        global physics_calc, exploded
        arcade.start_render()

        # shelf done
        arcade.draw_rectangle_filled(150, 300, 300, 350, arcade.color.DARK_BROWN, 0)
        arcade.draw_rectangle_filled(150, 370, 10, 300, arcade.color.LIGHT_BROWN, 90)
        arcade.draw_rectangle_filled(150, 300, 10, 300, arcade.color.LIGHT_BROWN, 90)

        # books
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

        # ghost
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

        # blood
        arcade.draw_ellipse_filled(500, 80, 100, 500, arcade.color.RED_DEVIL, 90)
        arcade.draw_rectangle_filled(330, 100, 5, 50, arcade.color.WHITE_SMOKE, 65)
        arcade.draw_rectangle_filled(400, 100, 5, 35, arcade.color.WHITE_SMOKE, 20)

        # Banner
        arcade.draw_rectangle_filled(SCREEN_WIDTH // 2, 530, 800, 100, arcade.color.ORANGE_RED, 0)
        arcade.draw_text("HAPPY GALLOWEEEEN", 170, 500, arcade.color.WHITE, 50)

        # Balloon strings
        arcade.draw_rectangle_filled(800, 150, 2, 500, arcade.color.WHITE)
        arcade.draw_ellipse_filled(800, 350, 200, 150, arcade.color.FERRARI_RED, 90)

        if exploded is False:
            self.pumpkin.display()
            self.pumpkin.move()

        if exploded is True:
            self.shapes.draw()
            self.candle.display()
            self.candle.move()
            if self.candle.up == True:
                self.shapes.move(0, self.candle.baseyincr)
            if self.candle.up == False:
                self.shapes.move(0,-self.candle.baseyincr)

        self.mouse.display_loc()

        if press_num == 3:
            for i in range(pcs_num):
                pcs_list[i].display()
                pcs_list[i].move(pcs_coords[i].position.x, pcs_coords[i].position.y)
                physics_calc = False
                exploded = True

        arcade.draw_lines([floor.a, floor.b], arcade.color.TROLLEY_GREY, 40)


def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()
