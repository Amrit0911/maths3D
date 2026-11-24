# Formal AI Tools Disclosure Statement

**Course:** Linear Algebra and Calculus (M3)  
**Assessment:** Internal Assessment - Project Option 1: Animation Video  
**Project Title:** Single-Variable Functions and Graphs: $f(x) = x^2 - 4x + 3$  
**Student Name:** Amrit Anand  
**Student ID:** E25B070507  

In compliance with the M3 Assessment Policy on Originality and AI tool disclosure:

### 1. Tools Utilized
- **Claude / Google Antigravity:** Utilized as an interactive programming and mathematical scripting assistant to structure Manim Community Edition code, choreograph 2D coordinate animations, and organize timing blocks.

### 2. Scope of Assistance
- **Animation Scripting & Architecture:** Generated modular scene class templates (`Scene1Hook` through `Scene6Summary`), helper constructors (`make_standard_axes`, `create_point_marker`), and standardized color palette definitions in `config.py`.
- **Timing & Audio Sync Layout:** Outlined storyboard duration targets and calculated scene `wait()` intervals to align with a 5-minute pacing schedule.
- **FFmpeg & Bash Automation:** Assisted in creating `render.sh` and `merge_audio.sh` shell scripts.

### 3. Independent Verification & Mathematical Authenticity
- All mathematical definitions, factoring steps ($(x-1)(x-3)$), vertex calculations via symmetry ($x=2, f(2)=-1$), and calculus intervals (decreasing on $(-\infty, 2)$, increasing on $(2, \infty)$) were independently verified on paper and hardcoded via a dynamic function generator `f(x)` in `helpers.py`.
- The author retains full conceptual mastery over all code and derivations and is prepared to independently explain any animation step, derivation, or design decision during the individual Viva / Q&A session.
