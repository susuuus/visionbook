# Integration Snippets for fairness.qmd

Replace the original ![...](figures/...) with these iframe embeds:

### fig-soap

```markdown
::{#fig-soap}
<iframe
  src="interactive_fairness/fig-soap.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Images of household items, and their recognized classes by five object recognition systems @DeVries2019. The systems tend to perform worse for non-Western countries and for lower-income households, such as those of the right two photographs.
:::
```

### fig-augmentation

```markdown
::{#fig-augmentation}
<iframe
  src="interactive_fairness/fig-augmentation.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

In this example “wears hat” is deemed to be a protected
attribute, but it is correlated with another attribute, which in this
example is “wears glasses” @Ramaswamy2021. The GAN-based method generates sets of
images where wearing hats is not correlated with wearing
glasses.
:::
```

### fig-transect

```markdown
::{#fig-transect}
<iframe
  src="interactive_fairness/fig-transect.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

A GAN creates sequences of faces, called **transects**, where only one attribute changes @Balakrishnan2020
:::
```

