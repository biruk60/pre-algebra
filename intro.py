from manim import * 
import manimpango

class IntroScene(ThreeDScene):
    def construct(self):
        background = ImageMobject("assets/images/blackboard.png").set_opacity(0.55)
        manimpango.register_font("assets/fonts/nyala_regular.ttf")
        background.scale_to_fit_width(config.frame_width)
        background.scale_to_fit_height(config.frame_height)
        background.set_z_index(-10)  # Keep behind everything
        bg_text = Text("@BK_BROOK", fill_opacity=0.025).scale(3)
        bg_text.set_z_index(-9)  # Keep behind everything

        # Add text as a fixed background element
        self.add_fixed_in_frame_mobjects(background)  
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
                
        graph = axes.plot(lambda x: x ** 2, x_range=[-2, 2, 1], color=BLUE)
        rects = axes.get_riemann_rectangles(
                                graph,
                                x_range=[-2, 2],
                                dx=0.08,
                                color=BLUE
                                
                            )

        graph2 = axes.plot_parametric_curve(
            lambda t: np.array([np.cos(t), np.sin(t), t]),
            t_range=[-2 * PI, 2 * PI],
            color='#EDC001',
        )
        self.play(GrowFromPoint(axes, ORIGIN),runt_time=1)
        self.play(Create(graph), run_time=2)
        # self.play(FadeIn(axes, runt_time=1), FadeIn(graph, run_time=2))
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
        self.wait(2)
        what = VGroup(axes, graph, graph2, rects)
        self.play(ShrinkToCenter(what))
        self.wait()
        # Heights and widths for better control
        height = 2
        widths = [0.8, 0.7, 0.8]

        # First Column
        col1_rectangle_width = widths[0]
        col1 = VGroup(
            Square(side_length=col1_rectangle_width, color='#4B5320', fill_opacity=0.8),
            Rectangle(height=height, width=col1_rectangle_width, color='#82EEFD', fill_opacity=0.8),            
            Rectangle(height=height, width=col1_rectangle_width, color='#FFDA03', fill_opacity=0.8) # unified width
        ).arrange(DOWN, buff=0.3)

        # Second Column
        col2_rectangle_width = col1_rectangle_width # match first column width
        col2 = VGroup(
            Rectangle(height=height, width=col2_rectangle_width, color='#FFE135', fill_opacity=0.8),
            Square(side_length=col2_rectangle_width, color='#4F7942', fill_opacity=0.8),            
            Rectangle(height=height, width=col2_rectangle_width, color='#63C5DA', fill_opacity=0.8)
        ).arrange(DOWN, buff=0.3)

        # Third Column
        col3_rectangle_width = col1_rectangle_width # match first column width
        col3 = VGroup(
            Rectangle(height=height, width=col3_rectangle_width, color='#52B2BF', fill_opacity=0.8),           
            Rectangle(height=height, width=col3_rectangle_width, color='#EDC001', fill_opacity=0.8),
            Square(side_length=col3_rectangle_width, color='#708238', fill_opacity=0.8),
        ).arrange(DOWN, buff=0.3)

        # Align bottoms of all columns
        for col in [col1, col2, col3]:
            col.move_to(ORIGIN)
        columns = VGroup(col1, col2, col3).arrange(RIGHT, buff=0.5)
        columns.align_to(col1, DOWN) # aligns bottom edge

        self.add_fixed_in_frame_mobjects(columns)
        self.play(FadeIn(columns), run_time=.5)
        
        # Add text below the aligned columns
        intro_text = Text("ሒሳብ ምስ ብሩኽ", font_size=36, font="Nyala")
        intro_text.next_to(columns, DOWN, buff=0.3)
        self.add_fixed_in_frame_mobjects(intro_text)
    
        self.play(Write(intro_text), run_time=.5)
        
        intro_text.save_state()
        columns.save_state()
        matrix = [[1, 1], [0, 2/3]]
        self.play(ApplyMatrix(matrix, intro_text), ApplyMatrix(matrix, columns))
        self.wait(.5)
        self.play(Restore(intro_text),Restore(columns), run_time=.5)
        

        self.play(Unwrite(intro_text))
        self.wait()
        self.play(ReplacementTransform(col1[0], col1[1]),ReplacementTransform(col1[1], col1[2]))
        self.play(ReplacementTransform(col2[0], col2[1]),ReplacementTransform(col2[1], col2[2]))
        self.play(ReplacementTransform(col3[0], col3[1]),ReplacementTransform(col3[1], col3[2]))
        self.play(ReplacementTransform(col1, col2))
        self.play(ReplacementTransform(col2, col3))
        self.play(FadeOut(columns))
        self.wait()
        
        # manim -ql -p --disable_caching  -o intro_video.mp4 .\intro.py IntroScene
