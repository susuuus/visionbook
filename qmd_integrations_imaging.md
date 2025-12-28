# Integration Snippets for imaging.qmd

Replace the original ![...](figures/...) with these iframe embeds:

### fig-lightSpray

```markdown
::{#fig-lightSpray}
<iframe
  src="interactive_imaging/fig-lightSpray.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

A light ray from the sun strikes a surface and generates outgoing rays
of intensity and color depending on the angles of the incoming and
outgoing rays relative to the surface orientation.
:::
```

### fig-rendering-a

```markdown
::{#fig-rendering-a}
<iframe
  src="interactive_imaging/fig-rendering-a.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Lambertian
:::
```

### fig-rendering-b

```markdown
::{#fig-rendering-b}
<iframe
  src="interactive_imaging/fig-rendering-b.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Phong
:::
```

### fig-rendering-c

```markdown
::{#fig-rendering-c}
<iframe
  src="interactive_imaging/fig-rendering-c.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Photograph
:::
```

### fig-wallpicture

```markdown
::{#fig-wallpicture}
<iframe
  src="interactive_imaging/fig-wallpicture.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

(a) Why there are no pictures appearing on the walls? (b) The pinhole
camera restricts the light rays reaching the wall, producing an image to
appear.
:::
```

### fig-pinhole3

```markdown
::{#fig-pinhole3}
<iframe
  src="interactive_imaging/fig-pinhole3.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

A simple setting for creating images on a white piece of paper. In
front of the white piece of paper we place another piece of black paper
with a hole in the middle. The black paper projects a shadow on the
white paper and, in the middle of the shadow, appears a picture of the
scene in front of the hole. By making the hole large you will get a
brighter, but blurrier
image.
:::
```

### fig-accidental-a

```markdown
::{#fig-accidental-a}
<iframe
  src="interactive_imaging/fig-accidental-a.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fig-accidental-b

```markdown
::{#fig-accidental-b}
<iframe
  src="interactive_imaging/fig-accidental-b.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fig-pinhole_names

```markdown
::{#fig-pinhole_names}
<iframe
  src="interactive_imaging/fig-pinhole_names.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Coordinate systems. In computer vision it is common to use the
**right-hand rule** for choosing the orientation of the 3D coordinate
axes.
:::
```

### fig-pinholeGeometry

```markdown
::{#fig-pinholeGeometry}
<iframe
  src="interactive_imaging/fig-pinholeGeometry.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Fig (a) Geometry of the pinhole camera. A 3D point $\mathbf{P}$ projects
into the location $\mathbf{p}$ in the projection plane, located at a
distance $f$ of the pinhole. The virtual camera plane is a radially
symmetric projection of the camera plane. (b) Relation between the
camera, $(x,y)$, and the image coordinate system
$(n,m)$.
:::
```

### fig-pinholeGeometry2

```markdown
::{#fig-pinholeGeometry2}
<iframe
  src="interactive_imaging/fig-pinholeGeometry2.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Perspective projection equations derived geometrically. From similar
triangles, we have $x/f = X/Z$ and $y/f = Y/Z$. Similar triangles are
indicated by the same color.
:::
```

### fig-orthographics

```markdown
::{#fig-orthographics}
<iframe
  src="interactive_imaging/fig-orthographics.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Orthographic projection. Projection is done by parallel rays orthogonal to the projection plane. In this example, we have $x = X$ and $y = Y$.
:::
```

### fig-straw

```markdown
::{#fig-straw}
<iframe
  src="interactive_imaging/fig-straw.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Straw camera example. (a) View through parallel straws. (b) The
subject is a hand in sunlight. (c) The resulting image of the straw
camera (using smaller straws than (a)). The image projection is
orthographic.
:::
```

