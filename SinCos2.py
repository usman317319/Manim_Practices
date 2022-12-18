from manim import *
from math import sin,cos


def PlotTrigFunc(trigfunc, text, COLOUR):
    axes = Axes(x_range=[0,14], y_range=[-2,2])

    if trigfunc == sin:
        trigfunc = axes.plot(lambda x: sin(x), color=COLOUR)
    elif trigfunc == cos:
        trigfunc = axes.plot(lambda x: cos(x), color=COLOUR)
    else:
        trigfunc = axes.plot(lambda x: sin(x) + cos(x), color=COLOUR)

    temp = VGroup(axes,trigfunc)

    return VGroup(Text(text),temp).arrange(DOWN)

class TrigFunctions(Scene):
    def construct(self):
        self.add(VGroup(
            PlotTrigFunc(sin, "Sin Function", RED),
            PlotTrigFunc(cos, "Cos Function", GREEN),
            PlotTrigFunc(lambda x: sin(x)+cos(x), "Sin + Cos Functions", YELLOW)
            ).arrange(DOWN).scale(0.35))