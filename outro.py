
from manim import * 
import manimpango

class OutroScene(Scene):
    def construct(self):
         background = ImageMobject("assets/images/blackboard.png").set_opacity(.8)
        background.scale_to_fit_width(config.frame_width)
        background.scale_to_fit_height(config.frame_height)
        background.set_z_index(-10)  # Keep behind everything

        self.add(background)
        bg_text = Text("@BK_BROOK", fill_opacity=0.025).scale(3)
        bg_text.set_z_index(-9)  # Keep behind everything

        # Add text as a fixed background element
        self.add(bg_text)
        # Texts
        share_text = Text("Share.", font_size=44, color='#52B2BF').shift(3*LEFT)
        like_text = Text("Like.", font_size=44, color='#708238').next_to(share_text, 1.5*RIGHT)
        subscribe_text = Text("Subscribe.", font_size=44, color='#EDC001').next_to(like_text, 1.5*RIGHT)
        buff=0.3
        self.play(FadeIn(share_text), FadeIn(like_text), FadeIn(subscribe_text), run_time=1)
        self.play(Circumscribe(share_text, Circle, color='#52B2BF', buff=buff))
        self.play(Circumscribe(share_text, Circle, True,color='#52B2BF', buff=buff))
        self.play(Circumscribe(like_text, Rectangle, color='#708238', buff=buff))
        self.play(Circumscribe(like_text, Rectangle, True,color='#708238', buff=buff))
        self.play(Circumscribe(subscribe_text, Circle, color='#EDC001', buff=buff))
        self.play(Circumscribe(subscribe_text, Circle, True,color='#EDC001', buff=buff))
        final_group = VGroup(share_text, like_text, subscribe_text)
        self.play(ShrinkToCenter(final_group), run_time=1)   
        self.wait(1)
        # manim -ql -p --disable_caching  -o outro_video.mp4 .\outro.py OutroScene
