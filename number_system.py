from manim import *
from manim.mobject.geometry.tips import StealthTip

class IntroScene(ThreeDScene):
    def construct(self):
        # Define the number line
        # triangle = Triangle()
        # dot = Dot(3 * UR, color=GREEN)
        # circle = Circle()
        # square = Square()
        # self.play(SpinInFromNothing(triangle))
        # self.play(GrowFromPoint(circle, dot, dot.get_color()))
        # self.play(GrowFromPoint(square, ORIGIN))
        # shapes = VGroup(triangle, circle, square)
        # self.play(ShrinkToCenter(shapes))
        # self.play(ShrinkToCenter(triangle),ShrinkToCenter(circle),ShrinkToCenter(square))
        
        # self.play(FadeTransform(triangle, circle))
        # self.wait(1)
        # ax = Axes()
        # sine = ax.plot(np.sin, color=RED)
        # alpha = ValueTracker(0)
        # point = always_redraw(
        #     lambda: Dot(
        #         sine.point_from_proportion(alpha.get_value()),
        #         color=BLUE
        #     )
        # )
        # tangent = always_redraw(
        #     lambda: TangentLine(
        #         sine,
        #         alpha=alpha.get_value(),
        #         color=YELLOW,
        #         length=4
        #     )
        # )
        # self.add(ax, sine, point, tangent)
        # self.play(alpha.animate.set_value(1), rate_func=linear, run_time=2)
        # graphs = VGroup(ax, sine, point, tangent)
        # Import SVG file


        # colors = [RED, GREEN, BLUE]

        # starting_points = VGroup(
        #     *[
        #         Dot(LEFT + pos, color=color)
        #         for pos, color in zip([UP, DOWN, LEFT], colors)
        #     ]
        # )
        
        # self.add(starting_points)
        # self.play(FadeTransform(finish_points,starting_points))

        # finish_points = VGroup(
        #     *[
        #         Dot(RIGHT + pos, color=color)
        #         for pos, color in zip([ORIGIN, UP, DOWN], colors)
        #     ]
        # )

        
        
        # for dot in starting_points:
        #     self.add(TracedPath(dot.get_center, stroke_color=dot.get_color()))

        # self.wait()
        # self.play(
        #     Create(finish_points),
        #     Transform(
        #         starting_points,
        #         finish_points,
        #         path_func=utils.paths.clockwise_path(),
        #         run_time=2,
        #     )
        # )
        # background_svg = SVGMobject("assets/man-stickman-svgrepo-com.svg")
        # background_svg.set_z_index(-10)  # Make sure it is rendered at the back
        # background_svg.set(width=3)      # Resize as needed
        # self.add_fixed_in_frame_mobjects(background_svg)
        # intro_text= Text('Maths with BK')
        # Add the SVG to the scene
        
        self.wait()
        intro_text= Text('Maths with BK', fill_opacity=1).to_edge(UP)
        bg_text = Text("@BK_BROOK", fill_opacity=0.065).scale(3)
        bg_text.set_z_index(-10)  # Keep behind everything

        # Add text as a fixed background element
        self.add_fixed_in_frame_mobjects(bg_text)
        axes = ThreeDAxes(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            z_range=[-6, 6, 1],
            x_length=8,
            y_length=6,
            z_length=6,           
            axis_config={'tip_shape': StealthTip } 
        )
        
        # axes.add_tip(tip_shape=StealthTip, at_start=True)
        # axes.add_coordinates()
        graph = axes.plot(lambda x: x ** 2, x_range=[-2, 2, 1], color=YELLOW)
        rects = axes.get_area(
                                graph,
                                x_range=[-2, 2],
                                color=BLUE,
                                opacity=1
                            )

        graph2 = axes.plot_parametric_curve(
            lambda t: np.array([np.cos(t), np.sin(t), t]),
            t_range=[-2 * PI, 2 * PI],
            color=RED,
        )

        self.play(FadeIn(axes, runt_time=1), FadeIn(graph, run_time=2))
        self.wait()

        ##THE CAMERA IS AUTO SET TO PHI = 0 and THETA = -90

        self.move_camera(phi=60 * DEGREES)
        self.wait()
        self.move_camera(theta=-45 * DEGREES)

        self.begin_ambient_camera_rotation(
            rate=PI / 10, about="theta"
        )  # Rotates at a rate of radians per second
        self.wait()
        self.play(Create(rects), run_time=3)
        self.play(Create(graph2))
        self.wait()
        self.stop_ambient_camera_rotation()

        self.wait()
        self.begin_ambient_camera_rotation(
            rate=PI / 10, about="phi"
        )  # Rotates at a rate of radians per second
        self.wait(1) 
        self.stop_ambient_camera_rotation()
        self.wait(1)
        self.add_fixed_in_frame_mobjects(intro_text)
        self.play(Write(intro_text))
        self.wait(2)
        self.play(Unwrite(intro_text))
        self.wait(5)
        

class OutroScene(Scene):
    def construct(self):
        # Texts
        share_text = Text("Share", font_size=44, color=BLUE)
        like_text = Text("Like", font_size=44, color=GREEN)
        subscribe_text = Text("Subscribe", font_size=44, color=RED)

        # Shapes
        share_circle = Circle(radius=1.2, color=BLUE)
        like_triangle = Triangle().scale(1.6).set_color(GREEN)
        subscribe_rect = Rectangle(width=4, height=2.4, color=RED)

        # Put text in shapes
        share_group = VGroup(share_circle, share_text).arrange(ORIGIN)
        like_group = VGroup(like_triangle, like_text).next_to(share_group, RIGHT)
        subscribe_group = VGroup(subscribe_rect, subscribe_text).next_to(like_group, RIGHT)

        # Stack vertically
        final_group = VGroup(share_group, like_group, subscribe_group).arrange(RIGHT,buff=0.4)

        # Animations
        self.play(FadeIn(share_group))
        self.wait(0.5)
        self.play(FadeIn(like_group), like_text.animate.set_color(YELLOW))
        self.wait(0.5)
        self.play(FadeIn(subscribe_group), subscribe_text.animate.set_color(ORANGE))
        self.wait(1)
        
        self.play(ShrinkToCenter(final_group))
        
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
