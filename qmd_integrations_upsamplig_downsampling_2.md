# Integration Snippets for upsamplig_downsampling_2.qmd

Replace the original ![...](figures/...) with these iframe embeds:

### fig-subsampled_textures

```markdown
::{#fig-subsampled_textures}
<iframe
  src="interactive_upsamplig_downsampling_2/fig-subsampled_textures.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Input image (left) and two decimated versions of the same image with factors $k=2$ and $k=4$.
:::
```

### fig-discrete_delta_train

```markdown
::{#fig-discrete_delta_train}
<iframe
  src="interactive_upsamplig_downsampling_2/fig-discrete_delta_train.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Visualization of three discrete two-dimensional (2D) delta trains with $k=2,4,8$ (top). Corresponding DFTs (bottom). The DFT of a delta train is another delta train.
:::
```

### fig-discrete_texture_sampling

```markdown
::{#fig-discrete_texture_sampling}
<iframe
  src="interactive_upsamplig_downsampling_2/fig-discrete_texture_sampling.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Visualization of an image multiplied by delta trains (top), and their corresponding DFTs (bottom). Only the DFT magnitude is shown.
:::
```

### fig-components_aliasing_FT

```markdown
::{#fig-components_aliasing_FT}
<iframe
  src="interactive_upsamplig_downsampling_2/fig-components_aliasing_FT.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

DFT of an image multiplied by a delta train and the decomposition into the four different translated copies of the DFT of the original input image.
:::
```

### fig-aliasing_in_matrix_form

```markdown
::{#fig-aliasing_in_matrix_form}
<iframe
  src="interactive_upsamplig_downsampling_2/fig-aliasing_in_matrix_form.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Visual representation of \eqn{\@eq-matrixformsubsampling}.
:::
```

### fig-decimationFT_inmatrixform

```markdown
::{#fig-decimationFT_inmatrixform}
<iframe
  src="interactive_upsamplig_downsampling_2/fig-decimationFT_inmatrixform.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Visualization of the product $\mathbf{D}_2 \mathbf{F^*}_{16}$ and its result.
:::
```

### fig-decimation_finalequations_inmatrixform

```markdown
::{#fig-decimation_finalequations_inmatrixform}
<iframe
  src="interactive_upsamplig_downsampling_2/fig-decimation_finalequations_inmatrixform.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Visualization of decimation and aliasing.
:::
```

### fig-discretesinc

```markdown
::{#fig-discretesinc}
<iframe
  src="interactive_upsamplig_downsampling_2/fig-discretesinc.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Discrete sinc function for $N=32$ and $k=2$ and the magnitude of its DFT.
:::
```

### fig-discretesinc_k4

```markdown
::{#fig-discretesinc_k4}
<iframe
  src="interactive_upsamplig_downsampling_2/fig-discretesinc_k4.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Discrete sinc function for $N=32$ and $k=4$ and the magnitude of its DFT.
:::
```

### fig-hamming_window

```markdown
::{#fig-hamming_window}
<iframe
  src="interactive_upsamplig_downsampling_2/fig-hamming_window.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Hamming window ($L=5$) and the magnitude of its DFT.
:::
```

### fig-ringing_artifacts

```markdown
::{#fig-ringing_artifacts}
<iframe
  src="interactive_upsamplig_downsampling_2/fig-ringing_artifacts.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Output of three different low-pass anti-aliasing filters. (left) Ideal low-pass filter. (center) Hamming window. (right) Binomial filter.
:::
```

### fig-downsampling_bilinear

```markdown
::{#fig-downsampling_bilinear}
<iframe
  src="interactive_upsamplig_downsampling_2/fig-downsampling_bilinear.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Downsampling by 2 uses a binomial filter as the anti-aliasing filter followed by decimation by 2.
:::
```

### fig-subsampled_antialiasing_textures

```markdown
::{#fig-subsampled_antialiasing_textures}
<iframe
  src="interactive_upsamplig_downsampling_2/fig-subsampled_antialiasing_textures.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Successive downsampling by a factor of 2 with anti-aliasing. Compare these results with the ones from @fig-subsampled_textures.
:::
```

### fig-upsampling_and_downsampling-nn_interp

```markdown
::{#fig-upsampling_and_downsampling-nn_interp}
<iframe
  src="interactive_upsamplig_downsampling_2/fig-upsampling_and_downsampling-nn_interp.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Nearest neighbor interpolation in 1D and 2D.
:::
```

### fig-bilinear_interp

```markdown
::{#fig-bilinear_interp}
<iframe
  src="interactive_upsamplig_downsampling_2/fig-bilinear_interp.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

1D linear interpolation and 2D bilinear interpolation.
:::
```

### fig-bilinear_interp_k4

```markdown
::{#fig-bilinear_interp_k4}
<iframe
  src="interactive_upsamplig_downsampling_2/fig-bilinear_interp_k4.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Kernels for (left) nearest neighbor, and (right) linear interpolation for $k=4$.
:::
```

### fig-upsamplingazebra

```markdown
::{#fig-upsamplingazebra}
<iframe
  src="interactive_upsamplig_downsampling_2/fig-upsamplingazebra.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Upsampling by a factor of $k=2$ using a bilinear interpolation filter.
:::
```

