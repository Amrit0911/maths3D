"""
scene3_intuition.py
-------------------
Scene 3: Visual Intuition & The Graph as Points (Target Duration: ~75 seconds)
Bridges algebraic substitution with geometric points:
  1. Sets up 2D coordinate system.
  2. Builds an input-output evaluation table one row at a time:
     x in {0, 1, 2, 3, 4}, showing f(x) calculation and plotting (x, f(x)).
  3. Extends boundary points x = -1 and x = 5.
  4. Traces the continuous parabola y = x^2 - 4x + 3 through all points.
  5. Sweeps a vertical test line left to right to prove the Vertical Line Test.
"""

from manim import *
from config import *
from helpers import *

class Scene3Intuition(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        # ----------------------------------------------------------------------
        # 1. Header & Split Screen Setup
        # ----------------------------------------------------------------------
        # Narration: "The graph of a function is simply the collection of all ordered pairs (x, f(x)) plotted in 2D space."
        title = Text("The Graph: Assembling Points (x, f(x))", font_size=SUBTITLE_FONT_SIZE + 2, color=COLOR_HIGHLIGHT)
        title.to_edge(UP, buff=0.4)
        self.play(FadeIn(title), run_time=1.0)

        # Coordinate axes placed on the right side
        axes = make_standard_axes(
            x_range=[-2.0, 5.5, 1.0],
            y_range=[-2.0, 9.0, 2.0],
            x_length=6.5,
            y_length=5.5,
            include_numbers=True
        ).shift(RIGHT * 2.8 + DOWN * 0.4)

        axes_label_x = MathTex("x", font_size=BODY_FONT_SIZE, color=COLOR_INPUT).next_to(axes.x_axis.get_end(), RIGHT, buff=0.15)
        axes_label_y = MathTex("y = f(x)", font_size=BODY_FONT_SIZE, color=COLOR_OUTPUT).next_to(axes.y_axis.get_end(), UP, buff=0.15)

        self.play(Create(axes), Write(axes_label_x), Write(axes_label_y), run_time=2.0)
        self.wait(1.0)

        # ----------------------------------------------------------------------
        # 2. Table Header on the Left
        # ----------------------------------------------------------------------
        # Narration: "Let us substitute specific inputs into f(x) = x^2 - 4x + 3 and plot each resulting coordinate."
        table_x_header = MathTex("x", color=COLOR_INPUT, font_size=BODY_FONT_SIZE)
        table_fx_header = MathTex("f(x)", color=COLOR_OUTPUT, font_size=BODY_FONT_SIZE)
        table_pt_header = MathTex("(x, y)", color=COLOR_HIGHLIGHT, font_size=BODY_FONT_SIZE)

        headers = VGroup(table_x_header, table_fx_header, table_pt_header).arrange(RIGHT, buff=0.6)
        headers.shift(LEFT * 4.0 + UP * 2.0)

        div_line = Line(LEFT * 5.5 + UP * 1.6, LEFT * 2.5 + UP * 1.6, color=COLOR_AXES, stroke_width=2)
        self.play(FadeIn(headers), Create(div_line), run_time=1.2)

        # ----------------------------------------------------------------------
        # 3. Step-by-Step Point Evaluation: x in {0, 1, 2, 3, 4}
        # ----------------------------------------------------------------------
        eval_points = [0, 1, 2, 3, 4]
        table_rows = VGroup()
        rendered_dots = []

        curr_y = 1.2
        for x_val in eval_points:
            y_val = f(x_val) # Strict computation from f(x)
            
            # Form row text
            r_x = MathTex(f"{x_val}", color=COLOR_INPUT, font_size=LABEL_FONT_SIZE + 2)
            r_fx = MathTex(f"{int(y_val)}", color=COLOR_OUTPUT, font_size=LABEL_FONT_SIZE + 2)
            r_pt = MathTex(f"({x_val}, {int(y_val)})", color=COLOR_HIGHLIGHT, font_size=LABEL_FONT_SIZE + 2)

            r_x.move_to([LEFT * 4.6][0] + UP * curr_y)
            r_fx.move_to([LEFT * 3.9][0] + UP * curr_y)
            r_pt.move_to([LEFT * 3.0][0] + UP * curr_y)
            row_grp = VGroup(r_x, r_fx, r_pt)
            table_rows.add(row_grp)

            # Coordinate markers
            pt_marker = create_point_marker(
                axes=axes,
                x_val=x_val,
                y_val=y_val,
                dot_color=COLOR_HIGHLIGHT,
                radius=0.07,
                label_text=f"({x_val}, {int(y_val)})",
                direction=DOWN if y_val == -1 else (UP if y_val == 3 and x_val == 0 else RIGHT)
            )

            # Narration comment: "Input x = {x_val} yields output f({x_val}) = {int(y_val)}."
            self.play(FadeIn(row_grp), run_time=0.6)
            self.play(FadeIn(pt_marker), run_time=0.8)
            rendered_dots.append(pt_marker)
            self.wait(0.5)

            curr_y -= 0.45

        # ----------------------------------------------------------------------
        # 4. Adding Boundary Points x = -1 and x = 5
        # ----------------------------------------------------------------------
        # Narration: "Adding boundary inputs x = -1 and x = 5 gives heights of 8, revealing the upward curve."
        for x_val in [-1, 5]:
            y_val = f(x_val)
            pt_bound = create_point_marker(
                axes=axes,
                x_val=x_val,
                y_val=y_val,
                dot_color=COLOR_HIGHLIGHT,
                radius=0.07,
                label_text=f"({x_val}, {int(y_val)})",
                direction=LEFT if x_val == -1 else RIGHT
            )
            self.play(FadeIn(pt_bound), run_time=0.8)
            rendered_dots.append(pt_bound)

        self.wait(1.5)

        # ----------------------------------------------------------------------
        # 5. Continuous Curve with Tracer Dot
        # ----------------------------------------------------------------------
        # Narration: "Connecting every real input between and beyond these points forms our smooth parabola."
        parabola = get_function_curve(axes, x_min=-1.1, x_max=5.1, color=COLOR_GRAPH, stroke_width=4.0)
        tracer_dot = Dot(color=COLOR_HIGHLIGHT, radius=0.09)
        tracer_dot.move_to(axes.c2p(-1.1, f(-1.1)))

        self.play(FadeIn(tracer_dot), run_time=0.5)
        self.play(
            Create(parabola),
            MoveAlongPath(tracer_dot, parabola),
            run_time=4.0,
            rate_func=linear
        )
        self.play(FadeOut(tracer_dot), run_time=0.5)
        self.wait(1.5)

        # ----------------------------------------------------------------------
        # 6. The Vertical Line Test
        # ----------------------------------------------------------------------
        # Narration: "Notice the Vertical Line Test: any vertical line crosses the curve at exactly one point, guaranteeing single output per input."
        v_line = DashedLine(
            start=axes.c2p(-1.0, -1.8),
            end=axes.c2p(-1.0, 8.8),
            color=COLOR_INPUT,
            stroke_width=2.5
        )
        v_test_label = Text("Vertical Line Test (1 Output)", font_size=LABEL_FONT_SIZE, color=COLOR_INPUT)
        v_test_label.to_edge(DOWN, buff=0.4).shift(RIGHT * 2.5)

        self.play(Create(v_line), FadeIn(v_test_label), run_time=1.0)
        
        # Sweep across domain x = -1 to x = 5
        self.play(
            v_line.animate.move_to(axes.c2p(5.0, 3.5)),
            run_time=3.5,
            rate_func=smooth
        )
        self.wait(2.0)

        # Clear Scene
        self.play(
            FadeOut(title), FadeOut(axes), FadeOut(axes_label_x), FadeOut(axes_label_y),
            FadeOut(headers), FadeOut(div_line), FadeOut(table_rows),
            FadeOut(parabola), FadeOut(v_line), FadeOut(v_test_label),
            *[FadeOut(dot) for dot in rendered_dots],
            run_time=1.5
        )
        self.wait(1.0)
