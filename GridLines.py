from manim import *

config.frame_height = 16
config.frame_width = 9

config.pixel_height = 1280
config.pixel_width = 720

FRAME_WIDTH = config["frame_x_radius"] * 2
FRAME_HEIGHT = config["frame_y_radius"] * 2
    
class GridLines(Scene):
    def construct(self):
        self.add(
            NumberPlane(
                x_length= config["frame_x_radius"] * 2,
                y_length= config["frame_y_radius"] * 2,
                x_range= [0, 30, 1],
                y_range= [0, 30, 1]
            ).set_color(BLACK)
        )
        time = ValueTracker(0)
        def time_updater(dt):
            time.increment_value(dt)
        self.add_updater(time_updater)

        x_dots = list()
        x_lines = list()
        y_dots = list()
        y_lines = list()
        for i in range(30):
            x_dots.append(
                Dot().scale(0.5).add_updater(lambda mobj, i= i : mobj.move_to( self.mobjects[0].c2p(time.get_value(), i, 0)) )
            )
            x_lines.append(
                always_redraw(lambda i=i : Line(start= self.mobjects[0].c2p(0,i,0), end= x_dots[i].get_center() ))
            )
            y_dots.append(
                Dot().scale(0.5).add_updater(lambda mobj, i= i : mobj.move_to( self.mobjects[0].c2p(i, time.get_value(), 0)) )
            )
            y_lines.append(
                always_redraw(lambda i=i : Line(start= self.mobjects[0].c2p(i,0,0), end= y_dots[i].get_center() ))
            )
        self.add(VGroup(*x_dots), VGroup(*x_lines), VGroup(*y_dots), VGroup(*y_lines))
        self.wait(30)
