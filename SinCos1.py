from manim import *
from math import *
# from colour import Color

class Test(Scene):
    def construct(self):
        sinT = Text("Sin function")
        sinPlot = Axes(x_range=[0,14], y_range=[-2,2])
        sine=sinPlot.plot(lambda x: sin(x),color=GREEN,stroke_width=5)
        temp=VGroup(sinPlot,sine)
        sinGroup=VGroup(temp,sinT).arrange(UP)
        

        cosT = Text("Cos function")
        cosPlot = Axes(x_range=[0,14], y_range=[-2,2])
        cose=cosPlot.plot(lambda x: cos(x),color=RED)
        temp=VGroup(cosPlot,cose)
        cosGroup=VGroup(temp,cosT).arrange(UP)
        

        sinPcosT = Text("Sin + Cos functions")
        sinPcosPlot = Axes(x_range=[0,14], y_range=[-2,2])
        sinPcos=sinPcosPlot.plot(lambda z: sin(z)+cos(z),color=YELLOW)
        temp=VGroup(sinPcosPlot,sinPcos)
        sinPcosGroup=VGroup(temp,sinPcosT).arrange(UP)
        

        self.add(VGroup(sinPcosGroup,cosGroup,sinGroup).arrange(UP).scale(0.35))