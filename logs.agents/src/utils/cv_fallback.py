# cv_fallback.py
# OpenCV-based geometry extractor — used as verification layer only.
# Primary detector is src/nodes/detector.py (VLM-based).
# Call detect_geometry(image_path) to get raw primitives dict.

import cv2
import numpy as np
from collections import defaultdict

def detect_geometry(image_path):
    # Load image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Could not load image: {image_path}")

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect edges using Canny
    edges = cv2.Canny(gray, 50, 150)

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter contours by area
    min_area = 100
    contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_area]

    # Filter contours by shape (approximate circle)
    contours = [cnt for cnt in contours if cv2.isContourConvex(cnt)]

    # Extract primitives
    primitives = []
    for cnt in contours:
        # Approximate the contour
        approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
        # Add to primitives
        primitives.append({
            'type': 'polygon',
            'points': [(x, y) for x, y in cnt],
            'approx': approx
        })

    return primitives