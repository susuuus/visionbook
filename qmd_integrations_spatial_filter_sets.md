# Integration Snippets for spatial_filter_sets.qmd

Replace the original ![...](figures/...) with these iframe embeds:

### fig-1D_gabor_function

```markdown
::{#fig-1D_gabor_function}
<iframe
  src="interactive_spatial_filter_sets/fig-1D_gabor_function.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Construction of a Gabor function. (a) Sine function. (b) Gaussian function. (c) Gabor function obtained as the product of (a) and (b).
:::
```

### fig-gabors

```markdown
::{#fig-gabors}
<iframe
  src="interactive_spatial_filter_sets/fig-gabors.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

2D Gabor functions.  (a) The localizing Gaussian window ($\sigma=1$), which can be thought of as a Gabor function for a zero frequency sinusoid.  (b) Cosine, and (c) sine phase Gabor functions with central frequency $u_0=2\pi$ and $v_0=0$.
:::
```

### fig-gabor_ft

```markdown
::{#fig-gabor_ft}
<iframe
  src="interactive_spatial_filter_sets/fig-gabor_ft.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

(a) Cosine and (b) sine Gabor functions. (c) Magnitude of the Fourier transform of both the cosine and sine Gabor functions (their FT only differs in the phase). (d) FT of the complex Gabor function, which is asymmetrical with a single lobe.
:::
```

### fig-gabor_ex_ft

```markdown
::{#fig-gabor_ex_ft}
<iframe
  src="interactive_spatial_filter_sets/fig-gabor_ex_ft.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Cosine phase Gabor functions tuned to different widths, frequencies, and orientations, and their corresponding Fourier transforms (only the magnitude is shown).
:::
```

### fig-gabor_zebra

```markdown
::{#fig-gabor_zebra}
<iframe
  src="interactive_spatial_filter_sets/fig-gabor_zebra.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Zebra picture filtered by cosine and sine Gabor functions at three scales with $\sigma = 2,4,8$ and $u_0 = 1/(2\sigma)$, $v_0=0$. Each row shows one scale. (a) Cosine and sine Gabor filters. (b) Cosine and sine outputs. (c) Magnitude and phase of the output of the complex Gabor filter.
:::
```

### fig-quad2

```markdown
::{#fig-quad2}
<iframe
  src="interactive_spatial_filter_sets/fig-quad2.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Computation of localized amplitude. The input is filtered by a pair of quadrature Gabor filters. Each filter output is squared and the result is added.
:::
```

### fig-quad3

```markdown
::{#fig-quad3}
<iframe
  src="interactive_spatial_filter_sets/fig-quad3.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Examples of Gabor outputs to illustrate the contrast invariances present in the local amplitude. In these examples the Gabor filters are centered along the horizontal frequency axis ($v_0=0$) therefore detecting only vertical edges.
:::
```

### fig-gabor_rectandpolar_tiles

```markdown
::{#fig-gabor_rectandpolar_tiles}
<iframe
  src="interactive_spatial_filter_sets/fig-gabor_rectandpolar_tiles.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Examples of Gabor sets. Two different ways of tiling the frequency domain.
:::
```

### fig-steer1

```markdown
::{#fig-steer1}
<iframe
  src="interactive_spatial_filter_sets/fig-steer1.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

The simplest steerable filters: a first-order derivative filter of any
  orientation can be synthesized from a linear combination of two
  basis filter derivatives. The second-order derivative needs three basis.
:::
```

### fig-steer1arc

```markdown
::{#fig-steer1arc}
<iframe
  src="interactive_spatial_filter_sets/fig-steer1arc.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Architecture for steerable filters. This architecture computes the second-order image derivative along orientation $\theta$.
:::
```

### fig-steer_quad_basis

```markdown
::{#fig-steer_quad_basis}
<iframe
  src="interactive_spatial_filter_sets/fig-steer_quad_basis.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

(a) Second derivative of Gaussian, $x-y$
separable steerable basis set. b) Approximation to Hilbert transform of second derivative of  Gaussian, $x-y$ steerable basis set. (c)  Nonseparable basis equivalent to (a). (d) Nonseparable basis set equivalent to (b).
:::
```

### fig-multioriflorets

```markdown
::{#fig-multioriflorets}
<iframe
  src="interactive_spatial_filter_sets/fig-multioriflorets.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

(Polar plots of orientation energy as a function of angle, computed using $g_{xx}$, $h_{xx}$ filters. (a) Note the non-superposition of oriented energies near the junction of the two lines. (b) Spatially blurring the oriented energy components of the filters results in much improved linear superposition of the orientation plots, removing spurious interference terms, as described in the text.
:::
```

### fig-multioriflorets_examples

```markdown
::{#fig-multioriflorets_examples}
<iframe
  src="interactive_spatial_filter_sets/fig-multioriflorets_examples.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Polar plots of orientation energy as a function of angle, computed using $g_{xx}$, $h_{xx}$ filters in two images.
:::
```

### fig-spacetimefilts

```markdown
::{#fig-spacetimefilts}
<iframe
  src="interactive_spatial_filter_sets/fig-spacetimefilts.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Space-time Gabor filters. (a) Cosine and sine $x$-$t$ Gabor filter, and (b) the sketch of its transfer function. (c) Sketch of the transfer function of a spatiotemporal Gabor filter in two spatial dimensions ($x$-$y$-$t$). The two planes show examples of spatiotemporal planes that intersect the Gabor filter in the same way.
:::
```

### fig-spacetimetiles2

```markdown
::{#fig-spacetimetiles2}
<iframe
  src="interactive_spatial_filter_sets/fig-spacetimetiles2.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fig-MT_velocity_tuned

```markdown
::{#fig-MT_velocity_tuned}
<iframe
  src="interactive_spatial_filter_sets/fig-MT_velocity_tuned.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Architecture to create velocity-selective units. In the first layer, cosine and sine filters are combined to create phase-invariant frequency-tuned outputs. In the second layer, the outputs of spatiotemporal Gabor filters are grouped according to different planes in the Fourier domain to create velocity-selective outputs.
:::
```

