"""Critic node: compare a rendered video against a reference.

This is a pragmatic critic for the current workflow:

detector.json -> plan.json -> manim script -> rendered mp4

The critic compares a candidate MP4 against a reference MP4 by sampling frames,
computing edge-overlap scores, and writing a small report with recommendations.

It does NOT auto-edit code. Instead it produces parameter-oriented suggestions
that you can wire into a driver loop (safe) or apply manually.


Edit:: the critic should take look at the primi
"""

from __future__ import annotations

import argparse
import base64
import importlib.util
import json
import mimetypes
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import cv2
import numpy as np


@dataclass
class CriticConfig:
    sample_times: Tuple[float, ...] = (0.1, 0.5, 0.9)
    resize_long_side: int = 900
    canny_low: int = 50
    canny_high: int = 150
    edge_dilate: int = 1
    missing_line_threshold: int = 60
    missing_line_min_length: int = 80
    missing_line_max_gap: int = 12


def _read_frame_at_fraction(video_path: str, fraction: float) -> Optional[np.ndarray]:
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        return None

    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT) or 0)
    if total <= 0:
        # Try time-based seek as fallback
        fps = float(cap.get(cv2.CAP_PROP_FPS) or 0.0)
        duration = float(cap.get(cv2.CAP_PROP_POS_MSEC) or 0.0)
        _ = fps, duration
        cap.release()
        return None

    idx = int(np.clip(round(fraction * (total - 1)), 0, total - 1))
    cap.set(cv2.CAP_PROP_POS_FRAMES, float(idx))
    ok, frame = cap.read()
    cap.release()
    return frame if ok else None


def _resize_to_long_side(bgr: np.ndarray, long_side: int) -> np.ndarray:
    h, w = bgr.shape[:2]
    if max(h, w) <= long_side:
        """Critic node (placeholder).

        Original implementation removed. Restore desired implementation as needed.
        """

        # Placeholder to keep module importable; replace with real code.
        __all__ = []


        def placeholder():
            """No-op placeholder for critic node."""
            return None
        ker = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (k, k))
