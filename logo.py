from manim import *

class BrightHorizonLogo(Scene):
    def construct(self):
        # Colors
        sun_color = YELLOW_E
        text_color = BLACK

        # --- Sunrise rays ---
        rays = VGroup()
        num_main_rays = 13
        max_length = 1.6
        min_length = 0.9
        # Centered at origin, going upward (semi‑circle fan)
        for i in range(num_main_rays):
            # angles from -60° to 60°
            angle = -60 * DEGREES + i * (120 * DEGREES / (num_main_rays - 1))
            length = min_length + (max_length - min_length) * abs(angle) / (60 * DEGREES)
            start = ORIGIN
            end = start + length * np.array([np.cos(angle), np.sin(angle), 0])
            ray = Line(start, end, stroke_width=3, color=text_color)
            rays.add(ray)

        # Small decorative dots near tips of some rays
        dots = VGroup()
        dot_indices = [1, 3, 5, 7, 9, 11]
        for idx in dot_indices:
            ray = rays[idx]
            # position slightly inside the tip
            pos = ray.get_end() * 0.85
            dot = Dot(pos, radius=0.035, color=sun_color)
            dots.add(dot)

        # Shift sunrise up slightly
        sunrise = VGroup(rays, dots).shift(UP * 1.5)

        # --- Text: Bright Horizon ---
        title = Text(
            "Bright Horizon",
            font="Times New Roman",
            weight=BOLD,
            color=text_color
        ).scale(0.9)
        title.next_to(sunrise, DOWN, buff=0.35)

        # --- Text: COUNSELING ---
        subtitle = Text(
            "COUNSELING",
            font="Times New Roman",
            weight=MEDIUM,
            color=text_color
        ).scale(0.4)
        subtitle.next_to(title, DOWN, buff=0.25)

        # Center everything on screen
        logo = VGroup(sunrise, title, subtitle).move_to(ORIGIN)
        self.add(logo)