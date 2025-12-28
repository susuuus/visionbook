# Integration Snippets for textures.qmd

Replace the original ![...](figures/...) with these iframe embeds:

### fig-infinite_texture

```markdown
::{#fig-infinite_texture}
<iframe
  src="interactive_textures/fig-infinite_texture.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

The infinite texture generation algorithm. If we had access to a very large image of the texture we want to generate, we could just crop pieces from it to create new images.
:::
```

### stone_wall.jpg

```markdown
::{#None}
<iframe
  src="interactive_textures/fig_stone_wall.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fig-parallel_counting

```markdown
::{#fig-parallel_counting}
<iframe
  src="interactive_textures/fig-parallel_counting.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

When looking at these images, we can count the number of circles at a glance if there are less than five circles. When an image has more than five items, we have to count them one by one.
:::
```

### fig-crowding

```markdown
::{#fig-crowding}
<iframe
  src="interactive_textures/fig-crowding.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Crowding. If you look at the central cross, the letter R on the right can be recognized, however the letter B on the left is hard to read.
:::
```

### fig-julez_texture

```markdown
::{#fig-julez_texture}
<iframe
  src="interactive_textures/fig-julez_texture.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Texture discrimination using textons.
:::
```

### fig-analysis_heeger_bergen

```markdown
::{#fig-analysis_heeger_bergen}
<iframe
  src="interactive_textures/fig-analysis_heeger_bergen.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

A reference texture image is transformed into a representation using a texture analysis (encoder). Then the texture synthesis procedure takes as input  a random noise image of the size of the desired output texture and the parameters of the reference image $\theta$.
:::
```

### fig-heeger_bergen_iterations

```markdown
::{#fig-heeger_bergen_iterations}
<iframe
  src="interactive_textures/fig-heeger_bergen_iterations.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

The steps of the Heeger-Bergen texture synthesis algorithm. The process starts with white noise input image. Each step takes as input the previous output, and it is modified by a function $f_{\theta}$, where $\theta$ are the parameters describing a texture. At each step the output image $x_t$ gets closer to the appearance of the reference texture @fig-analysis_heeger_bergen
:::
```

### fig-heegersubbands

```markdown
::{#fig-heegersubbands}
<iframe
  src="interactive_textures/fig-heegersubbands.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

(a) Texture analysis (encoder) using a steerable pyramid with six orientations and three scales. The output representation is the concatenation of the 18 subband histograms, the low-pass residual histogram and the input image histogram. (b) Texture synthesis, only one iteration shown. At each iteration, the output is put back as input and the process is repeated $N$ times. The diagram corresponds to the implementation of the function $f_{\theta}$ from @fig-heeger_bergen_iterations
:::
```

### fig-heegersubbands_histmatch

```markdown
::{#fig-heegersubbands_histmatch}
<iframe
  src="interactive_textures/fig-heegersubbands_histmatch.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Histogram matching for one of the subbands. The same operation is done for all the subbands independently.
:::
```

### fig-two_examples

```markdown
::{#fig-two_examples}
<iframe
  src="interactive_textures/fig-two_examples.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Two examples of synthesized textures. Inputs have a size of 256 $\times$ 256 pixels, outputs are 512 $\times$ 512. In these examples, the algorithm runs for 15 iterations, using a pyramid of six orientation and four scales.
:::
```

### fig-sampling_efros_leung

```markdown
::{#fig-sampling_efros_leung}
<iframe
  src="interactive_textures/fig-sampling_efros_leung.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

In the Efros-Leung algorithm @Efros99
:::
```

### fig-efros1a

```markdown
::{#fig-efros1a}
<iframe
  src="interactive_textures/fig-efros1a.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fig-efros1b

```markdown
::{#fig-efros1b}
<iframe
  src="interactive_textures/fig-efros1b.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fig-efros1c

```markdown
::{#fig-efros1c}
<iframe
  src="interactive_textures/fig-efros1c.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fig-efros1d

```markdown
::{#fig-efros1d}
<iframe
  src="interactive_textures/fig-efros1d.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fig-efrosresult

```markdown
::{#fig-efrosresult}
<iframe
  src="interactive_textures/fig-efrosresult.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Image synthesis results from the Efros-Leung algorithm.  The small crops are used to synthesize the larger texture regions. Input images are 128 $\times$ 128 pixels, and the outputs are 256 $\times$ 256 pixels. The neighbourhood size is 17 $\times$ 17 pixels.
:::
```

