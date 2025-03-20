from manim import *


class AnimatedSquareToCircle(Scene):
    def construct(self):
        left_circle = Circle(color=WHITE, fill_opacity=1).shift(2* LEFT)
        left_square = Square()

        right_circle = Circle(color=WHITE, fill_opacity=1).shift(2* RIGHT)
        right_square = Square()

        self.play(Create(left_square))
        self.play(left_square.animate.rotate(PI/4))
        self.play(Transform(left_square, left_circle))
        

        self.play(Create(right_square))
        self.play(left_square.animate.rotate(PI/4))
        self.play(Transform(right_square, right_circle))
        