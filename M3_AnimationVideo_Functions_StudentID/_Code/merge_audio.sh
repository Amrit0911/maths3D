#!/usr/bin/env bash
# ==============================================================================
# merge_audio.sh
# --------------
# Muxes clear voice-over narration (narration.wav) and optional subtle background
# music (music.mp3 at 12% volume) onto _Video.mp4 using ffmpeg.
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

VIDEO_INPUT="$REPO_ROOT/_Video.mp4"
NARRATION_INPUT="$REPO_ROOT/_Audio/narration.wav"
MUSIC_INPUT="$REPO_ROOT/_Audio/music.mp3"
FINAL_OUTPUT="$REPO_ROOT/_Video_With_Audio.mp4"

if [ ! -f "$VIDEO_INPUT" ]; then
    echo "Error: Video input $VIDEO_INPUT not found. Run render.sh first."
    exit 1
fi

if [ ! -f "$NARRATION_INPUT" ]; then
    echo "Notice: Narration file $NARRATION_INPUT not found."
    echo "To record voice-over, save your recording as $NARRATION_INPUT and re-run this script."
    exit 1
fi

echo "Muxing audio onto video..."

if [ -f "$MUSIC_INPUT" ]; then
    echo "Detected background music. Mixing voice-over (100%) and music (12%)..."
    ffmpeg -y -i "$VIDEO_INPUT" -i "$NARRATION_INPUT" -i "$MUSIC_INPUT" \
        -filter_complex "[1:a]volume=1.0[v1];[2:a]volume=0.12[m1];[v1][m1]amix=inputs=2:duration=first[aout]" \
        -map 0:v -map "[aout]" \
        -c:v copy -c:a aac -b:a 192k \
        "$FINAL_OUTPUT"
else
    echo "No background music found. Muxing narration track directly..."
    ffmpeg -y -i "$VIDEO_INPUT" -i "$NARRATION_INPUT" \
        -map 0:v -map 1:a \
        -c:v copy -c:a aac -b:a 192k \
        "$FINAL_OUTPUT"
fi

echo "Audio merge completed successfully!"
echo "Final video with audio saved to: $FINAL_OUTPUT"
# Replace main video with voiced version
mv "$FINAL_OUTPUT" "$VIDEO_INPUT"
echo "Updated $VIDEO_INPUT with audio."
