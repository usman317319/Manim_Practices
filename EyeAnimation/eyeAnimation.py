from manim import Animation, Scene, Rectangle
  
class ClossingEye(Animation):
    def __init__(self, mobject, **kwargs):
        super().__init__(mobject, **kwargs)
        self.mobject = mobject
        self.height = mobject.height

    # The function gets called with the execution of every frame with a new alpha value(from 0 to 1)
    def interpolate(self, alpha):
        super().interpolate(alpha)
        self.mobject.stretch_to_fit_height(self.height*(1-alpha))

    # Clean Up the mobject form the scene so that it is not visible any more
    def clean_up_from_scene(self, scene):
        super().clean_up_from_scene(scene)
        scene.remove(self.mobject)

class OpeningEye(Animation):
    def __init__(self, mobject, **kwargs):
        self.mobject = mobject
        self.height = mobject.height #store the initial height
        self.mobject.stretch_to_fit_height(0.00001) #set the height as minimum posible (not zero)
        super().__init__(self.mobject, **kwargs)

    def interpolate(self, alpha):
        super().interpolate(alpha)
        if alpha>0: # this is because stretch_to_fit_height dosen't work with 0
            self.mobject.stretch_to_fit_height(self.height*alpha)

class Example(Scene):
    def construct(self):     
        r = Rectangle()
        self.wait()
        self.play(OpeningEye(r))
        self.wait()
        self.play(ClossingEye(r))
        self.wait()        
        
