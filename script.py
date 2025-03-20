from manim import *
import numpy as np


class AnimatedSquareToCircle(Scene):
    def construct(self):
        left_circle = Circle(color=WHITE, fill_opacity=1).shift(2* LEFT)
        left_square = Square()
        left_small = Circle(color=BLACK, radius=0.5, fill_opacity=1).shift(1.5* LEFT)

        right_circle = Circle(color=WHITE, fill_opacity=1).shift(2* RIGHT)
        right_square = Square()
        right_small = Circle(color=BLACK, radius=0.5, fill_opacity=1).shift(1.5* RIGHT)

        sin = Axes(x_range=[1, 5], y_range=[3,5])
        smile = sin.plot(lambda x: np.sin(x+1), color=WHITE)
        self.add(smile)
        


        self.play(Create(left_square))
        self.play(left_square.animate.rotate(PI/4))
        self.play(Transform(left_square, left_circle))
        

        self.play(Create(right_square))
        self.play(left_square.animate.rotate(PI/4))
        self.play(Transform(right_square, right_circle))
        
        self.play(Create(left_small), Create(right_small))
        