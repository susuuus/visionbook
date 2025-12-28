# Integration Snippets for generative_modeling_and_rep_learning.qmd

Replace the original ![...](figures/...) with these iframe embeds:

### fig-generative_modeling_and_representation_learning-rep_gen_schematic

```markdown
::{#fig-generative_modeling_and_representation_learning-rep_gen_schematic}
<iframe
  src="interactive_generative_modeling_and_rep_learning/fig-generative_modeling_and_representation_learning-rep_gen_schematic.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

The relationship between representation learning and generative modeling. Here we label one side as "Data" and the other as "Embedding"; but what's the precise difference between these two things? Why is an RGB image data while a 100-dimensional vector of neural activations is an embedding? This is a question for you to think about; there is no correct answer.
:::
```

### fig-generative_modeling_and_representation_learning-genrep_schematic

```markdown
::{#fig-generative_modeling_and_representation_learning-genrep_schematic}
<iframe
  src="interactive_generative_modeling_and_rep_learning/fig-generative_modeling_and_representation_learning-genrep_schematic.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Generative modeling performs the opposite mapping from representation learning.
:::
```

### fig-generative_modeling_and_representation_learning-autoencoder_to_generative_model

```markdown
::{#fig-generative_modeling_and_representation_learning-autoencoder_to_generative_model}
<iframe
  src="interactive_generative_modeling_and_rep_learning/fig-generative_modeling_and_representation_learning-autoencoder_to_generative_model.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

The relationship between an autoencoder and a generative model.
:::
```

### fig-generative_modeling_and_representation_learning-autoencoder_complicated_latent_space

```markdown
::{#fig-generative_modeling_and_representation_learning-autoencoder_complicated_latent_space}
<iframe
  src="interactive_generative_modeling_and_rep_learning/fig-generative_modeling_and_representation_learning-autoencoder_complicated_latent_space.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

The latent space of an autoencoder can be just as complex as the data space.
:::
```

### fig-generative_modeling_and_representation_learning-gmm_vs_vae

```markdown
::{#fig-generative_modeling_and_representation_learning-gmm_vs_vae}
<iframe
  src="interactive_generative_modeling_and_rep_learning/fig-generative_modeling_and_representation_learning-gmm_vs_vae.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

From a finite mixture of Gaussians to an infinite mixture.
:::
```

### fig-generative_modeling_and_representation_learning-IGMM_training_iters

```markdown
::{#fig-generative_modeling_and_representation_learning-IGMM_training_iters}
<iframe
  src="interactive_generative_modeling_and_rep_learning/fig-generative_modeling_and_representation_learning-IGMM_training_iters.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Fitting an infinite mixture of Gaussians whose means and variances are parameterized by a generator function $g_\theta$
:::
```

### fig-generative_modeling_and_representation_learning-vae_importance_sampling1

```markdown
::{#fig-generative_modeling_and_representation_learning-vae_importance_sampling1}
<iframe
  src="interactive_generative_modeling_and_rep_learning/fig-generative_modeling_and_representation_learning-vae_importance_sampling1.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

To estimate $p_{\theta}(\mathbf{x})$ we only need to consider the Gaussian components (gray circles) that place significant probability on $\mathbf{x}$.
:::
```

### fig-generative_modeling_and_representation_learning-vae_importance_sampling2

```markdown
::{#fig-generative_modeling_and_representation_learning-vae_importance_sampling2}
<iframe
  src="interactive_generative_modeling_and_rep_learning/fig-generative_modeling_and_representation_learning-vae_importance_sampling2.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Optimal importance sampling estimates $p_{\theta}(\mathbf{x})$ by drawing samples from $p_{\theta}(Z \\| \mathbf{x})$.
:::
```

### fig-generative_modeling_and_representation_learning-VAE_encoder

```markdown
::{#fig-generative_modeling_and_representation_learning-VAE_encoder}
<iframe
  src="interactive_generative_modeling_and_rep_learning/fig-generative_modeling_and_representation_learning-VAE_encoder.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

A VAE's encoder, $f_{\psi}$, models $p(Z \\| \mathbf{x})$ as a Gaussian parameterized by $f_{\psi}(\mathbf{x})$.
:::
```

### fig-generative_modeling_and_representation_learning-VAE_as_autoencoder

```markdown
::{#fig-generative_modeling_and_representation_learning-VAE_as_autoencoder}
<iframe
  src="interactive_generative_modeling_and_rep_learning/fig-generative_modeling_and_representation_learning-VAE_as_autoencoder.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

To evaluate the likelihood a VAE places on a datapoint $x$, we encode $x$ into $z$-space and then decode back and compute the reconstruction error. This corresponds to one importance sample for approximating the likelihood function.
:::
```

### fig-generative_modeling_and_representation_learning-VAE_training_iters

```markdown
::{#fig-generative_modeling_and_representation_learning-VAE_training_iters}
<iframe
  src="interactive_generative_modeling_and_rep_learning/fig-generative_modeling_and_representation_learning-VAE_training_iters.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Training a VAE to model the blue distribution. The Gaussian components spread out to tile both the embedding space and the data space.
:::
```

### fig-generative_modeling_and_representation_learning-rivers_dataset

```markdown
::{#fig-generative_modeling_and_representation_learning-rivers_dataset}
<iframe
  src="interactive_generative_modeling_and_rep_learning/fig-generative_modeling_and_representation_learning-rivers_dataset.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

A toy generative model hand-coded in Python.
:::
```

### fig-generative_modeling_and_representation_learning-vae_rivers_samples

```markdown
::{#fig-generative_modeling_and_representation_learning-vae_rivers_samples}
<iframe
  src="interactive_generative_modeling_and_rep_learning/fig-generative_modeling_and_representation_learning-vae_rivers_samples.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Fitting a VAE to the rivers dataset
:::
```

### fig-generative_modeling_and_representation_learning-vae_rivers_latent_walk

```markdown
::{#fig-generative_modeling_and_representation_learning-vae_rivers_latent_walk}
<iframe
  src="interactive_generative_modeling_and_rep_learning/fig-generative_modeling_and_representation_learning-vae_rivers_latent_walk.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Walking along two axes of latent space generates images that show variation in two distinct attributes, demonstrating that this model is, to a degree, disentangled.
:::
```

### fig-generative_modeling_and_representation_learning-biggan_latent_walk

```markdown
::{#fig-generative_modeling_and_representation_learning-biggan_latent_walk}
<iframe
  src="interactive_generative_modeling_and_rep_learning/fig-generative_modeling_and_representation_learning-biggan_latent_walk.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Walking in in two orthogonal directions in BigGAN @brock2018large
:::
```

