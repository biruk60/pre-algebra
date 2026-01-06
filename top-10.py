from manim import *  # noqa: F403

class TableExamples(Scene):   
    def construct(self):
        logo = ImageMobject("./assets/images/kylian-mbappe-real-madrid.jpg")

        # 2. Scale the image to fit the *height* of the screen
        logo.scale_to_fit_height(config.frame_height)
        
        # 3. Check if the resulting image width is less than the screen width
        # and scale to width if necessary to cover all corners
        # if logo.width < config.frame_width:
        logo.scale_to_fit_width(config.frame_width)

        # 4. Center the image and place it behind other objects
        logo.center()
        logo.set_z_index(-10) # Place far in the background

        # Add the image to the scene
        self.add(logo)
        title = Text("#10: Kylian Mbappe\n", font_size=38, weight=BOLD, color=ORANGE)
        
        table = Table(
                    [["Real Madrid"], 
                    ["French"],
                    ["27"],
                    ["24"],
                    ["29"],
                    ["5"],
                    ["€200.00n"]], 
                    element_to_mobject=Text,
                    element_to_mobject_config={"font_size":12},
                    row_labels=[Text("Club", font_size=12, weight=BOLD), 
                                Text("Natationality", font_size=12, weight=BOLD),
                                Text("Age", font_size=12,weight=BOLD),
                                Text("Matches", font_size=12,weight=BOLD),
                                Text("Goals", font_size=12,weight=BOLD),
                                Text("Assists", font_size=12,weight=BOLD),
                                Text("Market Value", font_size=12,weight=BOLD)],
                                v_buff=0.3,
                                h_buff=0.5,
                                
                    
                    include_outer_lines=True,
                    line_config={"stroke_width": 1, "color": WHITE})
        table.remove(*table.get_vertical_lines())
        
        
        content_group = VGroup(title, table).arrange(
            DOWN, 
            aligned_edge=LEFT, 
            buff=0.4
        )
        rounded_box = SurroundingRectangle(
            content_group, 
            color=WHITE, 
            buff=0.5, # Buffer around the table
            corner_radius=0.1, # Rounded corners
            fill_opacity=0.2, # Optional fill
            stroke_width=1,
        )

        # 3. Group the table and the box together
        # table_group = Group(rounded_box, t3)
        # self.add(table_group)
        self.wait(2)
        self.play(GrowFromCenter(rounded_box), run_time=1)
        self.wait(2)
        self.play(Create(content_group), run_time=1)
        self.wait(2)
        self.play(FadeOut(content_group), run_time=1)
        self.wait(2)
        self.play(ShrinkToCenter(rounded_box), run_time=1)

# manim -pql  delu.py TableExamples
