"""
Generate Storyboard.pdf from Storyboard.md using ReportLab.
Produces a professional university assessment PDF document.
"""

from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


def generate_storyboard_pdf(output_pdf_path: Path):
    doc = SimpleDocTemplate(
        str(output_pdf_path),
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40,
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "DocTitle",
        parent=styles["Heading1"],
        fontSize=22,
        leading=26,
        textColor=colors.HexColor("#0F172A"),
        spaceAfter=6,
    )
    subtitle_style = ParagraphStyle(
        "DocSub",
        parent=styles["Normal"],
        fontSize=11,
        leading=15,
        textColor=colors.HexColor("#475569"),
        spaceAfter=14,
    )
    h2_style = ParagraphStyle(
        "Heading2",
        parent=styles["Heading2"],
        fontSize=14,
        leading=18,
        textColor=colors.HexColor("#1E293B"),
        spaceBefore=12,
        spaceAfter=6,
    )
    callout_style = ParagraphStyle(
        "Callout",
        parent=styles["Normal"],
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#0F172A"),
        backColor=colors.HexColor("#F1F5F9"),
        borderColor=colors.HexColor("#3B82F6"),
        borderWidth=1,
        borderPadding=8,
        spaceAfter=10,
    )
    table_text = ParagraphStyle(
        "TableText",
        parent=styles["Normal"],
        fontSize=8,
        leading=11,
        textColor=colors.HexColor("#1E293B"),
    )
    table_header = ParagraphStyle(
        "TableHeader",
        parent=styles["Normal"],
        fontSize=8.5,
        leading=11,
        fontName="Helvetica-Bold",
        textColor=colors.white,
    )

    story = []

    # Title & Metadata
    story.append(Paragraph("M3 Animation Video: Storyboard & Specification", title_style))
    story.append(
        Paragraph(
            "<b>Course:</b> Linear Algebra & Calculus (M3) &nbsp;|&nbsp; "
            "<b>Student:</b> Amrit Anand (ID: E25B070507) &nbsp;|&nbsp; "
            "<b>Example:</b> f(x) = x² - 4x + 3",
            subtitle_style,
        )
    )
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#3B82F6"), spaceAfter=12))

    # Learning Objective Box
    story.append(
        Paragraph(
            "<b>Learning Objective:</b> By the end of this video, the viewer will be able to explain that a "
            "single-variable function assigns exactly one output to each input, understand that the graph is "
            "the set of points (x, f(x)), and systematically read roots, y-intercept, vertex, domain, range, "
            "and increasing/decreasing intervals directly from the graph.<br/><br/>"
            "<b>Target Duration:</b> ~5 minutes 10 seconds (310 seconds total) &nbsp;|&nbsp; "
            "<b>Format:</b> 1080p Full HD (1920×1080), 30 fps",
            callout_style,
        )
    )

    # Hand-checked Values Table
    story.append(Paragraph("1. Hand-Checked Values for Viva Defense (All analytically verified)", h2_style))

    math_table_data = [
        [
            Paragraph("x", table_header),
            Paragraph("-1", table_header),
            Paragraph("0", table_header),
            Paragraph("1", table_header),
            Paragraph("2", table_header),
            Paragraph("3", table_header),
            Paragraph("4", table_header),
            Paragraph("5", table_header),
        ],
        [
            Paragraph("<b>f(x) = x² - 4x + 3</b>", table_text),
            Paragraph("<b>8</b>", table_text),
            Paragraph("<b>3</b>", table_text),
            Paragraph("<b>0</b>", table_text),
            Paragraph("<b>-1</b>", table_text),
            Paragraph("<b>0</b>", table_text),
            Paragraph("<b>3</b>", table_text),
            Paragraph("<b>8</b>", table_text),
        ],
        [
            Paragraph("Feature Note", table_text),
            Paragraph("Left bound", table_text),
            Paragraph("y-intercept", table_text),
            Paragraph("Root (x₁)", table_text),
            Paragraph("Vertex (Min)", table_text),
            Paragraph("Root (x₂)", table_text),
            Paragraph("Symm. pair", table_text),
            Paragraph("Right bound", table_text),
        ],
    ]

    t_math = Table(math_table_data, colWidths=[110, 60, 60, 60, 60, 60, 60, 60])
    t_math.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1E293B")),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#F8FAFC"), colors.HexColor("#EDF2F7")]),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    story.append(t_math)
    story.append(Spacer(1, 14))

    # 6 Scenes Storyboard Table
    story.append(Paragraph("2. Detailed 6-Scene Storyboard (plus Opening Frame)", h2_style))

    scene_data = [
        [
            Paragraph("#", table_header),
            Paragraph("Scene", table_header),
            Paragraph("Duration", table_header),
            Paragraph("Visual Setup & Animation", table_header),
            Paragraph("Mathematical Content & Derivations", table_header),
        ],
        [
            Paragraph("0", table_text),
            Paragraph("<b>Opening Frame</b>", table_text),
            Paragraph("5s", table_text),
            Paragraph("High-contrast title card: 'Functions and Their Graphs', formula f(x) = x² - 4x + 3, student name Amrit Anand (E25B070507), course metadata.", table_text),
            Paragraph("Introduce core quadratic function f(x) = x² - 4x + 3.", table_text),
        ],
        [
            Paragraph("1", table_text),
            Paragraph("<b>Hook / Context</b>", table_text),
            Paragraph("35s", table_text),
            Paragraph("Dual animated axes: smartphone battery % decaying exponentially; projectile ball rising and falling in a parabolic arc. Thesis card at bottom.", table_text),
            Paragraph("Battery model B(t) = 100e^(-0.22t); Projectile model h(t) = -4.9t² + 18t.", table_text),
        ],
        [
            Paragraph("2", table_text),
            Paragraph("<b>Concept Intro</b>", table_text),
            Paragraph("50s", table_text),
            Paragraph("Function Machine box: blue arrow enters ('Input x'), orange arrow exits ('Output f(x)'). Particle x=4 flows in and f(4)=3 emerges. Domain/range cards below.", table_text),
            Paragraph("f(4) = 4² - 4(4) + 3 = 3. Formal definitions: Domain ℝ, Range [-1, ∞).", table_text),
        ],
        [
            Paragraph("3", table_text),
            Paragraph("<b>Visual Intuition</b>", table_text),
            Paragraph("75s", table_text),
            Paragraph("Split screen: evaluation table on left, calibrated 2D axes on right. Step-by-step reveal for x ∈ {-1..5}. Continuous parabola traced; vertical line test sweeps domain.", table_text),
            Paragraph("Graph as {(x, f(x))}. Exact values (-1,8) to (5,8). Vertical line x = x₀ intersects y = f(x) once.", table_text),
        ],
        [
            Paragraph("4", table_text),
            Paragraph("<b>Worked Example</b>", table_text),
            Paragraph("75s", table_text),
            Paragraph("Algebraic derivations on left, graph landmarks flashing on right: (1) y-intercept (0,3); (2) factored zeros (1,0) & (3,0); (3) symmetry axis x=2 & vertex (2,-1).", table_text),
            Paragraph("f(0)=3; (x-1)(x-3)=0 ⇒ x₁=1, x₂=3; x_v = (1+3)/2 = 2, f(2) = -1.", table_text),
        ],
        [
            Paragraph("5", table_text),
            Paragraph("<b>Interpretation</b>", table_text),
            Paragraph("40s", table_text),
            Paragraph("Blue line shades x-axis (-∞, ∞) for domain; orange line shades y-axis [-1, ∞) for range. Curve splits at x=2: decreasing left branch, increasing right branch.", table_text),
            Paragraph("Domain: (-∞, ∞); Range: [-1, ∞); f'(x) = 2x - 4 < 0 on (-∞, 2), > 0 on (2, ∞).", table_text),
        ],
        [
            Paragraph("6", table_text),
            Paragraph("<b>Summary & Credits</b>", table_text),
            Paragraph("30s", table_text),
            Paragraph("Three takeaway cards appear sequentially, followed by academic references (Stewart, Strang, Thomas), music credit, and AI disclosure statement.", table_text),
            Paragraph("Synthesis of input-output rule, graphical representation, and algebraic landmarks.", table_text),
        ],
    ]

    t_scenes = Table(scene_data, colWidths=[20, 75, 45, 205, 185])
    t_scenes.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0F172A")),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#FFFFFF"), colors.HexColor("#F8FAFC")]),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    story.append(t_scenes)

    doc.build(story)
    print(f"Successfully generated {output_pdf_path}")


if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent.parent
    pdf_path = base_dir / "Storyboard.pdf"
    generate_storyboard_pdf(pdf_path)
