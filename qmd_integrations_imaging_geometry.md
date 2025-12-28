# Integration Snippets for imaging_geometry.qmd

Replace the original ![...](figures/...) with these iframe embeds:

### fig-world_and_camera_coordinates

```markdown
::{#fig-world_and_camera_coordinates}
<iframe
  src="interactive_imaging_geometry/fig-world_and_camera_coordinates.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Camera-centric and world-centric camera coordinate systems.
:::
```

### fig-world_and_camera_coordinates

```markdown
::{#fig-world_and_camera_coordinates}
<iframe
  src="interactive_imaging_geometry/fig-world_and_camera_coordinates.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

The picture taken by the standing character from @fig-world_and_camera_coordinates
:::
```

### fig-pinholeGeometry2bis

```markdown
::{#fig-pinholeGeometry2bis}
<iframe
  src="interactive_imaging_geometry/fig-pinholeGeometry2bis.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Perspective projection. Remember that from similar triangles, we have $x/f = X/Z$ and $y/f = Y/Z$.
:::
```

### fig-pinhole_and_sensor

```markdown
::{#fig-pinhole_and_sensor}
<iframe
  src="interactive_imaging_geometry/fig-pinhole_and_sensor.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

An image is projected into the sensor. World coordinates are transformed into pixels at the sensor. The focal length is $f$, and the physical width of the sensor is $w$. The sensor has $N \times M$ pixels.
:::
```

### fig-conventions

```markdown
::{#fig-conventions}
<iframe
  src="interactive_imaging_geometry/fig-conventions.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

(a) 3D representation of the image plane. 
(b and c) Two different conventions for the image coordinate systems. In this book we have been using (b).
:::
```

### fig-coordinate_systems_ray

```markdown
::{#fig-coordinate_systems_ray}
<iframe
  src="interactive_imaging_geometry/fig-coordinate_systems_ray.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

The 3D point $\mathbf{P}$ is obtained by scaling the point $\mathbf{p}=(x,y,f)$ with a scaling factor $Z/f$. The ray that passes by the point $\mathbf{p}$ is the line defined by $\lambda (x,y,f)$, with $\lambda$ being a positive real number.
:::
```

### simple_calibration_1.jpg

```markdown
::{#None}
<iframe
  src="interactive_imaging_geometry/fig_simple_calibration_1.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### simple_calibration_2.jpg

```markdown
::{#None}
<iframe
  src="interactive_imaging_geometry/fig_simple_calibration_2.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fig-camera_calibration

```markdown
::{#fig-camera_calibration}
<iframe
  src="interactive_imaging_geometry/fig-camera_calibration.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

World- and camera-coordinate systems. A 3D point expressed in world coordinates, $\mathbf{P}_W$, can be expressed in the camera-coordinate frame, $\mathbf{P}_c$, by applying the translation, $\mathbf{T}$, and rotation, $\mathbf{R}$, to the point coordinates.
:::
```

### fig-summary_camera_projection

```markdown
::{#fig-summary_camera_projection}
<iframe
  src="interactive_imaging_geometry/fig-summary_camera_projection.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Projection of a point into the image plane. This summary puts together @fig-pinholeGeometry2bis and @fig-camera_calibration. First, we change the world-coordinates system, in which the point is expressed, into the camera-coordinates system, using the extrinsic camera model, and then we project it into the camera plane using the intrinsic camera model.
:::
```

### fig-camera_calibration_scenarios

```markdown
::{#fig-camera_calibration_scenarios}
<iframe
  src="interactive_imaging_geometry/fig-camera_calibration_scenarios.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Four examples of camera poses respect to the world-coordinates system with increasing complexity. In the text we derive the projection matrix for each scenario.
:::
```

### fig-horizon_heads

```markdown
::{#fig-horizon_heads}
<iframe
  src="interactive_imaging_geometry/fig-horizon_heads.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

If you hold the camera parallel to the ground at the height of your eyes and take a picture of a person standing in front of you with a similar height, their eyes will project near the middle portion of the vertical axis of the picture.
:::
```

### fig-sketch_eyes_location

```markdown
::{#fig-sketch_eyes_location}
<iframe
  src="interactive_imaging_geometry/fig-sketch_eyes_location.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Sketch showing a person taking a picture of two people standing at different distances from the camera. Their eyes will project to the same image row regardless of their distance to the camera.
:::
```

### fig-reprojection_error

```markdown
::{#fig-reprojection_error}
<iframe
  src="interactive_imaging_geometry/fig-reprojection_error.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Reprojection error indicated by the red lines on the image plane.
:::
```

### fig-office_measurements

```markdown
::{#fig-office_measurements}
<iframe
  src="interactive_imaging_geometry/fig-office_measurements.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Office picture and real distances between a sparse set of points measured in centimeters.
:::
```

### fig-office_correspondences_img

```markdown
::{#fig-office_correspondences_img}
<iframe
  src="interactive_imaging_geometry/fig-office_correspondences_img.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Office picture and a table with the 3D world coordinates of 12 points, extracted using the measurements from @fig-office_measurements
:::
```

### fig-result_toymodel_3dscene_and_estimated_camera

```markdown
::{#fig-result_toymodel_3dscene_and_estimated_camera}
<iframe
  src="interactive_imaging_geometry/fig-result_toymodel_3dscene_and_estimated_camera.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Inferred camera location for the office picture. The figure shows three different viewpoints.
:::
```

