"""
config.py
---------
Shared visual constants, color palettes, typography, and styling parameters
for the Manim animation video: "Single-variable functions and graphs".
Strictly conforms to standard 16:9 1080p rendering (1920x1080).
"""

# ==============================================================================
# COLOR PALETTE (Strictly consistent throughout all 6 scenes)
# ==============================================================================
# User Rule: inputs = blue, outputs = orange, graph = green, highlights = yellow
COLOR_BG = "#0f111a"             # Deep elegant navy-dark background
COLOR_TEXT = "#E2E8F0"           # Crisp soft white for main text / descriptions
COLOR_SUBTEXT = "#94A3B8"        # Subtle slate gray for secondary commentary

COLOR_INPUT = "#38BDF8"          # Blue (inputs, x-coordinates, horizontal projections)
COLOR_OUTPUT = "#FB923C"         # Orange (outputs, y-coordinates, f(x), vertical projections)
COLOR_GRAPH = "#4ADE80"          # Green (function curve, parabola)
COLOR_HIGHLIGHT = "#FACC15"      # Yellow (key takeaways, critical focal points)

COLOR_AXES = "#64748B"           # Slate for axis lines and tick marks
COLOR_DECREASING = "#F87171"     # Soft Coral Red for decreasing slope/interval
COLOR_INCREASING = "#34D399"     # Emerald Green for increasing slope/interval
COLOR_BOX = "#1E293B"            # Container / Machine fill color
COLOR_BOX_BORDER = "#60A5FA"     # Machine container accent border

# ==============================================================================
# FONT & TEXT SIZES (Optimized for 1080p legibility)
# ==============================================================================
TITLE_FONT_SIZE = 42
SUBTITLE_FONT_SIZE = 28
BODY_FONT_SIZE = 24
MATH_FONT_SIZE = 32
LABEL_FONT_SIZE = 20
NOTE_FONT_SIZE = 18

# ==============================================================================
# GRAPHING & AXIS CONFIGURATION
# ==============================================================================
X_MIN, X_MAX, X_STEP = -2.5, 6.0, 1.0
Y_MIN, Y_MAX, Y_STEP = -2.5, 9.5, 1.0

# Scale factors for axes fitting into 16:9 canvas cleanly
AXES_WIDTH = 9.0
AXES_HEIGHT = 6.2

