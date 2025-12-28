# Integration Snippets for image_processing_fourier.qmd

Replace the original ![...](figures/...) with these iframe embeds:

### fig-FourierSeries6

```markdown
::{#fig-FourierSeries6}
<iframe
  src="interactive_image_processing_fourier/fig-FourierSeries6.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Reconstruction of a ramp with the first five sine functions.
:::
```

### fig-FourierSeries5_representation

```markdown
::{#fig-FourierSeries5_representation}
<iframe
  src="interactive_image_processing_fourier/fig-FourierSeries5_representation.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Two representations for the ramp function. (left) Time domain. (right) Fourier domain with coefficients of the sine series.
:::
```

### amplitudeandperiod.png

```markdown
::{#None}
<iframe
  src="interactive_image_processing_fourier/fig_amplitudeandperiod.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fig-disc2Dsignal

```markdown
::{#fig-disc2Dsignal}
<iframe
  src="interactive_image_processing_fourier/fig-disc2Dsignal.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

2D sine waves with $N=M=20$. The frequency values are (a) $u=2, v=0$; (b) $u=3, v=1$; (c) $u=7,v=-5$.
:::
```

### fig-complexexponential

```markdown
::{#fig-complexexponential}
<iframe
  src="interactive_image_processing_fourier/fig-complexexponential.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Complex exponential wave with (a) $N=40$, $k=1$, $A=1$; and (b) $N=40$, $k=3$, $A=1$. The red and green curves show the real and imaginary waves. The black line is the complex exponential. The dots correspond to the discrete samples.
:::
```

### fig-colorDFT

```markdown
::{#fig-colorDFT}
<iframe
  src="interactive_image_processing_fourier/fig-colorDFT.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Visualization of the discrete Fourier transform as a matrix.  The signal to be
 transformed forms the entries of the column vector at right.  The
 complex values of the Fourier transform matrix are indicated by the color,
 with the key in the bottom left.  In the vector at the right, black
 values indicate zero.
:::
```

### fig-DFT_a

```markdown
::{#fig-DFT_a}
<iframe
  src="interactive_image_processing_fourier/fig-DFT_a.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

DFT of an image and visualization of (top) the real and imaginary components, and (bottom) the amplitude and phase  of the Fourier transform.
:::
```

### fig-DFT_b

```markdown
::{#fig-DFT_b}
<iframe
  src="interactive_image_processing_fourier/fig-DFT_b.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Reconstructing an image from the $N$ Fourier coefficients of the largest amplitude.  The right frame shows the location, in the Fourier domain, of the $N$ Fourier coefficients, which when inverted, give the image at the left.
:::
```

### fig-2ddftexampleswaves

```markdown
::{#fig-2ddftexampleswaves}
<iframe
  src="interactive_image_processing_fourier/fig-2ddftexampleswaves.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Some 2D Fourier transform pairs. Images are $64 \times 64$ pixels. The waves are cosine with frequencies $(1,2)$, $(5,0)$, $(10,7)$, $(11,-15)$. The last two examples show the sum of two waves and the product.
:::
```

### fig-2ddftexamples

```markdown
::{#fig-2ddftexamples}
<iframe
  src="interactive_image_processing_fourier/fig-2ddftexamples.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Some two-dimensional Fourier transform pairs.
  Note the trends visible in the collection of transform pairs:  As
  the support of the image in one domain gets larger, the magnitude in
  the other domain becomes more localized.  A line transforms to a
  line oriented perpendicularly to the first. Images are $64 \times 64$ pixels, origin is in the center.
:::
```

### box_fun.png

```markdown
::{#None}
<iframe
  src="interactive_image_processing_fourier/fig_box_fun.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Box function for $L=5$ and $N=32$.
:::
```

### fig-boxfilterdft

```markdown
::{#fig-boxfilterdft}
<iframe
  src="interactive_image_processing_fourier/fig-boxfilterdft.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

DFT of the box filter with $L=5$, and $N=32$.
:::
```

### facade1.jpg

```markdown
::{#None}
<iframe
  src="interactive_image_processing_fourier/fig_facade1.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### facade1aprox.jpg

```markdown
::{#None}
<iframe
  src="interactive_image_processing_fourier/fig_facade1aprox.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fig-shiftFT

```markdown
::{#fig-shiftFT}
<iframe
  src="interactive_image_processing_fourier/fig-shiftFT.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Translation in space. Image (c) corresponds to image (a) after a translation of 16 pixels to the right and four pixels down. Images (b) and (d) show the real parts of their corresponding DFTs (with $N=128$). Image (f) shows the real part of the ratio between the two DFTs, and (e) is the inverse transform of the ratio between DFTs. The inverse is very close to an impulse located at the coordinates of the displacement vector between the two images.
:::
```

### fig-modulation

```markdown
::{#fig-modulation}
<iframe
  src="interactive_image_processing_fourier/fig-modulation.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Modulation in space. Multiplying an image by a cosine wave results in a new image with a Fourier transform with two copies of the Fourier transform of the original image. Only the magnitude of the Fourier transforms are shown.
:::
```

### fig-phaseoramp

```markdown
::{#fig-phaseoramp}
<iframe
  src="interactive_image_processing_fourier/fig-phaseoramp.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Swapping the amplitude and the phase of the Fourier Transform of two images. Each color channel is processed in the same way.
:::
```

### fig-phasevsamp

```markdown
::{#fig-phasevsamp}
<iframe
  src="interactive_image_processing_fourier/fig-phasevsamp.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

The relative importance of phase and amplitude depends on the image. Each row shows one image, its Fourier transform (amplitude and phase), and the resulting images obtained by applying the inverse Fourier transform to a signal with the original amplitude and randomized phase, and a signal with the original phase and a generic fixed $1/f$ amplitude. Note that for the first image, the phase seems to be the most important component. 
%However, as we move down, the relative importance between the two components changes. And for the bottom image (showing a pseudo-periodic threat texture) the amplitude is the most important component.
:::
```

### fig-quiz

```markdown
::{#fig-quiz}
<iframe
  src="interactive_image_processing_fourier/fig-quiz.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

The Fourier transform matching game: Match each image (a-h) with its corresponding Fourier transform magnitude (1-8).
:::
```

### con1.png

```markdown
::{#None}
<iframe
  src="interactive_image_processing_fourier/fig_con1.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Convolutional linear filter.
:::
```

### con2.png

```markdown
::{#None}
<iframe
  src="interactive_image_processing_fourier/fig_con2.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Transfer function of a linear filter.
:::
```

### fig-typestypes

```markdown
::{#fig-typestypes}
<iframe
  src="interactive_image_processing_fourier/fig-typestypes.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Sketch of the frequency responses of low-pass, band-pass, and high-pass filters.
:::
```

### fig-sketchresponses-a

```markdown
::{#fig-sketchresponses-a}
<iframe
  src="interactive_image_processing_fourier/fig-sketchresponses-a.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fig-sketchresponses-b

```markdown
::{#fig-sketchresponses-b}
<iframe
  src="interactive_image_processing_fourier/fig-sketchresponses-b.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fig-sketchresponses-c

```markdown
::{#fig-sketchresponses-c}
<iframe
  src="interactive_image_processing_fourier/fig-sketchresponses-c.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fig-filteringFT

```markdown
::{#fig-filteringFT}
<iframe
  src="interactive_image_processing_fourier/fig-filteringFT.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Simple filtering in the Fourier domain.  (a) The repeated columns of the
  building of the MIT dome generate harmonics along a horizontal line
  in the Fourier domain shown in (b). By zeroing out those Fourier
  components, as done in (d), the columns of the building are substantially removed (c). We can also the complementary operation keeping only those harmonics, shown in (f), which results in keeping only the columns (e).
:::
```

### experimental_setup.jpg

```markdown
::{#None}
<iframe
  src="interactive_image_processing_fourier/fig_experimental_setup.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### H.png

```markdown
::{#None}
<iframe
  src="interactive_image_processing_fourier/fig_H.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Output to an exponential wave.
:::
```

### fig-csfchart

```markdown
::{#fig-csfchart}
<iframe
  src="interactive_image_processing_fourier/fig-csfchart.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Contrast sensitivity function shown by the Campbell and Robson chart. The image shows a sine wave of increasing frequency from left to right, and increasing amplitude from top to bottom. Can you trace a curve over the chart to indicate where the sine wave becomes invisible?
:::
```

### my_CST.png

```markdown
::{#None}
<iframe
  src="interactive_image_processing_fourier/fig_my_CST.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

