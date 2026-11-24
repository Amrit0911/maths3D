#!/usr/bin/env bash
# ==============================================================================
# render.sh
# ---------
# Script to render MainVideo at 1080p 30fps (16:9 widescreen) using Manim CE,
# and copy the final MP4 to the repository root as _Video.mp4.
# ==============================================================================

set -e # Exit immediately on error

echo "================================================================"
echo "Starting Manim 1080p 30fps Render: MainVideo"
echo "================================================================"

# Resolve directories
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$SCRIPT_DIR"

# Flags:
# -qh: 1080p high quality (1920x1080)
# --fps 30: 30 frames per second
# --renderer cairo: default solid renderer
echo "Rendering main_video.py..."
manim -qh --fps 30 main_video.py MainVideo

# Locate output file
RENDERED_FILE="$SCRIPT_DIR/media/videos/main_video/1080p30/MainVideo.mp4"

if [ -f "$RENDERED_FILE" ]; then
    echo "Render successful!"
    echo "Copying to repository root: $REPO_ROOT/_Video.mp4"
    cp "$RENDERED_FILE" "$REPO_ROOT/_Video.mp4"
    echo "Done! Final video ready at: $REPO_ROOT/_Video.mp4"
else
    echo "Error: Expected output file $RENDERED_FILE not found."
    exit 1
fi
