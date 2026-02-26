import cv2
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Load the RANSAC figure
img_path = "figures_sorted/homography/diagrams_2d/ransac_algo.png"
img = cv2.imread(img_path)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

print("Image shape:", img.shape)
print("\nAnalyzing RANSAC figure with 6 subplots (a-f)...")

# The image appears to be arranged in 2 rows x 3 columns
# Let me split it into the 6 subplots
height, width = img.shape[:2]
subplot_height = height // 2
subplot_width = width // 3

subplots = []
labels = ['(a)', '(b)', '(c)', '(d)', '(e)', '(f)']

for row in range(2):
    for col in range(3):
        y_start = row * subplot_height
        y_end = (row + 1) * subplot_height
        x_start = col * subplot_width
        x_end = (col + 1) * subplot_width
        
        subplot = img_rgb[y_start:y_end, x_start:x_end]
        subplots.append(subplot)
        
print(f"\nExtracted {len(subplots)} subplots, each approximately {subplot_height}x{subplot_width} pixels")

# Now let's detect circles in subplot (a) which should have all 11 empty circles
print("\n" + "="*60)
print("SUBPLOT (a) - Initial data points")
print("="*60)

subplot_a = subplots[0]
gray_a = cv2.cvtColor(subplot_a, cv2.COLOR_RGB2GRAY)

# Detect circles using HoughCircles
circles = cv2.HoughCircles(
    gray_a,
    cv2.HOUGH_GRADIENT,
    dp=1,
    minDist=20,
    param1=50,
    param2=30,
    minRadius=5,
    maxRadius=15
)

if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    print(f"Found {len(circles)} circles in subplot (a)")
    
    # Sort by y-coordinate (top to bottom) then x-coordinate
    circles_sorted = sorted(circles, key=lambda c: (c[1], c[0]))
    
    print("\nCircle positions (x, y, radius):")
    for i, (x, y, r) in enumerate(circles_sorted):
        print(f"  Circle {i+1}: x={x:3d}, y={y:3d}, r={r}")
        
    # Find axes origin (should be bottom-left)
    # Look for edges
    edges = cv2.Canny(gray_a, 50, 150)
    
    # Find the axes lines
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=50, minLineLength=50, maxLineGap=10)
    
    if lines is not None:
        print(f"\nFound {len(lines)} lines (axes)")
        # Find vertical and horizontal lines near the edges
        vertical_lines = []
        horizontal_lines = []
        
        for line in lines:
            x1, y1, x2, y2 = line[0]
            angle = np.abs(np.arctan2(y2 - y1, x2 - x1) * 180 / np.pi)
            
            if angle < 10 or angle > 170:  # Horizontal
                horizontal_lines.append((x1, y1, x2, y2))
            elif 80 < angle < 100:  # Vertical
                vertical_lines.append((x1, y1, x2, y2))
        
        print(f"  Horizontal lines: {len(horizontal_lines)}")
        print(f"  Vertical lines: {len(vertical_lines)}")

# Save visualization
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
for idx, (ax, label) in enumerate(zip(axes.flat, labels)):
    ax.imshow(subplots[idx])
    ax.set_title(label, fontsize=16, fontweight='bold')
    ax.axis('off')

plt.tight_layout()
plt.savefig('figures/ransac_analysis.png', dpi=150, bbox_inches='tight')
print("\nVisualization saved to figures/ransac_analysis.png")

# Analyze each subplot for filled circles and lines
print("\n" + "="*60)
print("ANALYZING ALL SUBPLOTS")
print("="*60)

for idx, (subplot, label) in enumerate(zip(subplots, labels)):
    print(f"\n{label}:")
    
    # Detect red color (filled inliers)
    hsv = cv2.cvtColor(subplot, cv2.COLOR_RGB2HSV)
    
    # Red mask
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 100, 100])
    upper_red2 = np.array([180, 255, 255])
    red_mask = cv2.inRange(hsv, lower_red1, upper_red1) | cv2.inRange(hsv, lower_red2, upper_red2)
    red_pixels = np.sum(red_mask > 0)
    
    # Cyan/Blue mask
    lower_cyan = np.array([85, 50, 50])
    upper_cyan = np.array([105, 255, 255])
    cyan_mask = cv2.inRange(hsv, lower_cyan, upper_cyan)
    cyan_pixels = np.sum(cyan_mask > 0)
    
    print(f"  Red pixels: {red_pixels}")
    print(f"  Cyan/Blue pixels: {cyan_pixels}")
    
    # Find circles
    gray = cv2.cvtColor(subplot, cv2.COLOR_RGB2GRAY)
    circles = cv2.HoughCircles(
        gray,
        cv2.HOUGH_GRADIENT,
        dp=1,
        minDist=15,
        param1=50,
        param2=25,
        minRadius=5,
        maxRadius=15
    )
    
    if circles is not None:
        print(f"  Detected circles: {len(circles[0])}")

print("\n" + "="*60)
print("Analysis complete!")
