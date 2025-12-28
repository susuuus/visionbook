# Integration Snippets for simplesystem_final_slides.qmd

Replace the original ![...](figures/...) with these iframe embeds:

### img1.jpg

```markdown
::{#None}
<iframe
  src="interactive_simplesystem_final_slides/fig_img1.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Image from the simple world.
:::
```

### examples_training_midas.jpg

```markdown
::{#None}
<iframe
  src="interactive_simplesystem_final_slides/fig_examples_training_midas.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Images and depth maps from the training set. *Source*: Image from @Ranftl2022
:::
```

### projection-revisted.png

```markdown
::{#None}
<iframe
  src="interactive_simplesystem_final_slides/fig_projection-revisted.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Camera projection model
:::
```

### views_midas.jpg

```markdown
::{#None}
<iframe
  src="interactive_simplesystem_final_slides/fig_views_midas.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

3D reconstruction using a pretrained model. Multiple viewpoints of the reconstructed 3D scene
:::
```

### views.png

```markdown
::{#None}
<iframe
  src="interactive_simplesystem_final_slides/fig_views.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

3D reconstruction using the simple visual system from earlier chapter
:::
```

### comparison_midas_simpleworld.jpg

```markdown
::{#None}
<iframe
  src="interactive_simplesystem_final_slides/fig_comparison_midas_simpleworld.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Comparison: Pretrained model (MiDaS) vs simple world model. The pretrained model works across all examples, while the hand-crafted approach only works for the first and breaks down for others.
:::
```

### chatgpt_blockworld.png

```markdown
::{#None}
<iframe
  src="interactive_simplesystem_final_slides/fig_chatgpt_blockworld.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

(a) Input image and text prompt to ChatGPT. (b) Output by ChatGPT (GPT-4V, version from Nov 21, 2023) when asked to describe the image from the simple world.
:::
```

### chatgpt_blockworld_2.png

```markdown
::{#None}
<iframe
  src="interactive_simplesystem_final_slides/fig_chatgpt_blockworld_2.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Output by ChatGPT when asked to render a new image with the same elements. The reconstruction is close but not quite right.
:::
```

### gibson_bird.png

```markdown
::{#None}
<iframe
  src="interactive_simplesystem_final_slides/fig_gibson_bird.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Gibson's bird
:::
```

