"""
scene2_concept.py
-----------------
Scene 2: Concept Introduction & Function Machine (Target Duration: ~50 seconds)
Introduces the formal definition of a function using an animated 'Function Machine'.
Inputs (blue) enter from the left; the rule executes internally; outputs (orange) emerge right.
Defines:
  - Quadratic rule: f(x) = x^2 - 4x + 3
  - Domain (all valid inputs x in R)
  - Range (set of all resulting outputs f(x) >= -1)
"""

from manim import *
from config import *
from helpers import *

class Scene2Concept(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        # ----------------------------------------------------------------------
        # 1. Section Title
        # ----------------------------------------------------------------------
        # Narration: "Formally, a function f is a rule that assigns to each input x exactly one output f(x)."
        title = Text("The Concept of a Function", font_size=TITLE_FONT_SIZE, color=COLOR_HIGHLIGHT)
        title.to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=1.5)
        self.wait(4.0)

        # ----------------------------------------------------------------------
        # 2. The Function Machine Visual Box
        # ----------------------------------------------------------------------
        # Narration: "Imagine a deterministic machine: you drop an input into the slot, and a single output emerges."
        machine_box = RoundedRectangle(
            corner_radius=0.25,
            height=2.8,
            width=5.0,
            color=COLOR_BOX_BORDER,
            fill_color=COLOR_BOX,
            fill_opacity=0.9,
            stroke_width=3
        ).shift(UP * 0.2)

        machine_title = Text("Function Machine", font_size=BODY_FONT_SIZE, color=COLOR_SUBTEXT).next_to(machine_box.get_top(), DOWN, buff=0.25)
        rule_formula = MathTex("f(x) = x^2 - 4x + 3", font_size=MATH_FONT_SIZE + 4, color=COLOR_HIGHLIGHT).move_to(machine_box.get_center() + DOWN * 0.1)

        input_arrow = Arrow(LEFT * 5.5 + UP * 0.2, machine_box.get_left(), buff=0.1, color=COLOR_INPUT, stroke_width=5)
        input_label = Text("Input x", font_size=LABEL_FONT_SIZE + 2, color=COLOR_INPUT).next_to(input_arrow, UP, buff=0.15)

        output_arrow = Arrow(machine_box.get_right(), RIGHT * 5.5 + UP * 0.2, buff=0.1, color=COLOR_OUTPUT, stroke_width=5)
        output_label = Text("Output f(x)", font_size=LABEL_FONT_SIZE + 2, color=COLOR_OUTPUT).next_to(output_arrow, UP, buff=0.15)

        self.play(
            Create(machine_box),
            FadeIn(machine_title),
            Write(rule_formula),
            Create(input_arrow),
            FadeIn(input_label),
            Create(output_arrow),
            FadeIn(output_label),
            run_time=2.5
        )
        self.wait(7.0)

        # ----------------------------------------------------------------------
        # 3. Particle Flow Animation: Demonstrating an Example (x = 4 -> f(4) = 3)
        # ----------------------------------------------------------------------
        # Narration: "For instance, if we feed in x = 4, the machine squares it, subtracts four times four, and adds three."
        token_in = MathTex("x = 4", font_size=BODY_FONT_SIZE, color=COLOR_INPUT)
        token_in.move_to(LEFT * 5.2 + UP * 0.2)

        self.play(FadeIn(token_in, shift=RIGHT * 0.5), run_time=1.0)
        self.play(token_in.animate.move_to(machine_box.get_center()), run_time=1.8)
        self.play(FadeOut(token_in), Flash(machine_box, color=COLOR_HIGHLIGHT, flash_radius=1.5), run_time=0.8)

        # Output calculation: f(4) = 4^2 - 4(4) + 3 = 3
        # Narration: "Out comes a single definite output: f(4) = 3."
        token_out = MathTex("f(4) = 3", font_size=BODY_FONT_SIZE, color=COLOR_OUTPUT)
        token_out.move_to(machine_box.get_center())

        self.play(FadeIn(token_out), run_time=0.6)
        self.play(token_out.animate.move_to(RIGHT * 4.2 + UP * 0.2), run_time=1.8)
        self.wait(6.5)

        # ----------------------------------------------------------------------
        # 4. Formal Definitions: Domain and Range
        # ----------------------------------------------------------------------
        # Narration: "Every function has two fundamental sets: its Domain of valid inputs, and its Range of possible outputs."
        def_card = RoundedRectangle(
            corner_radius=0.15,
            height=2.0,
            width=11.5,
            color=COLOR_AXES,
            fill_color=COLOR_BOX,
            fill_opacity=0.9
        ).to_edge(DOWN, buff=0.5)

        domain_label = Text("Domain:", font_size=BODY_FONT_SIZE, color=COLOR_INPUT, weight=BOLD)
        domain_desc = Text("Set of all permitted inputs x  |  Here, x in R (all real numbers)", font_size=BODY_FONT_SIZE - 2, color=COLOR_TEXT)
        domain_row = VGroup(domain_label, domain_desc).arrange(RIGHT, buff=0.3)

        range_label = Text("Range:", font_size=BODY_FONT_SIZE, color=COLOR_OUTPUT, weight=BOLD)
        range_desc = Text("Set of all attainable outputs f(x)  |  Here, f(x) >= -1, [-1, inf)", font_size=BODY_FONT_SIZE - 2, color=COLOR_TEXT)
        range_row = VGroup(range_label, range_desc).arrange(RIGHT, buff=0.3)

        def_content = VGroup(domain_row, range_row).arrange(DOWN, buff=0.25).move_to(def_card.get_center())

        self.play(FadeIn(def_card), FadeIn(def_content), run_time=2.0)
        self.wait(18.0)

        # Clear Scene
        self.play(
            FadeOut(title),
            FadeOut(machine_box), FadeOut(machine_title), FadeOut(rule_formula),
            FadeOut(input_arrow), FadeOut(input_label),
            FadeOut(output_arrow), FadeOut(output_label), FadeOut(token_out),
            FadeOut(def_card), FadeOut(def_content),
            run_time=1.5
        )
        self.wait(1.0)
