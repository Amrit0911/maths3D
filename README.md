# Maths3D: Single-Variable Functions & Graphs
**M3 Animation Video Assessment — Linear Algebra & Calculus**  
**Student Name:** Amrit Anand  
**Student ID:** `E25B070507`  
**Core Function:** $f(x) = x^2 - 4x + 3$  

---

## 🎬 How to Access & Watch the Video

1. **Watch Directly on GitHub:**  
   Navigate to [`M3_AnimationVideo_Functions_E25B070507/_Video.mp4`](M3_AnimationVideo_Functions_E25B070507/_Video.mp4) and click to stream directly in your browser.
2. **Download Raw Video:**  
   Click the **Download** button on the `_Video.mp4` page to save the full 1080p (1920×1080 @ 30 fps) MP4 file locally.
3. **Open Locally (macOS / VLC):**  
   From the command line in this repository:
   ```bash
   open M3_AnimationVideo_Functions_E25B070507/_Video.mp4
   ```
   or with VLC:
   ```bash
   vlc M3_AnimationVideo_Functions_E25B070507/_Video.mp4
   ```

---

## 📄 Storyboard & Assessment Documentation

- **Storyboard (PDF):** [`M3_AnimationVideo_Functions_E25B070507/Storyboard.pdf`](M3_AnimationVideo_Functions_E25B070507/Storyboard.pdf)
- **Storyboard (Markdown):** [`M3_AnimationVideo_Functions_E25B070507/Storyboard.md`](M3_AnimationVideo_Functions_E25B070507/Storyboard.md)
- **Viva Defense Walkthrough:** [`M3_AnimationVideo_Functions_E25B070507/docs/CODE_WALKTHROUGH.md`](M3_AnimationVideo_Functions_E25B070507/docs/CODE_WALKTHROUGH.md)
- **Academic AI Disclosure:** [`M3_AnimationVideo_Functions_E25B070507/AI_DISCLOSURE.md`](M3_AnimationVideo_Functions_E25B070507/AI_DISCLOSURE.md)
- **Academic & Asset Credits:** [`M3_AnimationVideo_Functions_E25B070507/CREDITS.md`](M3_AnimationVideo_Functions_E25B070507/CREDITS.md)
- **Detailed Project Guide:** [`M3_AnimationVideo_Functions_E25B070507/README.md`](M3_AnimationVideo_Functions_E25B070507/README.md)

---

## 🚀 Rebuilding the Video from Source

```bash
cd M3_AnimationVideo_Functions_E25B070507

# 1. Create and activate virtual environment & install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r _Code/requirements.txt

# 2. Run mathematical verification tests
pytest _Code/tests/test_math.py

# 3. Fast 480p preview of a single scene
cd _Code
manim -ql scene1_hook.py Scene1Hook

# 4. Full 1080p production build
bash render.sh
```
