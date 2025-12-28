# Integration Snippets for motion_estimation.qmd

Replace the original ![...](figures/...) with these iframe embeds:

### fig-supervised_estimation

```markdown
::{#fig-supervised_estimation}
<iframe
  src="interactive_motion_estimation/fig-supervised_estimation.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

In FlowNet the direct approach estimates optical flow directly from a pair of frames.
:::
```

### fig-supervised_estimation_modular

```markdown
::{#fig-supervised_estimation_modular}
<iframe
  src="interactive_motion_estimation/fig-supervised_estimation_modular.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Motion estimation. (1) Extract features from each image; (2) compute a 3D cost volume; and (3) aggregate the cost volume in order to estimate the best optical flow for each pixel.
:::
```

### endpoint_error.png

```markdown
::{#None}
<iframe
  src="interactive_motion_estimation/fig_endpoint_error.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

