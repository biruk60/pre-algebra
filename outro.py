
from manim import * 
import manimpango

class OutroScene(Scene):
    def construct(self):
        # Texts
        share_text = Text("Share.", font_size=44, color='#52B2BF').shift(3*LEFT)
        like_text = Text("Like.", font_size=44, color='#708238').next_to(share_text, 1.5*RIGHT)
        subscribe_text = Text("Subscribe.", font_size=44, color='#EDC001').next_to(like_text, 1.5*RIGHT)

        self.play(FadeIn(share_text), FadeIn(like_text), FadeIn(subscribe_text), run_time=1)
        self.play(Circumscribe(share_text, Circle, color='#52B2BF', buff=.3))
        self.play(Circumscribe(share_text, Circle, True,color='#52B2BF', buff=.3))
        self.play(Circumscribe(like_text, Rectangle, color='#708238', buff=.3))
        self.play(Circumscribe(like_text, Rectangle, True,color='#708238', buff=.3))
        self.play(Circumscribe(subscribe_text, Circle, color='#EDC001', buff=.3))
        self.play(Circumscribe(subscribe_text, Circle, True,color='#EDC001', buff=.3))
        final_group = VGroup(share_text, like_text, subscribe_text)
        self.play(ShrinkToCenter(final_group), run_time=1)   
        self.wait(1)
        
        # manim -ql -p --disable_caching  -o outro_video.mp4 .\outro.py OutroScene
