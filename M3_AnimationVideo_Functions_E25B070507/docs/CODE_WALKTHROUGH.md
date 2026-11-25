# Code Walkthrough & Viva Defense Guide

**Course:** Linear Algebra and Calculus (M3)  
**Assessment:** Animation Video — Single-Variable Functions & Graphs  
**Student:** Amrit Anand (ID: E25B070507)  

---

## 1. Project Architecture Overview

The repository is modular and structured cleanly so that all mathematical logic, visual configuration, and scene choreography remain transparent and easy to defend:
```
M3_AnimationVideo_Functions_E25B070507/
  README.md                    (complete documentation and setup guide)
  _Video.mp4                   (final rendered 1080p @ 30 fps MP4)
  Storyboard.md                (6-scene storyboard source document)
  Storyboard.pdf               (6-scene storyboard table & mathematical specs)
  AI_DISCLOSURE.md             (academic integrity disclosure)
  CREDITS.md                   (textbook, software, and music citations)
  docs/
    CODE_WALKTHROUGH.md        (this viva defense guide)
  _Code/
    config.py                  (colors, fonts, resolution, theme palette)
    helpers.py                 (single source of truth f(x), axes, point markers)
    scene1_hook.py             (Hook: real-world battery decay & projectile motion)
    scene2_concept.py          (Concept: function machine, domain & range)
    scene3_intuition.py        (Intuition: evaluation table, plotting, vertical line test)
    scene4_worked_example.py   (Worked Example: y-intercept, roots, vertex via symmetry)
    scene5_interpretation.py   (Interpretation: domain, range, monotonicity intervals)
    scene6_summary.py          (Summary & Credits: 3 takeaways, references, AI disclosure)
    main_video.py              (Master orchestrator with Opening & Closing frames)
    tests/test_math.py         (automated SymPy verification tests)
    generate_storyboard_pdf.py (generates Storyboard.pdf via ReportLab)
    render.sh                  (1080p production render script)
    merge_audio.sh             (FFmpeg narration & background music muxing script)
```

---

## 2. Mathematical Definitions (`helpers.py` & `tests/test_math.py`)

### What does this do?
- Defines the single source of truth for our quadratic function: $f(x) = x^2 - 4x + 3$.
- `TABLE_INPUTS` and `TABLE_DATA` compute the exact pairs programmatically: $(-1, 8)$, $(0, 3)$, $(1, 0)$, $(2, -1)$, $(3, 0)$, $(4, 3)$, $(5, 8)$.
- Key landmarks (`ROOT_1 = 1.0`, `ROOT_2 = 3.0`, `Y_INTERCEPT_Y = f(0.0)`, `VERTEX_Y = f(2.0)`) are derived directly from `f(x)` rather than hardcoded independently.

### How to explain this in the Viva:
> *"To ensure mathematical consistency across all six scenes, the function definition and coordinate evaluations are centralized in `_Code/helpers.py`. Every scene imports `f`, `TABLE_DATA`, `ROOT_1`, `ROOT_2`, and `VERTEX_X`/`VERTEX_Y` from this single source of truth. In addition, `_Code/tests/test_math.py` runs SymPy assertions to verify the roots, y-intercept, vertex, range minimum, and monotonicity intervals."*

---

## 3. Scene-by-Scene Explanation

### Opening & Scene 1: Hook / Context (`main_video.py` & `scene1_hook.py`)
- **Visuals:** Opens with a 5-second title frame showing the course, topic, function $f(x) = x^2 - 4x + 3$, and student details (`Amrit Anand — E25B070507`). Transitions to dual real-world axes: smartphone battery decay $B(t) = 100e^{-0.22t}$ and projectile height $h(t) = -4.9t^2 + 18t$.
- **Viva Explanation:**
  > *"Scene 1 motivates why functions matter in everyday cause-and-effect relationships: at any moment in time $t$, there is a single battery percentage $B(t)$ or a single projectile height $h(t)$. That unique dependence is the core idea of a function."*

---

### Scene 2: Concept Introduction (`scene2_concept.py`)
- **Visuals:** Renders an animated "Function Machine" box. A blue input arrow ($x$) enters from the left, an orange output arrow ($f(x)$) exits to the right. Demonstrates $x = 4 \implies f(4) = 4^2 - 4(4) + 3 = 3$, and displays formal Domain ($\mathbb{R}$) and Range ($[-1, \infty)$) definition cards.
- **Viva Explanation:**
  > *"Scene 2 formalizes a function as a deterministic rule that assigns exactly one output $f(x)$ to each valid input $x$. We distinguish between the domain (the set of allowed inputs, $\mathbb{R}$) and the range (the set of outputs actually achieved, $[-1, \infty)$)."*

---

### Scene 3: Visual Intuition (`scene3_intuition.py`)
- **Visuals:** Split-screen layout with an evaluation table on the left and calibrated 2D axes on the right. Reveals rows for $x \in \{-1, 0, 1, 2, 3, 4, 5\}$ while plotting each $(x, f(x))$ point on the graph, then traces the continuous parabola and sweeps a vertical line across the domain.
- **Viva Explanation:**
  > *"Scene 3 connects arithmetic substitution to 2D geometry. The graph is literally the set of all coordinate pairs $(x, f(x))$. Sweeping the vertical line across the curve visually proves the Vertical Line Test: every vertical line $x = x_0$ intersects the parabola at most once."*

---

### Scene 4: Worked Example (`scene4_worked_example.py`)
- **Visuals:** Two-panel breakdown (algebraic steps on the left, highlighted graph landmarks on the right):
  1. **Y-Intercept:** Evaluates $f(0) = 0^2 - 4(0) + 3 = 3 \implies (0, 3)$.
  2. **Roots / Zeros:** Factors $x^2 - 4x + 3 = (x - 1)(x - 3) = 0 \implies x = 1, 3$.
  3. **Vertex by Symmetry:** Computes $x_v = \frac{1 + 3}{2} = 2$, $f(2) = -1 \implies (2, -1)$ on the axis of symmetry $x = 2$.
- **Viva Explanation:**
  > *"Scene 4 shows how to extract all key graphical landmarks algebraically and verify them on the plot. Setting $x=0$ gives the y-intercept, factoring gives the x-intercepts, and symmetry halfway between the roots locates the vertex $(2, -1)$."*

---

### Scene 5: Interpretation (`scene5_interpretation.py`)
- **Visuals:** Shades the $x$-axis in blue across $(-\infty, \infty)$ for the domain and the $y$-axis in orange for $[-1, \infty)$ for the range. Splits the parabola at $x = 2$: the left branch $(-\infty, 2)$ is highlighted as decreasing and the right branch $(2, \infty)$ as increasing.
- **Viva Explanation:**
  > *"Scene 5 reads global calculus properties directly from the graph. Because the parabola extends endlessly left and right, the domain is $(-\infty, \infty)$. Because the vertex $(2, -1)$ is a global minimum, the range is $[-1, \infty)$. Moving left to right, $f(x)$ decreases until $x = 2$ and increases thereafter."*

---

### Scene 6: Summary & Credits (`scene6_summary.py`)
- **Visuals:** Displays three sequential takeaway cards (unique output rule, graph as $(x, f(x))$, reading algebraic landmarks), followed by textbook citations, software credits, and the AI disclosure statement.
- **Viva Explanation:**
  > *"Scene 6 consolidates the three core takeaways and provides complete academic attribution."*

---

## 4. Common Viva Questions & Model Answers

**Q1: Why did you choose $f(x) = x^2 - 4x + 3$?**  
*Answer:* It factors cleanly over the integers into $(x - 1)(x - 3)$, has an integer vertex at $(2, -1)$, a clean y-intercept at $(0, 3)$, and integer table values from $x = -1$ to $x = 5$. This keeps on-screen arithmetic transparent while still demonstrating roots, symmetry, extrema, bounded range, and monotonicity intervals.

**Q2: How do you prove that $(2, -1)$ is the minimum without calculus, and with calculus?**  
*Answer:* Without calculus, the parabola opens upward and is symmetric about the midpoint of its roots, $x_v = \frac{1 + 3}{2} = 2$, or by completing the square: $f(x) = (x - 2)^2 - 1 \ge -1$. With calculus, $f'(x) = 2x - 4 = 0 \implies x = 2$, and $f''(2) = 2 > 0$ confirms a global minimum at $(2, -1)$.

**Q3: Is $f(x) = x^2 - 4x + 3$ a one-to-one (injective) function on $\mathbb{R}$?**  
*Answer:* No. For example, $f(1) = 0$ and $f(3) = 0$, and $f(0) = f(4) = 3$. Two distinct inputs produce the same output, which fails the Horizontal Line Test for $y > -1$.
