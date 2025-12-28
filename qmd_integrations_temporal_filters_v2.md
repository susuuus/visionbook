# Integration Snippets for temporal_filters_v2.qmd

Replace the original ![...](figures/...) with these iframe embeds:

### fig-mov_pulse_012

```markdown
::{#fig-mov_pulse_012}
<iframe
  src="interactive_temporal_filters_v2/fig-mov_pulse_012.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Fig (a) A sequence with one spatial dimension showing a static rectangular pulse. b) The rectangular pulse moves to the left at a speed $v=-0.5$ and c) moving towards the left, $v=-1$. As we work with discretized signals, speed units are in pixels per frame.
:::
```

### sinc.png

```markdown
::{#None}
<iframe
  src="interactive_temporal_filters_v2/fig_sinc.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### heav.png

```markdown
::{#None}
<iframe
  src="interactive_temporal_filters_v2/fig_heav.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fig-seq_filtered_kernel

```markdown
::{#fig-seq_filtered_kernel}
<iframe
  src="interactive_temporal_filters_v2/fig-seq_filtered_kernel.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Fig (a) Spatio-temporal Gaussian with $\sigma=1$ and $\sigma_t=4$. b) Same Gaussian parameters but skewed by the velocity vector $v_x=-1, v_y=0$ pixels/frame, c) and $v_x=1, v_y=0$ pixel/frame.
:::
```

### fig-sec_filtered_blur

```markdown
::{#fig-sec_filtered_blur}
<iframe
  src="interactive_temporal_filters_v2/fig-sec_filtered_blur.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Fig (a) One frame from the input sequence and the space-time section (on top). b) Output when convolving with the Gaussian from @fig-seq_filtered_kernel(a). c) Output of the convolution with @fig-seq_filtered_kernel(b), and d) output of the convolution with @fig-seq_filtered_kernel(c).
:::
```

### fig-gaussian_seq

```markdown
::{#fig-gaussian_seq}
<iframe
  src="interactive_temporal_filters_v2/fig-gaussian_seq.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Visualization of the space-time Gaussian. The Gaussian has a width of $\sigma^2=\sigma_t^2=1.5$, and has been discretized as a 3D array of size $7 \times 7 \times 7$. Each image shows one frame. a) Gaussian b) The partial derivative of the Gaussian with respect to $t$. c) Derivative along $v=(1,0)$ pixels/frame. d) $v=(-1,0)$ pixels/frame.
:::
```

### fig-tunedfilter

```markdown
::{#fig-tunedfilter}
<iframe
  src="interactive_temporal_filters_v2/fig-tunedfilter.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

(a) Input sequence. (b) Output to $h$ with $v_x=v_y=0$. (c) $v_x=1$ pixels/frame. (d) $v_x=-1$ pixel/frame.
:::
```

