# Integration Snippets for sampling_and_aliasing.qmd

Replace the original ![...](figures/...) with these iframe embeds:

### fig-cosine_wave_before_sampling

```markdown
::{#fig-cosine_wave_before_sampling}
<iframe
  src="interactive_sampling_and_aliasing/fig-cosine_wave_before_sampling.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Continuous cosine wave, $\ell (t)=\cos (wt)$, with frequency $w=18\pi$.
:::
```

### fig-cosine_wave_after_sampling

```markdown
::{#fig-cosine_wave_after_sampling}
<iframe
  src="interactive_sampling_and_aliasing/fig-cosine_wave_after_sampling.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Sampling the cosine wave with a sampling period of $T_s=1/11$.
:::
```

### fig-sampling_reconstruction1

```markdown
::{#fig-sampling_reconstruction1}
<iframe
  src="interactive_sampling_and_aliasing/fig-sampling_reconstruction1.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

There are infinite waves (only two shown) that perfectly pass by all the samples.
:::
```

### fig-alaising-a

```markdown
::{#fig-alaising-a}
<iframe
  src="interactive_sampling_and_aliasing/fig-alaising-a.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fig-aliasing-b

```markdown
::{#fig-aliasing-b}
<iframe
  src="interactive_sampling_and_aliasing/fig-aliasing-b.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fig-band_limited_signal

```markdown
::{#fig-band_limited_signal}
<iframe
  src="interactive_sampling_and_aliasing/fig-band_limited_signal.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

A band-limited signal with maximum frequency $w_{max}$.
:::
```

### fig-delta_train

```markdown
::{#fig-delta_train}
<iframe
  src="interactive_sampling_and_aliasing/fig-delta_train.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Delta train with period $T_s=1$. The arrows show when the train's value is infinite. The height of each impulse represents its area.
:::
```

### fig-sampling_signal_using_train

```markdown
::{#fig-sampling_signal_using_train}
<iframe
  src="interactive_sampling_and_aliasing/fig-sampling_signal_using_train.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Sampling a signal using the delta train.
:::
```

### fig-sketch_aliasing

```markdown
::{#fig-sketch_aliasing}
<iframe
  src="interactive_sampling_and_aliasing/fig-sketch_aliasing.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Sketch to illustrate aliasing. Example of a band-limited signal, with frequency content only inside the interval $(-w_{max}, w_{max})$. (a) Sampled with a sampling period such a that $T_s < \pi/w_{max}$. (b) Sampled with a period $T_s > \pi/w_{max}$. Aliasing is due to the overlap between the translated copies of the signal Fourier transform, $\mathscr{L}(w)$.
:::
```

### fig-sinc_function

```markdown
::{#fig-sinc_function}
<iframe
  src="interactive_sampling_and_aliasing/fig-sinc_function.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Sinc function. This signal is a modulated sine signal with an amplitude decay of $1/t$. The frequency is normalized so that the zero crossings happen at integer values.
:::
```

### fig-sampling_reconstruction2

```markdown
::{#fig-sampling_reconstruction2}
<iframe
  src="interactive_sampling_and_aliasing/fig-sampling_reconstruction2.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Smooth interpolation of the sampled function using sinc functions.
:::
```

### fig-alias1d

```markdown
::{#fig-alias1d}
<iframe
  src="interactive_sampling_and_aliasing/fig-alias1d.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

(left column)  Spatial sampling pattern.  (middle column)  Fourier transform of that spatial pattern, revealing replication locations of the Fourier transform spectrum of the subsampled signal.  (right column) Subsampled signal.  Zeroing out all but the central replication of the image spectrum yields the interpolated signal shown in red.
:::
```

### fig-sampling_reconstruction3

```markdown
::{#fig-sampling_reconstruction3}
<iframe
  src="interactive_sampling_and_aliasing/fig-sampling_reconstruction3.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

(top) Nearest interpolation. (bottom) Linear interpolation. Both interpolation methods can be modeled by a convolution with the kernel shown in the middle (a box and a triangle).
:::
```

### fig-sampling_grids

```markdown
::{#fig-sampling_grids}
<iframe
  src="interactive_sampling_and_aliasing/fig-sampling_grids.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Three types of sampling: rectangular grid, hexagonal, and irregular.
:::
```

### fig-sampling_grids_FT

```markdown
::{#fig-sampling_grids_FT}
<iframe
  src="interactive_sampling_and_aliasing/fig-sampling_grids_FT.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Sketch of the Fourier transforms of the rectangular and hexagonal samplings. The red boundary denotes the spectral content that gets periodically repeated.
:::
```

### fig-samplingfovea

```markdown
::{#fig-samplingfovea}
<iframe
  src="interactive_sampling_and_aliasing/fig-samplingfovea.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Distributions of cones in the fovea of a Monkey  \cite{Curcio1990
:::
```

### moire.png

```markdown
::{#None}
<iframe
  src="interactive_sampling_and_aliasing/fig_moire.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

