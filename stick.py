from manim import *

class AnatomicalStickFigure(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        head = Circle(radius=0.3, color=WHITE)

        # Slightly curved spine
        body = ArcBetweenPoints(
            head.get_bottom(),
            head.get_bottom() + DOWN * 1.2,
            angle=-0.25,
            color=WHITE,
        )

        # Important anchor points
        neck     = head.get_bottom()
        shoulder = body.point_from_proportion(0.25)
        waist    = body.point_from_proportion(0.7)
        hip      = body.point_from_proportion(1.0)

        # --- Arms: upper + lower ---

        # Left arm joints
        left_elbow_pos = shoulder + LEFT * 0.6 + DOWN * 0.1
        left_hand_pos  = left_elbow_pos + LEFT * 0.5 + DOWN * 0.2

        left_upper_arm = ArcBetweenPoints(
            shoulder, left_elbow_pos, angle=0.5, color=WHITE
        )
        left_lower_arm = ArcBetweenPoints(
            left_elbow_pos, left_hand_pos, angle=0.3, color=WHITE
        )

        # Right arm joints
        right_elbow_pos = shoulder + RIGHT * 0.6 + DOWN * 0.1
        right_hand_pos  = right_elbow_pos + RIGHT * 0.5 + DOWN * 0.2

        right_upper_arm = ArcBetweenPoints(
            shoulder, right_elbow_pos, angle=-0.5, color=WHITE
        )
        right_lower_arm = ArcBetweenPoints(
            right_elbow_pos, right_hand_pos, angle=-0.3, color=WHITE
        )

        # --- Legs: thigh + calf ---

        # Left leg joints
        left_knee_pos = hip + LEFT * 0.3 + DOWN * 0.7
        left_foot_pos = left_knee_pos + LEFT * 0.2 + DOWN * 0.6

        left_thigh = ArcBetweenPoints(
            hip, left_knee_pos, angle=-0.4, color=WHITE
        )
        left_calf = ArcBetweenPoints(
            left_knee_pos, left_foot_pos, angle=0.3, color=WHITE
        )

        # Right leg joints
        right_knee_pos = hip + RIGHT * 0.3 + DOWN * 0.7
        right_foot_pos = right_knee_pos + RIGHT * 0.2 + DOWN * 0.6

        right_thigh = ArcBetweenPoints(
            hip, right_knee_pos, angle=-0.2, color=WHITE
        )
        right_calf = ArcBetweenPoints(
            right_knee_pos, right_foot_pos, angle=0.2, color=WHITE
        )

        # Group for easier indexing and animation
        self.head          = head
        self.body          = body
        self.left_upper_arm  = left_upper_arm
        self.left_lower_arm  = left_lower_arm
        self.right_upper_arm = right_upper_arm
        self.right_lower_arm = right_lower_arm
        self.left_thigh      = left_thigh
        self.left_calf       = left_calf
        self.right_thigh     = right_thigh
        self.right_calf      = right_calf

        self.shoulder = shoulder
        self.left_elbow_pos  = left_elbow_pos
        self.right_elbow_pos = right_elbow_pos
        self.hip       = hip
        self.left_knee_pos   = left_knee_pos
        self.right_knee_pos  = right_knee_pos

        self.add(
            head,
            body,
            left_upper_arm, left_lower_arm,
            right_upper_arm, right_lower_arm,
            left_thigh, left_calf,
            right_thigh, right_calf,
        )
        self.move_to(ORIGIN)




class AnatomicalStickScene(Scene):
    def construct(self):
        guy = AnatomicalStickFigure()
        self.play(Create(guy))

        # Short alias
        shoulder = guy.shoulder
        left_elbow  = guy.left_elbow_pos
        right_elbow = guy.right_elbow_pos
        hip         = guy.hip
        left_knee   = guy.left_knee_pos
        right_knee  = guy.right_knee_pos

        # Wave with right arm: rotate upper arm at shoulder, then lower at elbow
        self.play(
            Rotate(guy.right_upper_arm, angle=0.5, about_point=shoulder),
            run_time=0.3,
        )
        self.play(
            Rotate(guy.right_lower_arm, angle=0.7, about_point=right_elbow),
            run_time=0.3,
        )
        self.play(
            Rotate(guy.right_lower_arm, angle=-0.7, about_point=right_elbow),
            Rotate(guy.right_upper_arm, angle=-0.5, about_point=shoulder),
            run_time=0.3,
        )

        # Simple walk-like leg motion: swing thighs at hip, calves at knee
        self.play(
            Rotate(guy.left_thigh, angle=0.3, about_point=hip),
            Rotate(guy.right_thigh, angle=-0.3, about_point=hip),
            run_time=0.4,
        )
        self.play(
            Rotate(guy.left_calf, angle=-0.4, about_point=left_knee),
            Rotate(guy.right_calf, angle=0.4, about_point=right_knee),
            run_time=0.4,
        )

        # Move whole character
        self.play(guy.animate.shift(RIGHT * 3), run_time=2)
        self.wait()