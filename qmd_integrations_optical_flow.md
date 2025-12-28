# Integration Snippets for optical_flow.qmd

Replace the original ![...](figures/...) with these iframe embeds:

### fig-visualization_optical_flow

```markdown
::{#fig-visualization_optical_flow}
<iframe
  src="interactive_optical_flow/fig-visualization_optical_flow.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Two frames of a sequence, ground-truth optical flow (color coded), and the color code to read the vector at each pixel.
:::
```

### fig-apperture_problem

```markdown
::{#fig-apperture_problem}
<iframe
  src="interactive_optical_flow/fig-apperture_problem.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Aperture problem when observing the motion of a one-dimensional (1D) structure larger than the image frame. The actual motion of the bar is upward, but the perception, when vision is limited to what is visible within the observation window, appears as if the motion of the bar is in the direction perpendicular to the bar.
:::
```

### barber_pole.png

```markdown
::{#None}
<iframe
  src="interactive_optical_flow/fig_barber_pole.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fig-toy_motion_figure

```markdown
::{#fig-toy_motion_figure}
<iframe
  src="interactive_optical_flow/fig-toy_motion_figure.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Translation to the right of a simple $6 \times 6$ size image.
:::
```

### gradient_algorithm.png

```markdown
::{#None}
<iframe
  src="interactive_optical_flow/fig_gradient_algorithm.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Gradient-based optical flow estimation using two input frames.
:::
```

### fig-square_grandient_based_1

```markdown
::{#fig-square_grandient_based_1}
<iframe
  src="interactive_optical_flow/fig-square_grandient_based_1.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Toy sequence with two moving squares. The red arrows indicate the direction of motion of each square.
:::
```

### fig-square_grandient_based_2

```markdown
::{#fig-square_grandient_based_2}
<iframe
  src="interactive_optical_flow/fig-square_grandient_based_2.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Spatial and temporal derivatives for the sequence from @fig-square_grandient_based_1
:::
```

### fig-square_grandient_based_3

```markdown
::{#fig-square_grandient_based_3}
<iframe
  src="interactive_optical_flow/fig-square_grandient_based_3.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Computation of all the products between derivatives from @fig-square_grandient_based_2
:::
```

### fig-square_grandient_based_5

```markdown
::{#fig-square_grandient_based_5}
<iframe
  src="interactive_optical_flow/fig-square_grandient_based_5.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Estimated optical flow for the sequence in @fig-square_grandient_based_2
:::
```

### fig-square_grandient_based_4

```markdown
::{#fig-square_grandient_based_4}
<iframe
  src="interactive_optical_flow/fig-square_grandient_based_4.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Estimated optical flow in the regions with $R > 2$ (around *good features to track* @shi1994goodfeatures
:::
```

### fig-multiscale_iterative_optical_flow

```markdown
::{#fig-multiscale_iterative_optical_flow}
<iframe
  src="interactive_optical_flow/fig-multiscale_iterative_optical_flow.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Multiscale iterative refinement for optical flow. Optical flow estimation is done on a Gaussian pyramid. (left) First, we run a few iterations on the lowest resolution scale of the pyramid (where the motion will be the smallest). The estimated motion is then upsampled and used as the initialization at the next level. (right) We iterate this process until arriving at the highest possible resolution.
:::
```

### fig-comparison_gradient_vs_iterative

```markdown
::{#fig-comparison_gradient_vs_iterative}
<iframe
  src="interactive_optical_flow/fig-comparison_gradient_vs_iterative.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Comparison between the optical flow estimated using the gradient-based algorithm and the multiscale iterative refinement approach.
:::
```

