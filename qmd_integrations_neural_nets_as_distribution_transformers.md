# Integration Snippets for neural_nets_as_distribution_transformers.qmd

Replace the original ![...](figures/...) with these iframe embeds:

### fig-neural_nets_as_distribution_transformers-trad_plot

```markdown
::{#fig-neural_nets_as_distribution_transformers-trad_plot}
<iframe
  src="interactive_neural_nets_as_distribution_transformers/fig-neural_nets_as_distribution_transformers-trad_plot.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

The traditional way of plotting the function $\mathbf{x}_{\text{out}} = \mathbf{x}_{\text{in}}$.
:::
```

### fig-neural_nets_as_distribution_transformers-new_way_plot

```markdown
::{#fig-neural_nets_as_distribution_transformers-new_way_plot}
<iframe
  src="interactive_neural_nets_as_distribution_transformers/fig-neural_nets_as_distribution_transformers-new_way_plot.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

An alternative way of plotting a function. Functions are mappings that rearrange the input space. The identity function $\mathbf{x}_{\text{out}}=\mathbf{x}_{\text{in}}$, shown here, means "no rearrangement," so the mapping is straight lines.
:::
```

### fig-neural_nets_as_distribution_transformers-new_way_plot_examples

```markdown
::{#fig-neural_nets_as_distribution_transformers-new_way_plot_examples}
<iframe
  src="interactive_neural_nets_as_distribution_transformers/fig-neural_nets_as_distribution_transformers-new_way_plot_examples.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Mapping plots for several simple functions that could be neural layers.
:::
```

### fig-neural_nets_as_data_transformations-new_way_plot_two_layer

```markdown
::{#fig-neural_nets_as_data_transformations-new_way_plot_two_layer}
<iframe
  src="interactive_neural_nets_as_distribution_transformers/fig-neural_nets_as_data_transformations-new_way_plot_two_layer.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Mapping plot for a `linear`-`relu` stack.
:::
```

### fig-neural_nets_as_data_transformations-2D_mapping_diagrams

```markdown
::{#fig-neural_nets_as_data_transformations-2D_mapping_diagrams}
<iframe
  src="interactive_neural_nets_as_distribution_transformers/fig-neural_nets_as_data_transformations-2D_mapping_diagrams.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

2D mapping diagrams for several neural layers. The `linear` layer mapping will shift, stretch, and rotate depending on its weights and biases.
:::
```

### fig-neural_nets-simple_MLP_network2

```markdown
::{#fig-neural_nets-simple_MLP_network2}
<iframe
  src="interactive_neural_nets_as_distribution_transformers/fig-neural_nets-simple_MLP_network2.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

An MLP with three linear layers and two outputs, suitable for performing binary softmax regression.
:::
```

### fig-neural_nets_as_data_transformations-goal_of_classifier

```markdown
::{#fig-neural_nets_as_data_transformations-goal_of_classifier}
<iframe
  src="interactive_neural_nets_as_distribution_transformers/fig-neural_nets_as_data_transformations-goal_of_classifier.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

The goal of a neural net classifier is to rearrange the input data distribution to match the target label distribution. (left) Input dataset with two classes in red and blue. (right) Target output (one-hot codes).
:::
```

### fig-neural_nets-nn_training_viz

```markdown
::{#fig-neural_nets-nn_training_viz}
<iframe
  src="interactive_neural_nets_as_distribution_transformers/fig-neural_nets-nn_training_viz.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

How a deep net remaps input data layer by layer. The target output is to move all the red points to $(0,1)$ and all the blue points to $(1,0)$ (one-hot codes for the two classes). As training progresses the network gradually achieves this separation.
:::
```

### fig-neural_nets-vit_mapping_plot

```markdown
::{#fig-neural_nets-vit_mapping_plot}
<iframe
  src="interactive_neural_nets_as_distribution_transformers/fig-neural_nets-vit_mapping_plot.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

How a powerful deep net remaps input images into a disentangled representation where semantic classes (shown in different colors) are separated. This deep net is a vision transformer (ViT~\cite{dosovitskiy2020vit}), which we will learn about in \sect{\ref{sec:transformers:ViT_arch}}. It was trained using contrastive language-image pre-training (CLIP~\cite{radford2021learning}, see \sect{\ref{sec:VLMs:CLIP}}). Each `ViT block` contains multiple layers of neural processing (see \fig{\ref{fig-transformers-ViT_arch}}; we visualize the embeddings right after the first `token norm` in a block). We apply t-SNE jointly across all shown layers.
:::
```

