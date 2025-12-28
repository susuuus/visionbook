# Integration Snippets for bias_and_shift.qmd

Replace the original ![...](figures/...) with these iframe embeds:

### fig-bias_and_shift-CIC_teaser

```markdown
::{#fig-bias_and_shift-CIC_teaser}
<iframe
  src="interactive_bias_and_shift/fig-bias_and_shift-CIC_teaser.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Each pair of images shows the grayscale input image and, to its right, the output of the automatic colorization system. Source: @zhang2016colorful
:::
```

### fig-bias_and_shift-colorizebot_examples

```markdown
::{#fig-bias_and_shift-colorizebot_examples}
<iframe
  src="interactive_bias_and_shift/fig-bias_and_shift-colorizebot_examples.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Two results of Reddit's ColorizeBot @colorizebot_blog. Original images are (left) Chopin, by Louis-Auguste Bisson, 1849, (right) and Benjamin the Thylacine, 1933. The bot ran the model from @zhang2016colorful on the original black and white photos.
:::
```

### fig-bias_and_shift-dogs_with_tongues

```markdown
::{#fig-bias_and_shift-dogs_with_tongues}
<iframe
  src="interactive_bias_and_shift/fig-bias_and_shift-dogs_with_tongues.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

(left) Colorization results, using a model trained on ImageNet (example made by Richard Zhang; input black and white photos from ImageNet @russakovsky2015imagenet. (right) Examples of dog images in ImageNet @russakovsky2015imagenet.
:::
```

### fig-bias_and_shift-regression_example

```markdown
::{#fig-bias_and_shift-regression_example}
<iframe
  src="interactive_bias_and_shift/fig-bias_and_shift-regression_example.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Generalization error can be arbitrarily bad when there is distribution shift between training and test.
:::
```

### fig-bias_and_shift-colorization_domain_gap

```markdown
::{#fig-bias_and_shift-colorization_domain_gap}
<iframe
  src="interactive_bias_and_shift/fig-bias_and_shift-colorization_domain_gap.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Domain gap between training data and test data in the ColorizeBot example.
:::
```

### fig-bias_and_shift-training_test_sets

```markdown
::{#fig-bias_and_shift-training_test_sets}
<iframe
  src="interactive_bias_and_shift/fig-bias_and_shift-training_test_sets.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Training and testing on different datasets. In this illustration, all datasets have 5 samples.
:::
```

### fig-bias_and_shift-test_as_function_of_data

```markdown
::{#fig-bias_and_shift-test_as_function_of_data}
<iframe
  src="interactive_bias_and_shift/fig-bias_and_shift-test_as_function_of_data.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Generalization error as a function of number of training examples. Test set is dataset A. Each curve shows the performance when training with dataset A and with dataset B (same distributions as in @fig-bias_and_shift-training_test_sets)
:::
```

### fig-bias_and_shift-datasetsJeopardy

```markdown
::{#fig-bias_and_shift-datasetsJeopardy}
<iframe
  src="interactive_bias_and_shift/fig-bias_and_shift-datasetsJeopardy.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Let's play the *Name That Dataset!* game. Modified from @Torralba2011. The game consists in associating each set of three images with the name of the dataset, from the list on the right, they belong to.
:::
```

### fig-bias_and_shift-palmer_1981enhanced

```markdown
::{#fig-bias_and_shift-palmer_1981enhanced}
<iframe
  src="interactive_bias_and_shift/fig-bias_and_shift-palmer_1981enhanced.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Cannonical viewpoints for 12 objects. Figure from @Palmer1981
:::
```

### fig-bias_and_shift-mugs

```markdown
::{#fig-bias_and_shift-mugs}
<iframe
  src="interactive_bias_and_shift/fig-bias_and_shift-mugs.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Pictures of mugs returned by a Google image search. There are many types of biases present in this small image collection.
:::
```

### fig-bias_and_shift-horses

```markdown
::{#fig-bias_and_shift-horses}
<iframe
  src="interactive_bias_and_shift/fig-bias_and_shift-horses.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Pictures of horses returned by a Google image search. There are many types of biases present in this small image collection.
:::
```

### fig-bias_and_shift-adversarial_perturbation

```markdown
::{#fig-bias_and_shift-adversarial_perturbation}
<iframe
  src="interactive_bias_and_shift/fig-bias_and_shift-adversarial_perturbation.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

An adversarial attack that adds subtle changes to the cat photo to make a neural net classify it instead as an ostrich. The noise image color values are scaled 20x for visualization.
:::
```

