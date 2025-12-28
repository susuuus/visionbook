# Integration Snippets for linear_image_filtering.qmd

Replace the original ![...](figures/...) with these iframe embeds:

### fig-contdiscsignal

```markdown
::{#fig-contdiscsignal}
<iframe
  src="interactive_linear_image_filtering/fig-contdiscsignal.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Fig (a) A continuous signal, and (b) a discrete signal obtained by sampling the continuous signal at the times $t=n$.
:::
```

### gray_image.png

```markdown
::{#None}
<iframe
  src="interactive_linear_image_filtering/fig_gray_image.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Grayscale image showing a person walking in the street. This tiny image has only $18\times18$ pixels.
:::
```

### fig-genericfilterH

```markdown
::{#fig-genericfilterH}
<iframe
  src="interactive_linear_image_filtering/fig-genericfilterH.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

System processing one signal.
:::
```

### fig-transformationsquizz

```markdown
::{#fig-transformationsquizz}
<iframe
  src="interactive_linear_image_filtering/fig-transformationsquizz.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

{Which one of these four image transformations (rotation by 30 degrees, scaling by 1/2, color to grayscale, and defocusing) can be written as linear functions? Answer: all of them!
:::
```

### fig-linear_filter

```markdown
::{#fig-linear_filter}
<iframe
  src="interactive_linear_image_filtering/fig-linear_filter.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

A linear function drawn as a **fully connected layer** in a neural network.
:::
```

### space_of_functions.png

```markdown
::{#None}
<iframe
  src="interactive_linear_image_filtering/fig_space_of_functions.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fig-translationInvar

```markdown
::{#fig-translationInvar}
<iframe
  src="interactive_linear_image_filtering/fig-translationInvar.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

A fundamental property of images is translation
  invariance--the same image may appear at arbitrary spatial positions
  within the image. *Source*: Fredo Durand.
:::
```

### fig-circle_2dconv

```markdown
::{#fig-circle_2dconv}
<iframe
  src="interactive_linear_image_filtering/fig-circle_2dconv.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Illustration of a 2D convolution of an input image with a kernel of size $3 \times 3$.For the pixels in the boundary we assumed that input image has zero values outside its boundary. The red and green boxes show the input pixels used to compute the corresponding output pixels.
:::
```

### fig-transformationsquizz2

```markdown
::{#fig-transformationsquizz2}
<iframe
  src="interactive_linear_image_filtering/fig-transformationsquizz2.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Fig (a) Defocusing an image can be written as a convolution. (b) Rotation can't be written as a convolution.
:::
```

### mn1.png

```markdown
::{#None}
<iframe
  src="interactive_linear_image_filtering/fig_mn1.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### mn2.png

```markdown
::{#None}
<iframe
  src="interactive_linear_image_filtering/fig_mn2.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### mn3.png

```markdown
::{#None}
<iframe
  src="interactive_linear_image_filtering/fig_mn3.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fig-convExamps

```markdown
::{#fig-convExamps}
<iframe
  src="interactive_linear_image_filtering/fig-convExamps.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Fig a) An impulse convolved with the input image gives no
 change.  (b) A shifted impulse shifts the image.  (c) Sum of two shifted copies of the image.  (d) Image defocusing by computing a local average over windows of $5 \times 5$ pixels. All the examples use zero padding for handling boundary conditions.
:::
```

### regions_convolution.png

```markdown
::{#None}
<iframe
  src="interactive_linear_image_filtering/fig_regions_convolution.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fig-boundaries

```markdown
::{#fig-boundaries}
<iframe
  src="interactive_linear_image_filtering/fig-boundaries.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Each row shows: (a) Different types of boundary extension. The last image shows the ground truth. (b) The output of convolving the image with a uniform kernel of size $11 \times 11$ with all the values equal to $1/121$. The output only shows the central region that corresponds to the input image without boundary extension. (c) The difference between each output and the ground truth output; see last column of (b). Note that the ground truth will not be available in practice.
:::
```

### circ_conv.png

```markdown
::{#None}
<iframe
  src="interactive_linear_image_filtering/fig_circ_conv.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### mn4.png

```markdown
::{#None}
<iframe
  src="interactive_linear_image_filtering/fig_mn4.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fig-corrvsconv

```markdown
::{#fig-corrvsconv}
<iframe
  src="interactive_linear_image_filtering/fig-corrvsconv.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Cross-correlation versus convolution. (a) Kernel. (b) and (e) are two input images. (c) and (f) are the output convolution with the kernel (a). (d) and (g) are the cross-correlation output with the kernel (a).
:::
```

### fig-normcorr

```markdown
::{#fig-normcorr}
<iframe
  src="interactive_linear_image_filtering/fig-normcorr.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Fig (a) Template. (b) Input image. (c) Correlation between input (b) and template (a). (d) Normalized correlation. e) Locations with cross-correlation above 75 percent of its maximum value.
:::
```

### fig-impulse_response_room_a

```markdown
::{#fig-impulse_response_room_a}
<iframe
  src="interactive_linear_image_filtering/fig-impulse_response_room_a.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

As shown in the sketch, sounds produced by one speaking person reach a listener via multiple paths. What the person hears is the superposition of all those signals. Figure modified from @TraerE7856.
:::
```

### fig-impulse_response_room_a2

```markdown
::{#fig-impulse_response_room_a2}
<iframe
  src="interactive_linear_image_filtering/fig-impulse_response_room_a2.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Fig (a) Apparatus used to measure the impulse response generated by a battery-powered speaker and a portable digital recorder. (b) Recorded acoustic impulse response of a room. Figure modified from @TraerE7856.
:::
```

### fig-impulse_response_room_b

```markdown
::{#fig-impulse_response_room_b}
<iframe
  src="interactive_linear_image_filtering/fig-impulse_response_room_b.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Modified from @TraerE7856.
:::
```

