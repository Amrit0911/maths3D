"""
Mathematical Verification Tests for M3 Animation Video
Verifies all algebraic and numerical claims for f(x) = x^2 - 4x + 3 using SymPy.
Course: Linear Algebra and Calculus (M3)
"""

import sys
from pathlib import Path
import sympy as sp

# Add _Code directory to path
CODE_DIR = Path(__file__).resolve().parent.parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from helpers import (
    f,
    ROOT_1,
    ROOT_2,
    Y_INTERCEPT_X,
    Y_INTERCEPT_Y,
    VERTEX_X,
    VERTEX_Y,
    TABLE_DATA,
)

x_sym = sp.Symbol("x", real=True)
f_sympy = x_sym**2 - 4 * x_sym + 3


def test_table_evaluations():
    """Verify all table values for x in {-1, 0, 1, 2, 3, 4, 5}."""
    expected = {
        -1: 8,
        0: 3,
        1: 0,
        2: -1,
        3: 0,
        4: 3,
        5: 8,
    }
    for x_val, y_val in TABLE_DATA:
        assert y_val == expected[x_val]
        assert f(x_val) == expected[x_val]
        assert f_sympy.subs(x_sym, x_val) == expected[x_val]


def test_y_intercept():
    """Verify y-intercept is (0, 3)."""
    assert Y_INTERCEPT_X == 0.0
    assert Y_INTERCEPT_Y == 3.0
    assert f_sympy.subs(x_sym, 0) == 3


def test_roots():
    """Verify roots of f(x) = x^2 - 4x + 3 are exactly {1, 3}."""
    roots = sp.solve(f_sympy, x_sym)
    assert set(roots) == {1, 3}
    assert {ROOT_1, ROOT_2} == {1.0, 3.0}
    assert sp.factor(f_sympy) == (x_sym - 1) * (x_sym - 3)


def test_vertex_and_symmetry():
    """Verify vertex at (2, -1) via symmetry and derivative."""
    assert VERTEX_X == (ROOT_1 + ROOT_2) / 2.0 == 2.0
    assert VERTEX_Y == f(VERTEX_X) == -1.0

    # Derivative check
    df = sp.diff(f_sympy, x_sym)
    d2f = sp.diff(df, x_sym)
    crit_pts = sp.solve(df, x_sym)
    assert crit_pts == [2]
    assert f_sympy.subs(x_sym, 2) == -1
    assert d2f.subs(x_sym, 2) > 0

    # Symmetry about x = 2: f(2 + h) == f(2 - h)
    h = sp.Symbol("h", real=True)
    assert sp.simplify(f_sympy.subs(x_sym, 2 + h) - f_sympy.subs(x_sym, 2 - h)) == 0


def test_monotonicity_and_range():
    """Verify decreasing on (-oo, 2), increasing on (2, oo), and range [-1, oo)."""
    df = sp.diff(f_sympy, x_sym)
    assert sp.simplify(df - (2 * x_sym - 4)) == 0
    assert sp.ask(sp.Q.negative(df.subs(x_sym, 0)))
    assert sp.ask(sp.Q.positive(df.subs(x_sym, 4)))
    # Completed square form (x - 2)^2 - 1 >= -1
    assert sp.simplify(f_sympy - ((x_sym - 2) ** 2 - 1)) == 0
    assert sp.limit(f_sympy, x_sym, sp.oo) == sp.oo
    assert sp.limit(f_sympy, x_sym, -sp.oo) == sp.oo
