# Integration Snippets for conditional_generative_models.qmd

Replace the original ![...](figures/...) with these iframe embeds:

### fig-conditional_generative_models-tshirts

```markdown
::{#fig-conditional_generative_models-tshirts}
<iframe
  src="interactive_conditional_generative_models/fig-conditional_generative_models-tshirts.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Different kinds of predictive distributions.
:::
```

### fig-conditional_generative_models-color_quantization

```markdown
::{#fig-conditional_generative_models-color_quantization}
<iframe
  src="interactive_conditional_generative_models/fig-conditional_generative_models-color_quantization.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

The funny shape of the $lab$ color gamut is because not every $ab$ value maps to a valid pixel color. When working with predictions over $lab$ color space, we may map $ab$ values that fall outside the gamut (valid range) to the nearest in-gamut value.
:::
```

### fig-conditional_generative_models-cgen_tshirt_color_inconsistency

```markdown
::{#fig-conditional_generative_models-cgen_tshirt_color_inconsistency}
<iframe
  src="interactive_conditional_generative_models/fig-conditional_generative_models-cgen_tshirt_color_inconsistency.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Color flipping can arise from a smooth underlying predictive distribution, on top of which independent choices are made.
:::
```

### graphical_model_x_z_to_y.png

```markdown
::{#None}
<iframe
  src="interactive_conditional_generative_models/fig_graphical_model_x_z_to_y.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fig-conditional_generative_models-cVAE_ball_bouncing_example

```markdown
::{#fig-conditional_generative_models-cVAE_ball_bouncing_example}
<iframe
  src="interactive_conditional_generative_models/fig-conditional_generative_models-cVAE_ball_bouncing_example.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

A scenario where a yellow ball is moving across a plane. The observation, $\mathbf{x}$, is a static frame. From that observation, we know what will be the color and rough position of the ball in the next frame, $\mathbf{y}$, but we don't know what direction it will have moved, because the velocity of the ball is unobserved. Therefore, velocity is a latent variable and one solution to the cVAE objective will be to encode in the model's latent variables ($\mathbf{z}$) the velocity of the ball, as is depicted here.
:::
```

### fig-conditional_generative_models-cVAE_ball_bouncing_example_nets

```markdown
::{#fig-conditional_generative_models-cVAE_ball_bouncing_example_nets}
<iframe
  src="interactive_conditional_generative_models/fig-conditional_generative_models-cVAE_ball_bouncing_example_nets.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

cVAE architecture. The dotted lines indicate that the *target encoder* is only used during training; at test time, usage follows the solid path.
:::
```

### fig-conditional_generative_models-text_conditional_diffusion_model

```markdown
::{#fig-conditional_generative_models-text_conditional_diffusion_model}
<iframe
  src="interactive_conditional_generative_models/fig-conditional_generative_models-text_conditional_diffusion_model.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Text-conditional diffusion model.
:::
```

### fig-conditional_generative_models-pix2pix_facades_arch

```markdown
::{#fig-conditional_generative_models-pix2pix_facades_arch}
<iframe
  src="interactive_conditional_generative_models/fig-conditional_generative_models-pix2pix_facades_arch.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

The pix2pix @pix2pix2017 model applied to translating a facade layout map into a photo of the facade. The model was trained on the CMP Facades Database @Tylecek13 and the input and ground truth images shown here are from that dataset.
:::
```

### fig-conditional_generative_models-cGAN_as_learned_loss

```markdown
::{#fig-conditional_generative_models-cGAN_as_learned_loss}
<iframe
  src="interactive_conditional_generative_models/fig-conditional_generative_models-cGAN_as_learned_loss.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

The discriminator of a GAN as a learned loss function.
:::
```

### fig-conditional_generative_models-patchgan_patch_size_variations

```markdown
::{#fig-conditional_generative_models-patchgan_patch_size_variations}
<iframe
  src="interactive_conditional_generative_models/fig-conditional_generative_models-patchgan_patch_size_variations.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Varying the receptive field (patch size) of the convolutional discriminator affects what kinds of structure the discriminator enforces. These results are from @pix2pix2017
:::
```

### fig-conditional_generative_models-cyclegan_teaser

```markdown
::{#fig-conditional_generative_models-cyclegan_teaser}
<iframe
  src="interactive_conditional_generative_models/fig-conditional_generative_models-cyclegan_teaser.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

A style transfer example from the CycleGAN paper @CycleGAN2017 *Input photo source*: Alexei A. Efros.
:::
```

### fig-conditional_generative_models-paired_vs_unpaired

```markdown
::{#fig-conditional_generative_models-paired_vs_unpaired}
<iframe
  src="interactive_conditional_generative_models/fig-conditional_generative_models-paired_vs_unpaired.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

(left) An example of paired image-to-image translation (colorization) versus (right) unpaired translation (photo to Cezanne). Figure adapted from @CycleGAN2017
:::
```

### fig-conditional_generative_models-cyclegan_schematic

```markdown
::{#fig-conditional_generative_models-cyclegan_schematic}
<iframe
  src="interactive_conditional_generative_models/fig-conditional_generative_models-cyclegan_schematic.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

CycleGAN schematic. Figure derived from @CycleGAN2017
:::
```

