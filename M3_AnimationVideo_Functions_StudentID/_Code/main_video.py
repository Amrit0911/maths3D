"""
main_video.py
-------------
Master Orchestrator Scene: MainVideo
Compiles and sequences all 6 scenes into a seamless ~5-minute 1080p video.
Includes:
  - Opening Frame (5s): Title, concept subtitle, student metadata placeholders
  - Scene 1: Hook (35s)
  - Scene 2: Concept Intro (50s)
  - Scene 3: Visual Intuition (75s)
  - Scene 4: Worked Example (75s)
  - Scene 5: Interpretation (40s)
  - Scene 6: Summary & Credits (30s)
Total Run Time: ~310 seconds (~5 min 10 sec), well within the 7-minute ceiling.
"""

from manim import *
from config import *
from helpers import *

# Import individual scene classes
from scene1_hook import Scene1Hook
from scene2_concept import Scene2Concept
from scene3_intuition import Scene3Intuition
from scene4_worked_example import Scene4WorkedExample
from scene5_interpretation import Scene5Interpretation
from scene6_summary import Scene6Summary

class MainVideo(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        # ======================================================================
        # OPENING FRAME (5 seconds)
        # ======================================================================
        # Narration: "Welcome. Today we explore single-variable functions and their graphs through the quadratic f(x) = x squared minus 4x plus 3."
        op_title = Text("Functions and Their Graphs", font_size=TITLE_FONT_SIZE + 6, color=COLOR_HIGHLIGHT)
        op_subtitle = MathTex(r"f(x) = x^2 - 4x + 3", font_size=MATH_FONT_SIZE + 8, color=COLOR_GRAPH)
        op_course = Text("Linear Algebra and Calculus (M3) • Internal Assessment Project", font_size=LABEL_FONT_SIZE + 2, color=COLOR_TEXT)
        op_meta = Text("Student Name: [Your Name Here]   |   Student ID: [StudentID]", font_size=LABEL_FONT_SIZE, color=COLOR_SUBTEXT)

        op_group = VGroup(op_title, op_subtitle, op_course, op_meta).arrange(DOWN, buff=0.45)

        self.play(FadeIn(op_group, shift=UP * 0.3), run_time=1.5)
        self.wait(2.5)
        self.play(FadeOut(op_group, shift=DOWN * 0.3), run_time=1.0)

        # ======================================================================
        # SCENE 1: HOOK (~35s)
        # ======================================================================
        Scene1Hook.construct(self)

        # ======================================================================
        # SCENE 2: CONCEPT INTRO (~50s)
        # ======================================================================
        Scene2Concept.construct(self)

        # ======================================================================
        # SCENE 3: VISUAL INTUITION (~75s)
        # ======================================================================
        Scene3Intuition.construct(self)

        # ======================================================================
        # SCENE 4: WORKED EXAMPLE (~75s)
        # ======================================================================
        Scene4WorkedExample.construct(self)

        # ======================================================================
        # SCENE 5: INTERPRETATION (~40s)
        # ======================================================================
        Scene5Interpretation.construct(self)

        # ======================================================================
        # SCENE 6: SUMMARY & CREDITS (~30s)
        # ======================================================================
        Scene6Summary.construct(self)
