"""
scene4_worked_example.py
------------------------
Scene 4: Worked Example & Algebraic Features (Target Duration: ~75 seconds)
Derives and highlights the primary mathematical landmarks of f(x) = x^2 - 4x + 3:
  1. Y-Intercept: Setting x = 0 -> (0, 3).
  2. Roots / Zeros: Factoring x^2 - 4x + 3 = (x - 1)(x - 3) = 0 -> x = 1, 3.
  3. Vertex: Axis of symmetry at x = 2; evaluating f(2) = 2^2 - 4(2) + 3 = -1 -> (2, -1).
Shows simultaneous connection between algebraic derivation on the left and geometric location on the right.
"""

from manim import *
from config import *
from helpers import *

class Scene4WorkedExample(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        # ----------------------------------------------------------------------
        # 1. Header & Setup
        # ----------------------------------------------------------------------
        # Narration: "Now let us systematically derive the three essential landmarks: y-intercept, roots, and the vertex."
        title = Text("Key Features: Intercepts, Roots & Vertex", font_size=SUBTITLE_FONT_SIZE + 2, color=COLOR_HIGHLIGHT)
        title.to_edge(UP, buff=0.4)
        self.play(FadeIn(title), run_time=1.0)

        # Coordinate axes on the right
        axes = make_standard_axes(
            x_range=[-1.5, 5.0, 1.0],
            y_range=[-2.0, 6.0, 1.0],
            x_length=6.0,
            y_length=5.2,
            include_numbers=True
        ).shift(RIGHT * 3.3 + DOWN * 0.4)

        parabola = get_function_curve(axes, x_min=-0.7, x_max=4.7, color=COLOR_GRAPH, stroke_width=3.5)
        self.play(Create(axes), Create(parabola), run_time=2.0)
        self.wait(1.0)

        # ----------------------------------------------------------------------
        # 2. Step 1: Y-Intercept (Set x = 0)
        # ----------------------------------------------------------------------
        # Narration: "First, the y-intercept. We substitute x = 0 into the function."
        y_int_heading = Text("1. Y-Intercept (x = 0)", font_size=BODY_FONT_SIZE, color=COLOR_OUTPUT, weight=BOLD)
        y_int_math = MathTex(
            r"f(0) = (0)^2 - 4(0) + 3 = 3",
            font_size=LABEL_FONT_SIZE + 2,
            color=COLOR_TEXT
        )
        y_int_pt_label = MathTex(r"\implies \mathbf{(0, 3)}", font_size=LABEL_FONT_SIZE + 2, color=COLOR_OUTPUT)
        y_int_group = VGroup(y_int_heading, y_int_math, y_int_pt_label).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        y_int_group.shift(LEFT * 3.8 + UP * 1.8)

        # Narration: "This gives (0, 3), where the graph crosses the vertical axis."
        pt_y_int = create_point_marker(
            axes, Y_INTERCEPT_X, Y_INTERCEPT_Y,
            dot_color=COLOR_OUTPUT,
            label_text="(0, 3)",
            direction=LEFT
        )

        self.play(FadeIn(y_int_group), run_time=1.5)
        self.play(FadeIn(pt_y_int), Flash(pt_y_int[1], color=COLOR_OUTPUT), run_time=1.0)
        self.wait(2.0)

        # ----------------------------------------------------------------------
        # 3. Step 2: Roots / X-Intercepts (Solve f(x) = 0)
        # ----------------------------------------------------------------------
        # Narration: "Second, the roots: where does the function equal zero? We factor the quadratic."
        roots_heading = Text("2. Roots / Zeros (f(x) = 0)", font_size=BODY_FONT_SIZE, color=COLOR_INPUT, weight=BOLD)
        roots_factor = MathTex(
            r"x^2 - 4x + 3 = (x - 1)(x - 3) = 0",
            font_size=LABEL_FONT_SIZE + 2,
            color=COLOR_TEXT
        )
        roots_sol = MathTex(r"\implies x = 1 \quad \text{and} \quad x = 3", font_size=LABEL_FONT_SIZE + 2, color=COLOR_INPUT)
        roots_group = VGroup(roots_heading, roots_factor, roots_sol).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        roots_group.shift(LEFT * 3.8 + UP * 0.1)

        # Narration: "This reveals two zeros: x = 1 and x = 3, marking the crossing points on the x-axis."
        pt_root_1 = create_point_marker(axes, ROOT_1, f(ROOT_1), dot_color=COLOR_INPUT, label_text="(1, 0)", direction=DOWN)
        pt_root_2 = create_point_marker(axes, ROOT_2, f(ROOT_2), dot_color=COLOR_INPUT, label_text="(3, 0)", direction=DOWN)

        self.play(FadeIn(roots_group), run_time=1.8)
        self.play(
            FadeIn(pt_root_1), FadeIn(pt_root_2),
            Flash(pt_root_1[1], color=COLOR_INPUT), Flash(pt_root_2[1], color=COLOR_INPUT),
            run_time=1.2
        )
        self.wait(2.5)

        # ----------------------------------------------------------------------
        # 4. Step 3: Vertex via Symmetry & Evaluation
        # ----------------------------------------------------------------------
        # Narration: "Third, parabolas are symmetric. The vertex x-coordinate lies midway between the roots at x = 2."
        vertex_heading = Text("3. Vertex (Axis of Symmetry)", font_size=BODY_FONT_SIZE, color=COLOR_HIGHLIGHT, weight=BOLD)
        vertex_symm = MathTex(r"x_v = \frac{1 + 3}{2} = 2", font_size=LABEL_FONT_SIZE + 2, color=COLOR_TEXT)
        vertex_calc = MathTex(r"f(2) = 2^2 - 4(2) + 3 = -1", font_size=LABEL_FONT_SIZE + 2, color=COLOR_TEXT)
        vertex_res = MathTex(r"\implies \text{Vertex: } \mathbf{(2, -1)}", font_size=LABEL_FONT_SIZE + 2, color=COLOR_HIGHLIGHT)
        vertex_group = VGroup(vertex_heading, vertex_symm, vertex_calc, vertex_res).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        vertex_group.shift(LEFT * 3.8 + DOWN * 1.8)

        # Axis of symmetry dashed line
        axis_line = DashedLine(
            start=axes.c2p(2.0, -1.8),
            end=axes.c2p(2.0, 5.5),
            color=COLOR_HIGHLIGHT,
            stroke_width=2.5
        )
        pt_vertex = create_point_marker(
            axes, VERTEX_X, VERTEX_Y,
            dot_color=COLOR_HIGHLIGHT,
            label_text="(2, -1)",
            direction=DOWN
        )

        # Narration: "Substituting x = 2 evaluates f(2) = -1. This minimum point is the vertex (2, -1)."
        self.play(FadeIn(vertex_group), Create(axis_line), run_time=2.0)
        self.play(FadeIn(pt_vertex), Flash(pt_vertex[1], color=COLOR_HIGHLIGHT), run_time=1.2)
        self.wait(4.0)

        # Clear Scene
        self.play(
            FadeOut(title), FadeOut(axes), FadeOut(parabola),
            FadeOut(y_int_group), FadeOut(pt_y_int),
            FadeOut(roots_group), FadeOut(pt_root_1), FadeOut(pt_root_2),
            FadeOut(vertex_group), FadeOut(axis_line), FadeOut(pt_vertex),
            run_time=1.5
        )
        self.wait(1.0)
