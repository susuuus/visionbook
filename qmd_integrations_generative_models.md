# Integration Snippets for generative_models.qmd

Replace the original ![...](figures/...) with these iframe embeds:

### fig-gen_models_image_classification

```markdown
::{#fig-gen_models_image_classification}
<iframe
  src="interactive_generative_models/fig-gen_models_image_classification.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

A classifier maps images to labels.
:::
```

### fig-gen_models_image_generation

```markdown
::{#fig-gen_models_image_generation}
<iframe
  src="interactive_generative_models/fig-gen_models_image_generation.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

A generator maps labels (or other descriptions) to images.
:::
```

### graphical_model_y_z_to_x_white.png

```markdown
::{#None}
<iframe
  src="interactive_generative_models/fig_graphical_model_y_z_to_x_white.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fig-generative_models-image_generation_with_z

```markdown
::{#fig-generative_models-image_generation_with_z}
<iframe
  src="interactive_generative_models/fig-generative_models-image_generation_with_z.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Making a generator stochastic by conditioning on a random variable.
:::
```

### graphical_model_z_to_x_white.png

```markdown
::{#None}
<iframe
  src="interactive_generative_models/fig_graphical_model_z_to_x_white.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### simple_rivers_script.png

```markdown
::{#None}
<iframe
  src="interactive_generative_models/fig_simple_rivers_script.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

A simple generative model that draws images of rivers.
:::
```

### fig-generative_models-rivers1

```markdown
::{#fig-generative_models-rivers1}
<iframe
  src="interactive_generative_models/fig-generative_models-rivers1.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Procedurally generated rivers.
:::
```

### fig-generative_models-gen_model_of_rivers_diagram

```markdown
::{#fig-generative_models-gen_model_of_rivers_diagram}
<iframe
  src="interactive_generative_models/fig-generative_models-gen_model_of_rivers_diagram.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

A generator that makes procedural rivers.
:::
```

### fig-generative_models-gen_model_training_vs_sampling

```markdown
::{#fig-generative_models-gen_model_training_vs_sampling}
<iframe
  src="interactive_generative_models/fig-generative_models-gen_model_training_vs_sampling.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Learning and using a generator.
:::
```

### fig-generative_models-gen_model_training_vs_sampling_indirect

```markdown
::{#fig-generative_models-gen_model_training_vs_sampling_indirect}
<iframe
  src="interactive_generative_models/fig-generative_models-gen_model_training_vs_sampling_indirect.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

The indirect approach to generative modeling. The scoring function can be either a probability density or an energy function. The models we learned about in @sec-stat_image_models.
:::
```

### fig-generative_models-max_likelihood_density

```markdown
::{#fig-generative_models-max_likelihood_density}
<iframe
  src="interactive_generative_models/fig-generative_models-max_likelihood_density.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Fitting a max likelihood density model to data. The gray region holds a constant amount of mass; think of it as piles of dirt. To increase the amount of dirt at the locations of the green arrows you must remove dirt from other regions, indicated in red.
:::
```

### fig-generative_models-contrastive_divergence

```markdown
::{#fig-generative_models-contrastive_divergence}
<iframe
  src="interactive_generative_models/fig-generative_models-contrastive_divergence.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Fitting a max likelihood energy function to data, using contrastive divergence. @hinton2002training
:::
```

### 1d_gaussian_summary.png

```markdown
::{#None}
<iframe
  src="interactive_generative_models/fig_1d_gaussian_summary.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fig-generative_models-autoregressive_prediction_schematic

```markdown
::{#fig-generative_models-autoregressive_prediction_schematic}
<iframe
  src="interactive_generative_models/fig-generative_models-autoregressive_prediction_schematic.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

An autoregressive model, $f_{\theta}$, that generates an image pixel by pixel. The black pixels are the remaining pixels to synthesize. Compare with the Efros-Leung model in @fig-sampling_efros_leung.
:::
```

### fig-generative_models-autoregressive_softmax_regression

```markdown
::{#fig-generative_models-autoregressive_softmax_regression}
<iframe
  src="interactive_generative_models/fig-generative_models-autoregressive_softmax_regression.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Autoregressive prediction as next-pixel-classification.
:::
```

### fig-generative_models-autoregressive_train_predict

```markdown
::{#fig-generative_models-autoregressive_train_predict}
<iframe
  src="interactive_generative_models/fig-generative_models-autoregressive_train_predict.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Training an autoregressive model, then sampling images from it.
:::
```

### fig-generative_models-reverse_autoregressive_sequence

```markdown
::{#fig-generative_models-reverse_autoregressive_sequence}
<iframe
  src="interactive_generative_models/fig-generative_models-reverse_autoregressive_sequence.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

An autoregressive sequence in reverse is a corruption process that removes one pixel at a time.
:::
```

### fig-generative_models-forward_diffusion_process

```markdown
::{#fig-generative_models-forward_diffusion_process}
<iframe
  src="interactive_generative_models/fig-generative_models-forward_diffusion_process.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Forward diffusion process.
:::
```

### fig-generative_models-reverse_diffusion_process

```markdown
::{#fig-generative_models-reverse_diffusion_process}
<iframe
  src="interactive_generative_models/fig-generative_models-reverse_diffusion_process.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Reverse diffusion process. The forward process creates supervision to train the reverse process.
:::
```

### diffusion_model.png

```markdown
::{#None}
<iframe
  src="interactive_generative_models/fig_diffusion_model.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Training a diffusion model consists of first producing training pairs of the form {noisy image, less noisy image}. Then do supervised learning on these pairs.
:::
```

### fig-generative_models-generative_models-gan_schematic

```markdown
::{#fig-generative_models-generative_models-gan_schematic}
<iframe
  src="interactive_generative_models/fig-generative_models-generative_models-gan_schematic.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Architecture of a GAN being trained to generate images of flamingos. The synthetic image in this example is generated by BigGAN @brock2018large
:::
```

