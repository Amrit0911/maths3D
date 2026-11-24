"""
scene6_summary.py
-----------------
Scene 6: Summary, Takeaways & Credits (Target Duration: ~30 seconds)
Recaps 3 core mathematical takeaways sequentially:
  1. Function Definition: Each input x has exactly one output f(x).
  2. The Graph: Ordered pairs (x, f(x)) visualizing relationships.
  3. Landmark Reading: Reading roots, intercept, vertex, and range directly from the graph.
Followed by closing credits, reference literature, and AI disclosure.
"""

from manim import *
from config import *
from helpers import *

class Scene6Summary(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        # ----------------------------------------------------------------------
        # 1. Takeaways Header
        # ----------------------------------------------------------------------
        # Narration: "To conclude, let us review the three core principles we uncovered today."
        title = Text("Key Takeaways", font_size=TITLE_FONT_SIZE, color=COLOR_HIGHLIGHT)
        title.to_edge(UP, buff=0.8)
        self.play(FadeIn(title), run_time=1.0)
        self.wait(0.5)

        # ----------------------------------------------------------------------
        # 2. Three Sequential Takeaway Cards
        # ----------------------------------------------------------------------
        box_w, box_h = 10.5, 1.1

        # Takeaway 1
        # Narration: "One: A function is a deterministic rule giving exactly one output per input."
        card1 = RoundedRectangle(corner_radius=0.15, height=box_h, width=box_w, color=COLOR_INPUT, fill_color=COLOR_BOX, fill_opacity=0.9)
        card1.shift(UP * 1.3)
        t1 = Text("1. Unique Output: Each input x has exactly one f(x) (Vertical Line Test).", font_size=BODY_FONT_SIZE - 2, color=COLOR_TEXT).move_to(card1)

        self.play(FadeIn(card1), Write(t1), run_time=1.2)
        self.wait(3.5)

        # Takeaway 2
        # Narration: "Two: The graph is the complete geometric assembly of all pairs (x, f(x))."
        card2 = RoundedRectangle(corner_radius=0.15, height=box_h, width=box_w, color=COLOR_GRAPH, fill_color=COLOR_BOX, fill_opacity=0.9)
        card2.shift(DOWN * 0.1)
        t2 = Text("2. Graph as Geometry: The curve represents all ordered pairs (x, f(x)).", font_size=BODY_FONT_SIZE - 2, color=COLOR_TEXT).move_to(card2)

        self.play(FadeIn(card2), Write(t2), run_time=1.2)
        self.wait(3.5)

        # Takeaway 3
        # Narration: "Three: Algebra and geometry mirror each other: roots, intercepts, and extrema are visible landmarks."
        card3 = RoundedRectangle(corner_radius=0.15, height=box_h, width=box_w, color=COLOR_HIGHLIGHT, fill_color=COLOR_BOX, fill_opacity=0.9)
        card3.shift(DOWN * 1.5)
        t3 = Text("3. Analytical Power: Roots, intercepts, vertex, and range can be read directly.", font_size=BODY_FONT_SIZE - 2, color=COLOR_TEXT).move_to(card3)

        self.play(FadeIn(card3), Write(t3), run_time=1.2)
        self.wait(5.0)

        # ----------------------------------------------------------------------
        # 3. Credits & AI Disclosure Frame
        # ----------------------------------------------------------------------
        # Clear takeaways
        self.play(
            FadeOut(title), FadeOut(card1), FadeOut(t1),
            FadeOut(card2), FadeOut(t2), FadeOut(card3), FadeOut(t3),
            run_time=1.2
        )

        # Narration: "Thank you for watching. This animation was created with Manim Community Edition."
        credits_title = Text("Credits & Academic References", font_size=SUBTITLE_FONT_SIZE + 4, color=COLOR_HIGHLIGHT).to_edge(UP, buff=0.8)
        
        c1 = Text("Course: Linear Algebra and Calculus (M3) - Internal Assessment", font_size=BODY_FONT_SIZE - 2, color=COLOR_TEXT)
        c2 = Text("Topic: Single-variable functions and graphs | f(x) = x^2 - 4x + 3", font_size=BODY_FONT_SIZE - 2, color=COLOR_TEXT)
        c3 = Text("Reference: Stewart, J. (2015). Calculus: Early Transcendentals (8th ed.)", font_size=LABEL_FONT_SIZE, color=COLOR_SUBTEXT)
        c4 = Text("Music: 'Gymnopedie No. 1' by Erik Satie (Royalty Free / Public Domain)", font_size=LABEL_FONT_SIZE, color=COLOR_SUBTEXT)
        c5 = Text("AI Disclosure: Visual scripting & math choreography assisted by Claude / Google Antigravity.", font_size=LABEL_FONT_SIZE, color=COLOR_HIGHLIGHT)

        credits_group = VGroup(c1, c2, c3, c4, c5).arrange(DOWN, buff=0.35).next_to(credits_title, DOWN, buff=0.6)

        self.play(FadeIn(credits_title), FadeIn(credits_group), run_time=2.0)
        self.wait(7.2)

        self.play(FadeOut(credits_title), FadeOut(credits_group), run_time=1.5)
        self.wait(1.0)
