# Linear Algebra and Calculus (M3) - Animation Video Project
## Topic: Single-variable Functions and Graphs ($f(x) = x^2 - 4x + 3$)
**Student Name:** Amrit Anand  
**Student ID:** `E25B070507`  

This repository contains the complete animation source code, video rendering pipeline, mathematical verification tests, storyboard PDF, and supporting documentation for Option 1 of the M3 Internal Assessment (10% weightage).

> **PUBLIC REPOSITORY REMINDER:**  
> This repository must remain **PUBLIC** for submission and grading verification.

---

## 1. Project Overview & Learning Objectives
- **Target Video Duration:** ~5 minutes (310 seconds total runtime, strictly under the 7-minute limit).
- **Format:** 1080p Full HD (1920x1080), 30 fps, 16:9 widescreen landscape.
- **Learning Objective:**
  > *"By the end of this video, the viewer will be able to explain that a single-variable function assigns exactly one output to each input, understand that the graph is the set of points $(x, f(x))$, and systematically read roots, y-intercept, vertex, domain, range, and increasing/decreasing intervals directly from the graph."*

---

## 2. Mathematical Rigor & Architecture
All mathematics is anchored to a single source of truth defined in `_Code/helpers.py`:
$$f(x) = x^2 - 4x + 3$$
No computed numbers are hardcoded. All coordinates, table evaluations, and vertex positions are computed programmatically:
- **Y-Intercept:** $f(0) = 3 \implies (0, 3)$
- **Roots / Zeros:** $f(x) = 0 \iff (x - 1)(x - 3) = 0 \implies x \in \{1, 3\}$
- **Vertex / Extrema:** By symmetry $x_v = \frac{1+3}{2} = 2$; $f(2) = -1 \implies (2, -1)$
- **Table of Values:** $x \in \{-1, 0, 1, 2, 3, 4, 5\} \implies f(x) \in \{8, 3, 0, -1, 0, 3, 8\}$
- **Domain:** $\mathbb{R} = (-\infty, \infty)$
- **Range:** $[-1, \infty)$
- **Monotonicity:** Strictly decreasing on $(-\infty, 2)$, strictly increasing on $(2, \infty)$

---

## 3. Directory Structure
```
M3_AnimationVideo_Functions_E25B070507/
├── _Video.mp4                 # Final rendered 1080p MP4 video
├── _Code/
│   ├── config.py                  # Visual themes, colors (blue=in, orange=out, green=graph), fonts
│   ├── helpers.py                 # Single source of truth f(x), axes constructor, marker helpers
│   ├── scene1_hook.py             # Scene 1: Real-world hook & motivation (35s)
│   ├── scene2_concept.py          # Scene 2: Function machine & formal definitions (50s)
│   ├── scene3_intuition.py        # Scene 3: Step-by-step point plotting & vertical line test (75s)
│   ├── scene4_worked_example.py   # Scene 4: Intercept, factoring roots, vertex derivation (75s)
│   ├── scene5_interpretation.py   # Scene 5: Domain, range, increasing/decreasing intervals (40s)
│   ├── scene6_summary.py          # Scene 6: Three takeaways, credits, AI disclosure (30s)
│   ├── main_video.py              # Master orchestrator with Opening (5s) and Closing scenes
│   ├── tests/test_math.py         # Automated SymPy unit tests for all mathematical claims
│   ├── generate_storyboard_pdf.py # Generates Storyboard.pdf via ReportLab
│   ├── render.sh                  # 1080p 30fps bash render script
│   ├── merge_audio.sh             # FFmpeg voice narration and music muxing script
│   └── requirements.txt           # Python dependencies
├── docs/
│   └── CODE_WALKTHROUGH.md        # Plain-English viva defense guide
├── Storyboard.md                  # 6-scene structured academic storyboard
├── Storyboard.pdf                 # Formatted PDF storyboard & mathematical specification
├── AI_DISCLOSURE.md               # Formal declaration of AI tools used (as required)
├── CREDITS.md                     # Textbook and music citations
└── README.md                      # Project documentation & run guide
```

---

## 4. Setup & Rendering Instructions (macOS / Linux)

### Step 1: Install System Prerequisites
On macOS via Homebrew:
```bash
brew install python ffmpeg
# LaTeX is recommended for MathTex rendering:
brew install --cask mactex-no-gui
# Or basictex: brew install --cask basictex
```

On Ubuntu / Debian:
```bash
sudo apt-get update
sudo apt-get install -y python3 python3-pip ffmpeg libcairo2-dev libpango1.0-dev texlive-latex-base texlive-latex-extra
```

### Step 2: Install Python Dependencies
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r _Code/requirements.txt
```

### Step 3: Fast Preview of a Single Scene (Low Quality -ql)
To rapidly test animations without waiting for 1080p:
```bash
cd _Code
manim -ql scene1_hook.py Scene1Hook
# Or scene 3:
manim -ql scene3_intuition.py Scene3Intuition
```

### Step 4: Full 1080p Render
Run the automated render script:
```bash
cd _Code
bash render.sh
```
This renders `MainVideo` at high quality (`-qh --fps 30`), produces a 1920x1080 MP4, and automatically copies it to the repository root as `_Video.mp4`.

### Step 5: (Optional) Voice-over & Music Muxing
To attach voice narration and background audio:
1. Save your voice recording at `_Audio/narration.wav`.
2. (Optional) Save royalty-free background music at `_Audio/music.mp3`.
3. Run:
   ```bash
   bash _Code/merge_audio.sh
   ```


---

## 5. Mathematical Summary Table (Viva Reference)

| $x$ | Hand Substitution: $f(x) = x^2 - 4x + 3$ | $f(x)$ | Geometric Feature |
| :---: | :--- | :---: | :--- |
| **$-1$** | $(-1)^2 - 4(-1) + 3 = 1 + 4 + 3$ | **$8$** | Left boundary point |
| **$0$** | $0^2 - 4(0) + 3 = 3$ | **$3$** | **$y$-intercept** $(0, 3)$ |
| **$1$** | $1^2 - 4(1) + 3 = 1 - 4 + 3$ | **$0$** | **Root / $x$-intercept** $(1, 0)$ |
| **$2$** | $2^2 - 4(2) + 3 = 4 - 8 + 3$ | **$-1$** | **Vertex / Global Minimum** $(2, -1)$ |
| **$3$** | $3^2 - 4(3) + 3 = 9 - 12 + 3$ | **$0$** | **Root / $x$-intercept** $(3, 0)$ |
| **$4$** | $4^2 - 4(4) + 3 = 16 - 16 + 3$ | **$3$** | Symmetric pair to $(0, 3)$ |
| **$5$** | $5^2 - 4(5) + 3 = 25 - 20 + 3$ | **$8$** | Right boundary point |

---

## 6. Verification & Academic Integrity
- Run `pytest _Code/tests/test_math.py` to verify all mathematical assertions with SymPy.
- Refer to [docs/CODE_WALKTHROUGH.md](docs/CODE_WALKTHROUGH.md) for the Viva Defense Walkthrough.
- Refer to [AI_DISCLOSURE.md](AI_DISCLOSURE.md) for the complete disclosure of AI tools used.
