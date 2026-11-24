"""
scene5_interpretation.py
------------------------
Scene 5: Global Interpretation & Calculus Foundations (Target Duration: ~40 seconds)
Visualizes global behavioral properties:
  1. Domain: Shaded continuous blue band spanning all real numbers (-inf, inf) on the x-axis.
  2. Range: Shaded continuous orange band spanning [-1, inf) on the y-axis.
  3. Increasing / Decreasing Intervals:
     - Decreasing (sloping downward, red) on (-inf, 2)
     - Split at the vertex x = 2
     - Increasing (sloping upward, green) on (2, inf)
"""

from manim import *
from config import *
from helpers import *

class Scene5Interpretation(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        # ----------------------------------------------------------------------
        # 1. Header & Setup
        # ----------------------------------------------------------------------
        # Narration: "With our landmarks established, we can interpret the global behavior of the entire function."
        title = Text("Global Behavior: Domain, Range & Monotonicity", font_size=SUBTITLE_FONT_SIZE + 2, color=COLOR_HIGHLIGHT)
        title.to_edge(UP, buff=0.4)
        self.play(FadeIn(title), run_time=1.0)

        # Coordinate axes centered
        axes = make_standard_axes(
            x_range=[-2.0, 5.5, 1.0],
            y_range=[-2.0, 7.0, 1.0],
            x_length=7.5,
            y_length=5.2,
            include_numbers=True
        ).shift(RIGHT * 1.5 + DOWN * 0.4)

        self.play(Create(axes), run_time=1.5)

        # ----------------------------------------------------------------------
        # 2. Domain on X-Axis & Range on Y-Axis
        # ----------------------------------------------------------------------
        # Narration: "The Domain extends across every real number x from negative infinity to positive infinity."
        domain_line = Line(
            start=axes.c2p(-2.0, 0),
            end=axes.c2p(5.5, 0),
            color=COLOR_INPUT,
            stroke_width=8
        )
        domain_label = MathTex(r"\text{Domain: } x \in (-\infty, \infty)", font_size=BODY_FONT_SIZE, color=COLOR_INPUT)
        domain_label.to_edge(LEFT, buff=0.8).shift(UP * 1.8)

        self.play(Create(domain_line), FadeIn(domain_label), run_time=1.5)
        self.wait(6.0)

        # Narration: "Because the parabola opens upwards with minimum at y = -1, the Range is [-1, infinity)."
        range_line = Line(
            start=axes.c2p(0, -1.0),
            end=axes.c2p(0, 6.8),
            color=COLOR_OUTPUT,
            stroke_width=8
        )
        range_label = MathTex(r"\text{Range: } y \in [-1, \infty)", font_size=BODY_FONT_SIZE, color=COLOR_OUTPUT)
        range_label.next_to(domain_label, DOWN, buff=0.5, aligned_edge=LEFT)

        self.play(Create(range_line), FadeIn(range_label), run_time=1.5)
        self.wait(7.0)

        # ----------------------------------------------------------------------
        # 3. Increasing and Decreasing Branches
        # ----------------------------------------------------------------------
        # Narration: "Now observe how outputs change as x increases from left to right."
        curve_dec = axes.plot(f, x_range=[-1.0, 2.0], color=COLOR_DECREASING, stroke_width=5)
        curve_inc = axes.plot(f, x_range=[2.0, 4.8], color=COLOR_INCREASING, stroke_width=5)

        dec_label = Text("Decreasing: (-inf, 2)", font_size=LABEL_FONT_SIZE + 2, color=COLOR_DECREASING)
        dec_label.next_to(range_label, DOWN, buff=0.5, aligned_edge=LEFT)

        inc_label = Text("Increasing: (2, inf)", font_size=LABEL_FONT_SIZE + 2, color=COLOR_INCREASING)
        inc_label.next_to(dec_label, DOWN, buff=0.3, aligned_edge=LEFT)

        # Narration: "To the left of x = 2, the function slopes downward: it is strictly decreasing."
        self.play(Create(curve_dec), FadeIn(dec_label), run_time=2.0)
        self.wait(6.0)

        # Narration: "At x = 2, it reaches its turning point. To the right of x = 2, it slopes upward: strictly increasing."
        pt_vertex = create_point_marker(axes, 2.0, -1.0, dot_color=COLOR_HIGHLIGHT, radius=0.08)
        self.play(Create(curve_inc), FadeIn(inc_label), FadeIn(pt_vertex), run_time=2.0)
        self.wait(9.0)

        # Clear Scene
        self.play(
            FadeOut(title), FadeOut(axes),
            FadeOut(domain_line), FadeOut(domain_label),
            FadeOut(range_line), FadeOut(range_label),
            FadeOut(curve_dec), FadeOut(curve_inc),
            FadeOut(dec_label), FadeOut(inc_label), FadeOut(pt_vertex),
            run_time=1.5
        )
        self.wait(1.0)
