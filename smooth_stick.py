from manim import *

class AnatomicalStickFigure(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # --- core points (neutral pose) ---
        self.head_center = ORIGIN + UP * 2.5
        self.neck        = self.head_center + DOWN * 0.3
        self.shoulder    = self.neck + DOWN * 0.2
        self.waist       = self.shoulder + DOWN * 0.7
        self.hip         = self.waist + DOWN * 0.5

        # Limb base directions (local axes)
        self.arm_dir     = RIGHT
        self.leg_dir     = RIGHT

        # Trackers for joint angles (radians)
        self.r_shoulder_angle = ValueTracker(-0.2)
        self.r_elbow_angle    = ValueTracker(0.5)
        self.l_shoulder_angle = ValueTracker(0.3)
        self.l_elbow_angle    = ValueTracker(-0.4)

        self.r_hip_angle   = ValueTracker(-0.2)
        self.r_knee_angle  = ValueTracker(0.3)
        self.l_hip_angle   = ValueTracker(0.3)
        self.l_knee_angle  = ValueTracker(-0.3)

        # lengths
        self.upper_arm_len = 0.8
        self.lower_arm_len = 0.7
        self.thigh_len     = 1.0
        self.calf_len      = 0.9

        # head + body placeholders; real shapes come from updater
        self.head = Circle(radius=0.3, color=WHITE)
        self.body = VMobject()

        # limb segments as VMobject placeholders
        self.r_upper_arm = VMobject()
        self.r_lower_arm = VMobject()
        self.l_upper_arm = VMobject()
        self.l_lower_arm = VMobject()
        self.r_thigh     = VMobject()
        self.r_calf      = VMobject()
        self.l_thigh     = VMobject()
        self.l_calf      = VMobject()

        self.add(
            self.body,
            self.r_upper_arm, self.r_lower_arm,
            self.l_upper_arm, self.l_lower_arm,
            self.r_thigh, self.r_calf,
            self.l_thigh, self.l_calf,
            self.head,
        )

        # Single updater to recompute geometry every frame
        self.add_updater(self.update_pose)
        self.update_pose(self)  # initial pose

    def update_pose(self, mob):
        # convenience
        def rot(v, angle):
            return v.rotate(angle)

        # spine: smooth curve from neck to hip
        neck = self.neck
        hip  = self.hip
        self.body.become(
            ArcBetweenPoints(neck, hip, angle=-0.3, color=WHITE)
        )

        # head follows neck
        self.head.move_to(self.head_center)

        # --- arms ---
        # right upper arm
        r_sh = self.r_shoulder_angle.get_value()
        r_el = self.r_elbow_angle.get_value()
        r_upper_dir = rot(self.arm_dir, r_sh)
        r_elbow_pos = self.shoulder + r_upper_dir * self.upper_arm_len
        r_lower_dir = rot(r_upper_dir, r_el)

        r_hand_pos = r_elbow_pos + r_lower_dir * self.lower_arm_len

        self.r_upper_arm.become(
            ArcBetweenPoints(
                self.shoulder, r_elbow_pos, angle=0.4, color=WHITE
            )
        )
        self.r_lower_arm.become(
            ArcBetweenPoints(
                r_elbow_pos, r_hand_pos, angle=0.2, color=WHITE
            )
        )

        # left upper arm
        l_sh = self.l_shoulder_angle.get_value()
        l_el = self.l_elbow_angle.get_value()
        l_upper_dir = rot(-self.arm_dir, l_sh)
        l_elbow_pos = self.shoulder + l_upper_dir * self.upper_arm_len
        l_lower_dir = rot(l_upper_dir, l_el)

        l_hand_pos = l_elbow_pos + l_lower_dir * self.lower_arm_len

        self.l_upper_arm.become(
            ArcBetweenPoints(
                self.shoulder, l_elbow_pos, angle=-0.4, color=WHITE
            )
        )
        self.l_lower_arm.become(
            ArcBetweenPoints(
                l_elbow_pos, l_hand_pos, angle=-0.2, color=WHITE
            )
        )

        # --- legs ---
        # right leg
        r_hip_a  = self.r_hip_angle.get_value()
        r_knee_a = self.r_knee_angle.get_value()
        r_thigh_dir = rot(self.leg_dir + DOWN, r_hip_a)
        r_knee_pos  = self.hip + r_thigh_dir * self.thigh_len
        r_calf_dir  = rot(r_thigh_dir, r_knee_a)
        r_foot_pos  = r_knee_pos + r_calf_dir * self.calf_len

        self.r_thigh.become(
            ArcBetweenPoints(
                self.hip, r_knee_pos, angle=-0.3, color=WHITE
            )
        )
        self.r_calf.become(
            ArcBetweenPoints(
                r_knee_pos, r_foot_pos, angle=0.3, color=WHITE
            )
        )

        # left leg
        l_hip_a  = self.l_hip_angle.get_value()
        l_knee_a = self.l_knee_angle.get_value()
        l_thigh_dir = rot(-self.leg_dir + DOWN, l_hip_a)
        l_knee_pos  = self.hip + l_thigh_dir * self.thigh_len
        l_calf_dir  = rot(l_thigh_dir, l_knee_a)
        l_foot_pos  = l_knee_pos + l_calf_dir * self.calf_len

        self.l_thigh.become(
            ArcBetweenPoints(
                self.hip, l_knee_pos, angle=-0.3, color=WHITE
            )
        )
        self.l_calf.become(
            ArcBetweenPoints(
                l_knee_pos, l_foot_pos, angle=0.3, color=WHITE
            )
        )

        # keep figure centered if needed
        mob.move_to(ORIGIN)




class SmoothWalkScene(Scene):
    def construct(self):
        guy = AnatomicalStickFigure()
        self.add(guy)

        t = ValueTracker(0)

        # updater that drives all joint angles from t
        def gait_updater(dt):
            t.increment_value(dt)

            phase = t.get_value() * 2  # speed factor

            # simple mirrored walk cycle
            guy.r_hip_angle.set_value( 0.4 * np.sin(phase))
            guy.l_hip_angle.set_value(-0.4 * np.sin(phase))

            guy.r_knee_angle.set_value(0.6 * np.sin(phase + np.pi / 4))
            guy.l_knee_angle.set_value(0.6 * np.sin(phase + np.pi / 4 + np.pi))

            guy.r_shoulder_angle.set_value(-0.4 * np.sin(phase))
            guy.l_shoulder_angle.set_value( 0.4 * np.sin(phase))

            guy.r_elbow_angle.set_value(0.3 * np.sin(phase + np.pi / 3))
            guy.l_elbow_angle.set_value(0.3 * np.sin(phase + np.pi / 3 + np.pi))

        guy.add_updater(lambda m, dt: gait_updater(dt))

        # translate the whole figure smoothly to the right
        def move_forward(m, dt):
            m.shift(RIGHT * dt * 1.5)

        guy.add_updater(move_forward)

        self.wait(4)