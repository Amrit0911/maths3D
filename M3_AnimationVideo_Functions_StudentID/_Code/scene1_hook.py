"""
scene1_hook.py
--------------
Scene 1: Hook & Real-World Motivation (Target Duration: ~35 seconds)
Introduces the guiding question: "How do we picture one quantity depending on another?"
Presents two intuitive real-world relationships:
  1. Phone battery % vs Hours elapsed (decay curve)
  2. Projectile ball height vs Flight time (parabolic arc)
Concludes with the core idea: relationships become visible as curves in 2D space.
"""

from manim import *
import numpy as np
from config import *
from helpers import *

class Scene1Hook(Scene):
    def construct(self):
        # Background color
        self.camera.background_color = COLOR_BG

        # ----------------------------------------------------------------------
        # 1. Guiding Question & Section Header
        # ----------------------------------------------------------------------
        # Narration: "Every day, we experience quantities that are bound together in cause and effect."
        title = Text("How Do Quantities Depend on Each Other?", font_size=TITLE_FONT_SIZE, color=COLOR_HIGHLIGHT)
        title.to_edge(UP, buff=0.8)

        # Narration: "How can we take these dynamic relationships and picture them clearly with mathematics?"
        self.play(Write(title), run_time=2.0)
        self.wait(1.5)

        # ----------------------------------------------------------------------
        # 2. Example 1: Phone Battery Life over Time
        # ----------------------------------------------------------------------
        # Narration: "Consider your smartphone battery: as hours tick by, the remaining percentage steadily drains."
        axes_battery = Axes(
            x_range=[0, 12, 2],
            y_range=[0, 100, 20],
            x_length=4.8,
            y_length=3.2,
            axis_config={"color": COLOR_AXES, "stroke_width": 2, "include_tip": True}
        ).shift(LEFT * 3.5 + DOWN * 0.8)

        lbl_batt_x = Text("Time (hours)", font_size=LABEL_FONT_SIZE, color=COLOR_INPUT).next_to(axes_battery.x_axis, DOWN, buff=0.2)
        lbl_batt_y = Text("Battery (%)", font_size=LABEL_FONT_SIZE, color=COLOR_OUTPUT).next_to(axes_battery.y_axis, UP, buff=0.2).shift(RIGHT * 0.4)
        lbl_batt_title = Text("1. Battery Depletion", font_size=SUBTITLE_FONT_SIZE, color=COLOR_TEXT).next_to(axes_battery, UP, buff=0.4)

        batt_curve = axes_battery.plot(
            lambda t: 100.0 * np.exp(-0.22 * t),
            x_range=[0, 11],
            color=COLOR_OUTPUT,
            stroke_width=3.5
        )

        self.play(
            FadeIn(lbl_batt_title),
            Create(axes_battery),
            FadeIn(lbl_batt_x),
            FadeIn(lbl_batt_y),
            run_time=2.0
        )
        self.play(Create(batt_curve), run_time=2.5)
        self.wait(1.5)

        # ----------------------------------------------------------------------
        # 3. Example 2: Ball Height over Time
        # ----------------------------------------------------------------------
        # Narration: "Or throw a ball into the air: gravity dictates its height at each exact instant of flight."
        axes_ball = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 20, 5],
            x_length=4.8,
            y_length=3.2,
            axis_config={"color": COLOR_AXES, "stroke_width": 2, "include_tip": True}
        ).shift(RIGHT * 3.5 + DOWN * 0.8)

        lbl_ball_x = Text("Time (s)", font_size=LABEL_FONT_SIZE, color=COLOR_INPUT).next_to(axes_ball.x_axis, DOWN, buff=0.2)
        lbl_ball_y = Text("Height (m)", font_size=LABEL_FONT_SIZE, color=COLOR_OUTPUT).next_to(axes_ball.y_axis, UP, buff=0.2).shift(RIGHT * 0.4)
        lbl_ball_title = Text("2. Projectile Flight", font_size=SUBTITLE_FONT_SIZE, color=COLOR_TEXT).next_to(axes_ball, UP, buff=0.4)

        ball_curve = axes_ball.plot(
            lambda t: -4.9 * (t ** 2) + 18.0 * t,
            x_range=[0, 3.67],
            color=COLOR_GRAPH,
            stroke_width=3.5
        )

        self.play(
            FadeIn(lbl_ball_title),
            Create(axes_ball),
            FadeIn(lbl_ball_x),
            FadeIn(lbl_ball_y),
            run_time=2.0
        )
        self.play(Create(ball_curve), run_time=2.5)
        self.wait(2.0)

        # ----------------------------------------------------------------------
        # 4. Central Thesis & Transition
        # ----------------------------------------------------------------------
        # Narration: "Whenever one variable determines another uniquely, we are studying a single-variable function."
        thesis_box = RoundedRectangle(corner_radius=0.2, height=1.2, width=11.5, color=COLOR_HIGHLIGHT, fill_color=COLOR_BOX, fill_opacity=0.95)
        thesis_box.to_edge(DOWN, buff=0.4)
        thesis_text = Text(
            "A function maps each input to exactly one output.",
            font_size=BODY_FONT_SIZE,
            color=COLOR_TEXT
        ).move_to(thesis_box.get_center())

        self.play(FadeIn(thesis_box), Write(thesis_text), run_time=2.0)
        self.wait(4.0)

        # Clear scene cleanly for next topic
        self.play(
            FadeOut(title),
            FadeOut(axes_battery), FadeOut(lbl_batt_title), FadeOut(lbl_batt_x), FadeOut(lbl_batt_y), FadeOut(batt_curve),
            FadeOut(axes_ball), FadeOut(lbl_ball_title), FadeOut(lbl_ball_x), FadeOut(lbl_ball_y), FadeOut(ball_curve),
            FadeOut(thesis_box), FadeOut(thesis_text),
            run_time=1.5
        )
        self.wait(1.0)
