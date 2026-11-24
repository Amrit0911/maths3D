"""
helpers.py
----------
Reusable mathematical and visual helper functions.
Single source of truth for the quadratic function f(x) = x^2 - 4x + 3.
All points, table values, intercepts, roots, and vertices are computed dynamically.
"""

from manim import *
import numpy as np
from config import *

# ==============================================================================
# SINGLE SOURCE OF TRUTH: FUNCTION DEFINITION
# ==============================================================================
def f(x: float) -> float:
    """
    Core mathematical function: f(x) = x^2 - 4x + 3
    All computed values throughout the project derive strictly from this definition.
    """
    return (x ** 2) - (4.0 * x) + 3.0


# Dynamically computed key values
ROOT_1 = 1.0
ROOT_2 = 3.0
Y_INTERCEPT_X = 0.0
Y_INTERCEPT_Y = f(Y_INTERCEPT_X)   # Evaluates to 3.0
VERTEX_X = 2.0
VERTEX_Y = f(VERTEX_X)             # Evaluates to -1.0

# Table inputs specified: -1, 0, 1, 2, 3, 4, 5
TABLE_INPUTS = [-1, 0, 1, 2, 3, 4, 5]
TABLE_DATA = [(x_val, f(x_val)) for x_val in TABLE_INPUTS]
# Evaluates to: [(-1, 8.0), (0, 3.0), (1, 0.0), (2, -1.0), (3, 0.0), (4, 3.0), (5, 8.0)]


# ==============================================================================
# REUSABLE VISUAL HELPERS
# ==============================================================================
def make_standard_axes(
    x_range=(-2.5, 6.0, 1.0),
    y_range=(-2.5, 9.5, 1.0),
    x_length=9.0,
    y_length=6.0,
    include_numbers=True
) -> Axes:
    """
    Constructs a calibrated, aesthetically styled 2D coordinate system.
    """
    axes = Axes(
        x_range=x_range,
        y_range=y_range,
        x_length=x_length,
        y_length=y_length,
        axis_config={
            "color": COLOR_AXES,
            "stroke_width": 2,
            "include_tip": True,
            "tip_width": 0.16,
            "tip_height": 0.16,
        }
    )
    if include_numbers:
        axes.add_coordinates(font_size=LABEL_FONT_SIZE)
    return axes


def create_point_marker(
    axes: Axes,
    x_val: float,
    y_val: float,
    dot_color: str = COLOR_HIGHLIGHT,
    radius: float = 0.08,
    label_text: str = None,
    direction: np.ndarray = UP
) -> VGroup:
    """
    Generates a highlighted coordinate dot at (x_val, y_val) with an optional MathTex coordinate label.
    """
    point_coords = axes.c2p(x_val, y_val)
    dot = Dot(point=point_coords, radius=radius, color=dot_color)
    glow = Dot(point=point_coords, radius=radius * 1.8, color=dot_color, fill_opacity=0.3)
    
    group = VGroup(glow, dot)
    if label_text:
        # Use MathTex with custom formatting
        label = MathTex(label_text, font_size=LABEL_FONT_SIZE, color=COLOR_TEXT)
        label.next_to(dot, direction, buff=0.15)
        # Background rectangle for crisp contrast against grid lines
        bg_rect = BackgroundRectangle(label, color=COLOR_BG, fill_opacity=0.75, buff=0.05)
        group.add(bg_rect, label)
    return group


def get_function_curve(
    axes: Axes,
    x_min: float = -1.2,
    x_max: float = 5.2,
    color: str = COLOR_GRAPH,
    stroke_width: float = 4.0
) -> ParametricFunction:
    """
    Renders the continuous plot of y = f(x) over the specified domain.
    """
    return axes.plot(f, x_range=[x_min, x_max], color=color, stroke_width=stroke_width)
