from manim.mobject.text.text_mobject import Text
from manim import *  # noqa: F403

def layout()->[mobject.types.image_mobject.ImageMobject, mobject.text.text_mobject.Text]:
    background = ImageMobject("assets/images/soccer_1.jpg").set_opacity(.65)
    # manimpango.register_font("assets/fonts/nyala_regular.ttf")
    background.scale_to_fit_width(config.frame_width)
    background.scale_to_fit_height(config.frame_height)
    background.set_z_index(-10)  # Keep behind everything
    bg_text = Text("@BK_BROOK", fill_opacity=0.15).scale(3)
    bg_text.set_z_index(-9)  # Keep behind everything
    return background, bg_text

class OneGroupAtATime(Scene):
    def construct(self):
        background, bg_text = layout()
        self.add(background)  
        self.add(bg_text)
        self.wait()
        counter_tracker = ValueTracker(0)
        vline = NumberLine(x_range=[1, 10, 1], length=5, include_numbers=True,
                          rotation=PI/2, label_direction=LEFT).to_edge(RIGHT, buff=2)
        
        marker = Dot(color=ORANGE, radius=0.08)
        marker.add_updater(lambda m: m.move_to(vline.number_to_point(10 - counter_tracker.get_value())))
        number_display = always_redraw(lambda: Integer(10 - int(counter_tracker.get_value())).next_to(marker, RIGHT))
        
        self.play(Create(vline), Create(marker), Create(number_display), run_time=1)
        
        # Countdown loop with FULL animations for each player
        for k in range(10):
            self.play(counter_tracker.animate.set_value(k), run_time=0.5)
            
            # When count reaches this player, run their FULL animation sequence
            if k == 0:  # Shows #10 first
                self.player10_animation()
            elif k == 1:
                #self.player9_animation()
                pass
            # ... etc for all 10 players
            
            self.wait(2)

        self.wait(2)

    def player10_animation(self):
        """Full Lautaro Martínez animation sequence"""
        logo = ImageMobject("assets/images/lautaro-martinez-inter.jpg").scale(1.3).set_opacity(.80)
        logo.shift(LEFT * 1.5)
        self.play(FadeIn(logo), run_time=1)
        title = Text("Lautaro Martínez\n", font_size=50, weight=BOLD, color=ORANGE)        
        title.next_to(logo, UP, buff=0.3)  # Directly above logo
        self.play(Write(title), run_time=1)
        
        table = Table([["ኢንተር ሚላን"], ["ኣርጀንቲና"], ["28"], ["ማእከል-ኣጥቃዓይ"],
                      ["25"], ["16"], ["5"], ["€85 ሚልዮን"]], 
                     element_to_mobject=Text,
                     element_to_mobject_config={"font_size":12, "font":"Noto Sans Ethiopic","color": WHITE},
                     row_labels=[Text("ክለብ", font_size=12, font="Noto Sans Ethiopic", weight=BOLD, color=WHITE), 
                                Text("ዜግነት", font_size=12, font="Noto Sans Ethiopic", weight=BOLD, color=WHITE), 
                                Text("ቦታ", font_size=12, font="Noto Sans Ethiopic", weight=BOLD, color=WHITE), 
                                Text("ዕድመ", font_size=12, font="Noto Sans Ethiopic", weight=BOLD, color=WHITE), 
                                Text("ግጥም", font_size=12, font="Noto Sans Ethiopic", weight=BOLD, color=WHITE), 
                                Text("ጎል", font_size=12, font="Noto Sans Ethiopic", weight=BOLD, color=WHITE), 
                                Text("ሓገዝ", font_size=12, font="Noto Sans Ethiopic", weight=BOLD, color=WHITE), 
                                Text("ዋጋ ዕዳጋ" , font_size=12, font="Noto Sans Ethiopic", weight=BOLD, color=WHITE)],
                     v_buff=0.3, 
                     h_buff=0.4, 
                     include_outer_lines=True,
                    line_config={"stroke_width": 1, "color": ORANGE})
        table.remove(*table.get_vertical_lines())
        
        content_group = VGroup(table).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        
        content_group.shift(LEFT * 1.5)
        rounded_box = SurroundingRectangle(content_group, 
                                            color=ORANGE,           # Stroke color (border)
                                            fill_color=WHITE, 
                                           buff=0.5, 
                                         corner_radius=0.1, 
                                         fill_opacity=0.2, 
                                         stroke_width=1,)
            
        self.play(GrowFromCenter(rounded_box), run_time=1)
        self.wait(0.5)
        self.play(FadeIn(content_group), run_time=1)
        self.wait(2)
        self.play(FadeOut(content_group), run_time=1)
        self.wait(0.5)
        self.play(ShrinkToCenter(rounded_box), run_time=1)
        self.play(Unwrite(title), run_time=1)
        self.play(FadeOut(logo), run_time=1)


    # manim -pqm .\top_10_valuable_players.py OneGroupAtATime --resolution 1920,1080 --fps 30
