import numpy as np
import plotly.graph_objects as go
import os

# Define coordinate axes
axes = [
    go.Scatter3d(x=[0, 2], y=[0, 0], z=[0, 0], mode='lines', name='X_C', line=dict(color='black', width=5)),
    go.Scatter3d(x=[0, 0], y=[0, 2], z=[0, 0], mode='lines', name='Y_C', line=dict(color='black', width=5)),
    go.Scatter3d(x=[0, 0], y=[0, 0], z=[0, 2], mode='lines', name='Z_C', line=dict(color='black', width=5))
]

# Camera center
camera_center = go.Scatter3d(x=[0], y=[0], z=[0], mode='markers', marker=dict(size=8, color='black'), name='Camera Center')

# Virtual image plane at Z = f
f = 1
x_plane = np.linspace(-1, 1, 10)
y_plane = np.linspace(-1, 1, 10)
X_plane, Y_plane = np.meshgrid(x_plane, y_plane)
Z_plane = np.full_like(X_plane, f)

image_plane = go.Surface(x=X_plane, y=Y_plane, z=Z_plane, opacity=0.3, colorscale='gray', name="Virtual Image Plane")

# 3D point P and projection ray
P = np.array([1, 0.5, 2])  # Arbitrary 3D point
p_img = (f / P[2]) * P  # Projection on the image plane

ray = go.Scatter3d(x=[0, P[0]], y=[0, P[1]], z=[0, P[2]], mode='lines', line=dict(color='red', width=3), name='Ray')
point_P = go.Scatter3d(x=[P[0]], y=[P[1]], z=[P[2]], mode='markers', marker=dict(size=6, color='blue'), name='Point P')
point_p = go.Scatter3d(x=[p_img[0]], y=[p_img[1]], z=[p_img[2]], mode='markers', marker=dict(size=6, color='blue'), name='Projected p')

# Combine all elements
fig = go.Figure(data=[*axes, camera_center, image_plane, ray, point_P, point_p])
fig.update_layout(
    scene=dict(
        xaxis_title="X_C", yaxis_title="Y_C", zaxis_title="Z_C",
        aspectmode="cube"
    ),
    title="Pinhole Camera Model"
)

# Get the script's file name without the extension
script_name = os.path.splitext(os.path.basename(__file__))[0]

# Save the figure as HTML
fig.write_html(f"{script_name}.html")

fig.show()