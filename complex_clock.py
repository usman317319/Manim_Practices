from manim import *

class IotaClock(VGroup):
    def __init__(self):
        # Values
        self.answers = ["i", "-1", "-i", "1"]

        # Clock Parts
        self.body = VGroup(
            Circle(radius= 1),
            Line([0,-1,0], [0,1,0]),  # Vertical Line
            Line([-1,0,0], [1,0,0]) # Horizontal Line
        ).set_color("#ed443e")
        self.needle = Line([0,0,0], [0,0.9,0]).add_tip(tip_length= 0.2, tip_width= 0.2)
        self.labels = VGroup(*[ MathTex(f"{i}") for i in self.answers ])
        self.labels[0].next_to(self.body[1], UP, buff= 0.3)
        self.labels[1].next_to(self.body[2], LEFT, buff= 0.3)
        self.labels[2].next_to(self.body[1], DOWN, buff= 0.3)
        self.labels[3].next_to(self.body[2], RIGHT, buff= 0.3)

        self.dot = Dot().scale(0.5)

        self.clock = VGroup(self.body, self.needle, self.labels, self.dot)

        # Values
        self.calculation = MathTex("i", "^1", "=\ ", f"{self.answers[0]}")

        # next counter
        self.powerCounter   = 1
        self.answersCounter = 0

        # VGrouping and Arranging
        super().__init__(self.calculation, self.clock)
        self.arrange(buff= 1.5)
        self.add_background_rectangle(color= WHITE, opacity= 0.4)
        self[0].scale(1.2)
    
    def next(self):
        self.powerCounter   += 1
        self.answersCounter += 1
        if (self.answersCounter % 4) == 0:
            self.answersCounter = 0
        return Succession(
            Rotate(self.needle, angle= PI/2, about_point= self.body.get_center()),
            AnimationGroup(
                self.calculation[1].animate.become(MathTex(f"^{{{self.powerCounter}}}").move_to(self.calculation[1])),
                self.calculation[-1].animate.become(MathTex(f"{self.answers[self.answersCounter]}").move_to(self.calculation[-1])),
                Indicate(self.labels[self.answersCounter])
            )
        )
    
class Test(Scene):
    def construct(self):
        a = IotaClock()
        self.add(a)
        for i in range(10):
            self.play(a.next())
            self.wait(0.5)
