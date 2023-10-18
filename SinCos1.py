from manim import *
from math import *
# from colour import Color

class Test(Scene):
    def construct(self):
        
        axes = []
        axes.append(Axes(x_range= [0,14], y_range= [-2,2], x_length= 10, y_length= 2).add_coordinates(font_size= 15).to_edge(UP))
        for i in range(1,3):
            axes.append(Axes(x_range= [0,14], y_range= [-2,2], x_length= 10, y_length= 2).add_coordinates(font_size= 15).next_to(axes[i-1], DOWN, buff= 0.5))
        self.add(VGroup(*axes))

        # Sin Function in Parametric Form
        sin = ParametricFunction(lambda t: axes[0].c2p(t,np.sin(t)), t_range= [0,14], color= GREEN, stroke_width= 5)
        # Cos Function in Parametric Form
        cos = ParametricFunction(lambda t: axes[1].c2p(t,np.cos(t)), t_range= [0,14], color= RED)
        # Sum of Sin and Cos Function in Parametric Form
        sincos = ParametricFunction(lambda t: axes[2].c2p(t,np.sin(t) + np.cos(t)), t_range= [0,14], color= YELLOW)
        self.add(sin, cos, sincos)

        # Adding text
        MathTex.set_default(font_size= 25) # Set the font size you prefer as default otherwise have to set individually in evey MathTex variable
        function_dis = [MathTex("sin(\Theta)"), MathTex("cos(\Theta)"), MathTex("sin(\Theta)+cos(\Theta)")]
        for i in range(0,len(function_dis)):
            function_dis[i].set_color(color= axes[i].get_color()).next_to(axes[i], UP, buff= 0)
        self.add(VGroup(*function_dis))
