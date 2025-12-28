# Integration Snippets for stat_image_models_revised.qmd

Replace the original ![...](figures/...) with these iframe embeds:

### fig-spaces_real_images

```markdown
::{#fig-spaces_real_images}
<iframe
  src="interactive_stat_image_models_revised/fig-spaces_real_images.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

The space of natural images is just very small part of the space of all possible images. In the case of color images with $32\times32$ pixels, most of the space is filled with images that look like noise.
:::
```

### fig-worlds

```markdown
::{#fig-worlds}
<iframe
  src="interactive_stat_image_models_revised/fig-worlds.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Different visual worlds, some real, some synthetic. (a) White noise. (b) Gabor patches. (c) Mondrian. (d) Stars. (e) Clouds. (f) Line drawing. (g) Computer graphic imagery (CGI). (h) A real street.  All these worlds have different visual properties. There is even something that makes CGI images distinct from pictures of true scenes.
:::
```

### fig-noiseInTheWorld

```markdown
::{#fig-noiseInTheWorld}
<iframe
  src="interactive_stat_image_models_revised/fig-noiseInTheWorld.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Telling noise from surface texture. Which one is which?
:::
```

### cubes_with_and_without_noise.jpg

```markdown
::{#None}
<iframe
  src="interactive_stat_image_models_revised/fig_cubes_with_and_without_noise.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

@fig-noiseInTheWorld (b) has noise added
:::
```

### fig-model_training_vs_sampling

```markdown
::{#fig-model_training_vs_sampling}
<iframe
  src="interactive_stat_image_models_revised/fig-model_training_vs_sampling.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Fitting a statistical image model to a set of training images. Once the model is learned we can use the model to sample new images.
:::
```

### fig-model_hist_example

```markdown
::{#fig-model_hist_example}
<iframe
  src="interactive_stat_image_models_revised/fig-model_hist_example.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Estimation of the image model parameters using one image, and then sampling a new image by sampling pixels independently using the histogram of the training image.
:::
```

### fig-histMatch

```markdown
::{#fig-histMatch}
<iframe
  src="interactive_stat_image_models_revised/fig-histMatch.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Examples of images and corresponding random samples with the same distribution of pixel intensities. Only the image with stars (a) has some visual similarity with the randomly sampled image.
:::
```

### fig-illumination

```markdown
::{#fig-illumination}
<iframe
  src="interactive_stat_image_models_revised/fig-illumination.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Perceptual importance of simple histogram manipulations. Figure from @Fleming2001
:::
```

### fig-correlation

```markdown
::{#fig-correlation}
<iframe
  src="interactive_stat_image_models_revised/fig-correlation.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

(center) Scatter plots of pairs of pixels intensities as a function of distance and (right) cross-correlation as a function for vertical (green) and horizontal (red) displacements for the street scene image.
:::
```

### fig-deadleaves

```markdown
::{#fig-deadleaves}
<iframe
  src="interactive_stat_image_models_revised/fig-deadleaves.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Images sampled from the dead leaves model, for different shapes of dead leaves. (a) Circles, and (b) Squares.
:::
```

### fig-FT_angular_averages

```markdown
::{#fig-FT_angular_averages}
<iframe
  src="interactive_stat_image_models_revised/fig-FT_angular_averages.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

(top) Three natural images with size 512 $\times$ 512 pixels, and one random image. (middle) The magnitude of their Fourier transforms (FT), images are transformed to grayscale by averaging the three color channels. (bottom) Plot of the angular average of radial sections of the FT, compared with the curves that correspond to $1/w$, $1/w^{1.5}$, and $1/w^2$, where $w$ is the radial frequency. We can see that the FT of the three natural images decays roughly with $1/w^{\alpha}$. The noise image is very different (has a flat magnitude).
:::
```

### fig-figure_samples_1_over_f

```markdown
::{#fig-figure_samples_1_over_f}
<iframe
  src="interactive_stat_image_models_revised/fig-figure_samples_1_over_f.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

(top) Images are generated by making an image with a random phase and with a magnitude of the power spectrum following $1/ (1+w ^\alpha)$ with $\alpha=1.5$. (bottom) Same generative process applied to each color channel independently. The generated images look like clouds.
:::
```

### fig-magFTMatch

```markdown
::{#fig-magFTMatch}
<iframe
  src="interactive_stat_image_models_revised/fig-magFTMatch.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Examples of images and random samples with the same magnitude of the FT of the corresponding image. We use PCA in color space to find decorrelated color components. Then, each decorrelated color channel is sampled independently and the final image is created by returning to the original color space. Only the image with clouds (b) has some visual similarity with the randomly sampled image.
:::
```

### fig-hair-a

```markdown
::{#fig-hair-a}
<iframe
  src="interactive_stat_image_models_revised/fig-hair-a.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fig-hair-b

```markdown
::{#fig-hair-b}
<iframe
  src="interactive_stat_image_models_revised/fig-hair-b.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fig-denoisingGaussianModel

```markdown
::{#fig-denoisingGaussianModel}
<iframe
  src="interactive_stat_image_models_revised/fig-denoisingGaussianModel.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

(Top row) Ground truth decomposition of image into Gaussian white noise and the image, uncorrupted by noise.  (bottom row) Gaussian image model denoising results.  Note that the estimated noise image shows residual spatial structure from the original image.
:::
```

### fig-derivativeshist

```markdown
::{#fig-derivativeshist}
<iframe
  src="interactive_stat_image_models_revised/fig-derivativeshist.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

(a) Input image.  (b) Horizontal and (c) vertical derivatives of the input image.  (d) Histogram of pixel intensities of the input image.  (e and f) Histograms of the two derivatives of the original image. Note that both histograms have non-Gaussian distributions, a characteristic of natural images.
:::
```

### fig-derivativesdistributions

```markdown
::{#fig-derivativesdistributions}
<iframe
  src="interactive_stat_image_models_revised/fig-derivativesdistributions.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Comparison of histograms of images from different visual worlds, and band-pass filtered versions of those images. (top row) Gaussian noise.  Band-pass filtered Gaussian noise is still Gaussian distributed.  (middle and bottom rows) Two very different looking images, when band-pass filtered, have similar looking non-Gaussian, narrowly peaked histogram distributions. The black line shows the best Gaussian fit, a poor fit to the spiky histograms.
:::
```

### fig-generalizedgaussian

```markdown
::{#fig-generalizedgaussian}
<iframe
  src="interactive_stat_image_models_revised/fig-generalizedgaussian.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Generalized Laplacian distribution with $s=1$ and (a) $r=0.1$, (b) $r=1$, (c) $r=2$, and (d) $r=10$. %Changing the exponent $r$ changes the shape of the distribution, generating some special case probability distributions (Gaussian, uniform, Laplacian).
:::
```

### fig-best_a

```markdown
::{#fig-best_a}
<iframe
  src="interactive_stat_image_models_revised/fig-best_a.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Reconstructed signal using (left) $r=2$ and (right) $r=0.5$. The estimated values of $a$ are 0.5 and 1.
:::
```

### fig-waveletBayes

```markdown
::{#fig-waveletBayes}
<iframe
  src="interactive_stat_image_models_revised/fig-waveletBayes.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Showing the likelihood, prior, and posterior terms for the estimation of a subband coefficient from several noisy observations.  (a)  A zero subband coefficient is observed. (b)  An observation of 0.26 shifts the likelihood term, but the posterior still has a peak at zero. (c) an observed coefficient value of 1.22 yields a maximum posterior probability estimate of 0.9.
:::
```

### fig-bayeslut

```markdown
::{#fig-bayeslut}
<iframe
  src="interactive_stat_image_models_revised/fig-bayeslut.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Input/output coring curve for maximum posterior denoising for the example of @fig-waveletBayes
:::
```

### nlm1.jpg

```markdown
::{#None}
<iframe
  src="interactive_stat_image_models_revised/fig_nlm1.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fig-nlm2

```markdown
::{#fig-nlm2}
<iframe
  src="interactive_stat_image_models_revised/fig-nlm2.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Nonlocal means denoising algorithm results. (left) Original image without noise. (middle) Noisy image. (right) Denoised image.*Source*:Figure from @Baudes2011
:::
```

### fig-spaces_real_images_final

```markdown
::{#fig-spaces_real_images_final}
<iframe
  src="interactive_stat_image_models_revised/fig-spaces_real_images_final.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

The space of natural images is just very small part of the space of all possible images. In the case of color images with $32 \times 32$ pixels, most of the space is filled with images that look like noise.
:::
```

