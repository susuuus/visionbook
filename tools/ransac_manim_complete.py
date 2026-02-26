from manim import *
import json
import numpy as np

class RANSACVisualization(Scene):
    def construct(self):
        # Set white background
        self.camera.background_color = WHITE
        
        # Load circle positions
        with open('tools/ransac_master_positions_ordered.json', 'r') as f:
            data = json.load(f)
        
        # Circle positions from data (axes-relative coordinates)
        # Convert to Manim coordinates (need to scale and flip Y)
        # Original image subplot size: 1622 x 1312 pixels
        # Manim default camera: 14.22 x 8 units
        
        # Scale factor to fit in Manim
        scale_x = 10.0 / 1400  # Keep some margin
        scale_y = 6.0 / 1000
        
        # Convert positions
        circle_positions = []
        for circle in data['master_positions']:
            x = circle['x_from_y_axis']
            y = circle['y_from_x_axis']
            # Convert to Manim coordinates (center origin, flip Y)
            manim_x = x * scale_x - 5.0  # Center horizontally
            manim_y = y * scale_y - 3.0  # Center vertically
            circle_positions.append((manim_x, manim_y))
        
        # Define colors for each subplot
        subplot_colors = {
            'a': {'red': [], 'cyan': []},
            'b': {'red': [4, 9], 'cyan': [5]},  # 0-indexed: #5→4, #10→9, #6→5
            'c': {'red': [5, 10], 'cyan': [4, 6]},  # #6→5, #11→10, #5→4, #7→6
            'd': {'red': [0, 5], 'cyan': [1, 2, 3, 4, 6, 7, 8]},  # #1→0, #6→5, etc
            'e': {'red': [0, 7], 'cyan': [1, 2, 3, 4, 5, 8]},  # #1→0, #8→7, etc
            'f': {'red': [], 'cyan': [0, 1, 2, 3, 4, 5, 6, 7, 8]}  # All cyan #1-#9
        }
        
        # Line connections - based on line analysis (0-indexed)
        line_connections = {
            'a': None,  # No filled circles
            'b': {'start': 4, 'end': 9},  # #5(idx=4) ↔ #10(idx=9)
            'c': {'start': 5, 'end': 10},  # #6(idx=5) ↔ #11(idx=10)
            'd': {'start': 0, 'end': 5},  # #1(idx=0) ↔ #6(idx=5)
            'e': {'start': 0, 'end': 7},  # #1(idx=0) ↔ #8(idx=7)
            'f': {'start': 0, 'end': 8}  # #1(idx=0) ↔ #9(idx=8) - spans all 9 inliers
        }
        
        # Inlier counts
        inlier_counts = {
            'a': 0,
            'b': 3,
            'c': 4,
            'd': 9,
            'e': 8,
            'f': 9
        }
        
        # Create X and Y axes separately as simple lines with arrows
        x_axis = Arrow(
            start=[-5, -3, 0],
            end=[5, -3, 0],
            color=BLACK,
            stroke_width=5,
            buff=0,
            tip_length=0.3,
            max_tip_length_to_length_ratio=0.15
        )
        y_axis = Arrow(
            start=[-5, -3, 0],
            end=[-5, 3, 0],
            color=BLACK,
            stroke_width=5,
            buff=0,
            tip_length=0.3,
            max_tip_length_to_length_ratio=0.15
        )
        
        # Animate each subplot
        subplots = ['a', 'b', 'c', 'd', 'e', 'f']
        
        for subplot_idx, subplot_label in enumerate(subplots):
            if subplot_idx == 0:
                # First subplot: show axes and all empty circles
                self.play(Create(x_axis), Create(y_axis), run_time=1.5)
                
                # Create all circles (empty)
                circles = []
                for i, (x, y) in enumerate(circle_positions):
                    circle = Circle(
                        radius=0.15,
                        color=BLACK,
                        stroke_width=3,  # Thicker circle outlines
                        fill_opacity=0
                    ).move_to([x, y, 0])
                    circles.append(circle)
                
                # Show all circles at once
                self.play(*[Create(c) for c in circles], run_time=1.0)
                
                # Add subplot label at bottom center (150px from bottom = ~0.9 units from bottom)
                label = Text(f"({subplot_label})", color=BLACK, font_size=28).move_to([0, -3.8, 0])
                self.play(FadeIn(label), run_time=0.5)
                
                self.wait(1.5)
                self.play(FadeOut(label), run_time=0.3)
                
            else:
                # Subsequent subplots: transition by coloring circles and adding lines
                
                # Get colors for this subplot
                red_indices = subplot_colors[subplot_label]['red']
                cyan_indices = subplot_colors[subplot_label]['cyan']
                
                # Reset all circles to empty
                animations = []
                for i, circle in enumerate(circles):
                    if i in red_indices:
                        animations.append(circle.animate.set_fill(RED, opacity=1))
                    elif i in cyan_indices:
                        animations.append(circle.animate.set_fill(BLUE, opacity=1))
                    else:
                        animations.append(circle.animate.set_fill(WHITE, opacity=1))
                
                # Color circles
                self.play(*animations, run_time=0.8)
                
                # Add fitted line if present - connect the actual red circles
                line = None
                if subplot_label in line_connections and line_connections[subplot_label] is not None:
                    line_info = line_connections[subplot_label]
                    start_idx = line_info['start']
                    end_idx = line_info['end']
                    
                    # Get the actual circle positions
                    start_pos = circle_positions[start_idx]
                    end_pos = circle_positions[end_idx]
                    
                    # Calculate direction vector
                    dx = end_pos[0] - start_pos[0]
                    dy = end_pos[1] - start_pos[1]
                    length = np.sqrt(dx**2 + dy**2)
                    
                    # Extend the line beyond the circles by 20% on each side
                    extension = 0.2
                    extended_start_x = start_pos[0] - extension * dx
                    extended_start_y = start_pos[1] - extension * dy
                    extended_end_x = end_pos[0] + extension * dx
                    extended_end_y = end_pos[1] + extension * dy
                    
                    line = Line(
                        start=[extended_start_x, extended_start_y, 0],
                        end=[extended_end_x, extended_end_y, 0],
                        color=RED,
                        stroke_width=6  # Much thicker red lines
                    )
                    self.play(Create(line), run_time=0.6)
                
                # Add subplot label at bottom center (150px from bottom)
                label = Text(f"({subplot_label})", color=BLACK, font_size=28).move_to([0, -3.8, 0])
                
                # Add inlier count label at top center (270px from top)
                inlier_label = None
                if inlier_counts[subplot_label] > 0:
                    inlier_label = Text(
                        f"{inlier_counts[subplot_label]} inliers",
                        color=BLACK,
                        font_size=24
                    ).move_to([0, 2.5, 0])
                    self.play(FadeIn(label), FadeIn(inlier_label), run_time=0.5)
                else:
                    self.play(FadeIn(label), run_time=0.5)
                
                self.wait(1.5)
                
                # Clean up for next subplot
                if line is not None:
                    self.play(FadeOut(line), run_time=0.3)
                if inlier_label is not None:
                    self.play(FadeOut(label), FadeOut(inlier_label), run_time=0.3)
                else:
                    self.play(FadeOut(label), run_time=0.3)
        
        # Final wait
        self.wait(2)


if __name__ == "__main__":
    # Render command:
    # manim -pql tools/ransac_manim_complete.py RANSACVisualization
    pass
