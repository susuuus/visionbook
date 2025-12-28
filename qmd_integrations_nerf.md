# Integration Snippets for nerf.qmd

Replace the original ![...](figures/...) with these iframe embeds:

### fig-nerfs-plenoptic_function

```markdown
::{#fig-nerfs-plenoptic_function}
<iframe
  src="interactive_nerf/fig-nerfs-plenoptic_function.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Plenoptic function @Adelson91. The figure shows a slice of the plenoptic function at four locations. Two of the locations are in free space, and two other locations are inside a pinhole camera.
:::
```

### fig-nerfs-flatland_cameras_and_images

```markdown
::{#fig-nerfs-flatland_cameras_and_images}
<iframe
  src="interactive_nerf/fig-nerfs-flatland_cameras_and_images.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

The scene we are modeling. The circle of black triangles on the left are the cameras. The 1D images they see are shown on the right. These images are denoted as $\{\boldsymbol\ell^{(i)}\}_{i=1}^N$.
:::
```

### fig-nerfs-flatland_implicit_to_explicit

```markdown
::{#fig-nerfs-flatland_implicit_to_explicit}
<iframe
  src="interactive_nerf/fig-nerfs-flatland_implicit_to_explicit.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

How a radiance field maps coordinates to colors/densities. (left) Input $(X,Y)$ coordinates, visualized with $X$-values in the green channel and $Y$-values in the blue channel. (right) Radiance field components $L^c$ (colors) and $L^\sigma$ (densities) rendered at each of these coordinates.
:::
```

### fig-nerfs-nerf_module

```markdown
::{#fig-nerfs-nerf_module}
<iframe
  src="interactive_nerf/fig-nerfs-nerf_module.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Module for a parameterized radiance field. We use $\mathbf{R}$ to denote the vector of coordinates $L_\theta$ takes as input.
:::
```

### fig-nerfs-image_to_image_arch

```markdown
::{#fig-nerfs-image_to_image_arch}
<iframe
  src="interactive_nerf/fig-nerfs-image_to_image_arch.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

NeRF architecture for computing the values at each position in an entire radiance field, sampled on a grid. The $\texttt{pos\_enc}$ refers to positional encoding. You can consider this architecture be a CNN with 1x1 filters, or as an MLP applied to each input coordinate vector.
:::
```

### fig-nerfs-flatland_positional_encoding

```markdown
::{#fig-nerfs-flatland_positional_encoding}
<iframe
  src="interactive_nerf/fig-nerfs-flatland_positional_encoding.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

The first layer of NeRF applies positional encoding to the input coordinate values. Here we show the resulting positional codes for all possible input coordinate values $(X,Y)$ within some range.
:::
```

### fig-nerfs-flatland_volume_rendering

```markdown
::{#fig-nerfs-flatland_volume_rendering}
<iframe
  src="interactive_nerf/fig-nerfs-flatland_volume_rendering.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Volume rendering of our Flatland radiance field.
:::
```

### fig-nerfs-pixel2ray

```markdown
::{#fig-nerfs-pixel2ray}
<iframe
  src="interactive_nerf/fig-nerfs-pixel2ray.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Module for mapping from pixel coordinates to the world coordinates of a ray through that pixel.
:::
```

### fig-nerfs-ray2coords

```markdown
::{#fig-nerfs-ray2coords}
<iframe
  src="interactive_nerf/fig-nerfs-ray2coords.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Module for sampling coordinates along a ray.
:::
```

### fig-nerfs-vrender

```markdown
::{#fig-nerfs-vrender}
<iframe
  src="interactive_nerf/fig-nerfs-vrender.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Module for volume rendering of a single ray.
:::
```

### fig-nerfs-full_nerf_pipeline

```markdown
::{#fig-nerfs-full_nerf_pipeline}
<iframe
  src="interactive_nerf/fig-nerfs-full_nerf_pipeline.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Full NeRF pipeline for rendering an image.
:::
```

### nerf_learning.png

```markdown
::{#None}
<iframe
  src="interactive_nerf/fig_nerf_learning.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fig-nerfs-flatland_training

```markdown
::{#fig-nerfs-flatland_training}
<iframe
  src="interactive_nerf/fig-nerfs-flatland_training.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Iterations of fitting a radiance field to Flatland. All of these are top-down views of the world (we are looking at Flatland from above, which is a view the inhabitants cannot see). (a) The radiance field visualized as an image with color equal to the color of the field at each position and transparency proportional to the density of the field at each position. (b and c) The volume rendering process for two different cameras looking at the radiance field. The circle colors and transparencies again show the color and density of the field, and the circle size shows the $\alpha$ value as we walk along each camera ray. Small circles mean those points are more occluded; i.e. there is a low probability of the ray reaching them and they contribute very little to the volume rendering integral.
:::
```

