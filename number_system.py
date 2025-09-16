from manim import *
from manim.mobject.geometry.tips import StealthTip

class NumberLineWithAnnotations(Scene):
    def construct(self):
        # Define the number line
        number_line = NumberLine(
            x_range=[-2.5, 4.5, 1],
            length=12,
            color=WHITE,
            include_numbers=True,
            numbers_to_include=[-2, -1, 0, 1, 2, 3, 4],
            include_tip=True,
            tip_shape=StealthTip,  # Arrow at right side
        )
        number_line.add_tip(tip_shape=StealthTip, at_start=True)
        self.add(number_line)
        self.play(FadeIn(number_line), run_time=2)

        # Values to annotate and their positions
        values = [
            ("\\frac{-13}{6}", -2.1667),
            ("-\\sqrt{2}", -1.4142),
            ("-0.43", -0.43),
            ("\\frac{1}{2}", 0.5),
            ("\\sqrt{3}", 1.7321),
            ("2\\frac{3}{4}", 2.75),
            ("\\pi", 3.1416),
            ("3.8", 3.8),
        ]

        # Draw magenta ticks and LaTeX labels below
        for label, pos in values:
            # magenta tick
            tick = Line(
                start=number_line.number_to_point(pos) + UP*0.15,
                end=number_line.number_to_point(pos) + DOWN*0.75,
                color=RED,
                stroke_width=3,
            )
            # label placement
            math_label = MathTex(label).scale(0.7)
            math_label.next_to(
                number_line.number_to_point(pos) + DOWN * 0.75, DOWN, buff=0.09
            )
            self.play(FadeIn(tick), FadeIn(math_label), run_time=1)

        self.wait(2)
