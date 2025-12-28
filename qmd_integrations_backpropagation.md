# Integration Snippets for backpropagation.qmd

Replace the original ![...](figures/...) with these iframe embeds:

### fig-backpropagation-simple_MLP

```markdown
::{#fig-backpropagation-simple_MLP}
<iframe
  src="interactive_backpropagation/fig-backpropagation-simple_MLP.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

In this chapter we will visualize neural nets as a sequence of layers, which we call a computation graph.
:::
```

### fig-backpropagation-mod_block_forward

```markdown
::{#fig-backpropagation-mod_block_forward}
<iframe
  src="interactive_backpropagation/fig-backpropagation-mod_block_forward.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Forward operation of a neural net layer.
:::
```

### fig-backpropagation-composed_modules

```markdown
::{#fig-backpropagation-composed_modules}
<iframe
  src="interactive_backpropagation/fig-backpropagation-composed_modules.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Basic sequential computation graph.
:::
```

### fig-backpropagation-cgraph_tree

```markdown
::{#fig-backpropagation-cgraph_tree}
<iframe
  src="interactive_backpropagation/fig-backpropagation-cgraph_tree.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Computation graph as a tree.
:::
```

### fig-backpropagation-generic_layer_g_L

```markdown
::{#fig-backpropagation-generic_layer_g_L}
<iframe
  src="interactive_backpropagation/fig-backpropagation-generic_layer_g_L.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

A generic layer in the computation graph. The braces represent the part of the computation graph we need to consider in order to evaluate $\mathbf{g}_{\texttt{out}}$, $\mathbf{L}$, and $\mathbf{g}in$.
:::
```

### fig-backpropagation-mod_block_backward

```markdown
::{#fig-backpropagation-mod_block_backward}
<iframe
  src="interactive_backpropagation/fig-backpropagation-mod_block_backward.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

`backward` for a generic layer. We use the color 
<span style="display: inline-block; background-color: rgb(247, 224, 89); height: 10px; width: 20px; position: relative; top: 1mm;"></span> 
to indicate parameter gradients.
:::
```

### fig-backpropagation-forward_pass

```markdown
::{#fig-backpropagation-forward_pass}
<iframe
  src="interactive_backpropagation/fig-backpropagation-forward_pass.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Forward pass.
:::
```

### fig-backpropagation-backward_pass

```markdown
::{#fig-backpropagation-backward_pass}
<iframe
  src="interactive_backpropagation/fig-backpropagation-backward_pass.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### backprop_for_chains.png

```markdown
::{#None}
<iframe
  src="interactive_backpropagation/fig_backprop_for_chains.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Backpropagation (for chain computation graphs). A simple version of the backpropagation algorithm. This will work for the computation graphs we have seen so far, which consist of a series of layers, $f_1 \circ \ldots \circ f_L$, with no merging or branching (see @sec-backpropagation-branch_and_merge for how to handle more complicated graphs with merge and branch operations).
:::
```

### fig-backpropagation-linear_forward_backward_matrices

```markdown
::{#fig-backpropagation-linear_forward_backward_matrices}
<iframe
  src="interactive_backpropagation/fig-backpropagation-linear_forward_backward_matrices.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

The forward and backward matrix multiples for a linear layer.
:::
```

### fig-backpropagation-parameter_grad_linear_matrices

```markdown
::{#fig-backpropagation-parameter_grad_linear_matrices}
<iframe
  src="interactive_backpropagation/fig-backpropagation-parameter_grad_linear_matrices.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Matrix multiply for parameter gradient of a linear layer.
:::
```

### fig-backpropagation-linear_layer_backprop

```markdown
::{#fig-backpropagation-linear_layer_backprop}
<iframe
  src="interactive_backpropagation/fig-backpropagation-linear_layer_backprop.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Linear layer forward and backward.
:::
```

### fig-backpropagation-pointwise_backward_matices

```markdown
::{#fig-backpropagation-pointwise_backward_matices}
<iframe
  src="interactive_backpropagation/fig-backpropagation-pointwise_backward_matices.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Matrix multiply for \texttt{backward} of a pointwise layer.
:::
```

### fig-backpropagation-pointwise_layer_backprop

```markdown
::{#fig-backpropagation-pointwise_layer_backprop}
<iframe
  src="interactive_backpropagation/fig-backpropagation-pointwise_layer_backprop.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Matrix multiply for \texttt{backward} of a pointwise layer.
:::
```

### fig-backpropagation-L2_loss_layer_backprop

```markdown
::{#fig-backpropagation-L2_loss_layer_backprop}
<iframe
  src="interactive_backpropagation/fig-backpropagation-L2_loss_layer_backprop.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Matrix multiply for `backward` of an $L_2$ loss layer.
:::
```

### fig-backpropagation-forward_pass_MLP

```markdown
::{#fig-backpropagation-forward_pass_MLP}
<iframe
  src="interactive_backpropagation/fig-backpropagation-forward_pass_MLP.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Forward pass through an MLP.
:::
```

### fig-backpropagation-backward_pass_MLP

```markdown
::{#fig-backpropagation-backward_pass_MLP}
<iframe
  src="interactive_backpropagation/fig-backpropagation-backward_pass_MLP.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Backward pass through an MLP.
:::
```

### fig-backpropagation-backprop_as_neural_net

```markdown
::{#fig-backpropagation-backprop_as_neural_net}
<iframe
  src="interactive_backpropagation/fig-backpropagation-backprop_as_neural_net.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

The computation graph for backpropagation through a three-layer MLP. It's just another neural net! Solid lines are involved in computing data/activation gradients and dotted lines are involved in computing parameter gradients.
:::
```

### fig-backpropagation-branch_and_merge

```markdown
::{#fig-backpropagation-branch_and_merge}
<iframe
  src="interactive_backpropagation/fig-backpropagation-branch_and_merge.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

The `merge` and `branch` layers.
:::
```

### fig-backpropagation-branch_and_merge_layers_backprop_diagram

```markdown
::{#fig-backpropagation-branch_and_merge_layers_backprop_diagram}
<iframe
  src="interactive_backpropagation/fig-backpropagation-branch_and_merge_layers_backprop_diagram.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Merge and branch layers `forward` and `backward`.
:::
```

### fig-backpropagation-backprop_DAG

```markdown
::{#fig-backpropagation-backprop_DAG}
<iframe
  src="interactive_backpropagation/fig-backpropagation-backprop_DAG.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

An example of a DAG computation graph that we can construct, and do backpropagation through, with the tools defined previously.
:::
```

### fig-backpropagation-parameter_sharing

```markdown
::{#fig-backpropagation-parameter_sharing}
<iframe
  src="interactive_backpropagation/fig-backpropagation-parameter_sharing.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Parameter sharing is equivalent to branching a parameter in the computation graph.
:::
```

### fig-backpropagation-J_forward_backward_blocks

```markdown
::{#fig-backpropagation-J_forward_backward_blocks}
<iframe
  src="interactive_backpropagation/fig-backpropagation-J_forward_backward_blocks.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Full forward and backward passes for a learning problem $\min J(\mathbf{x}_0,\mathbf{y},\theta)$, collapsed into a single computation block.
:::
```

### fig-backpropagation-backprop_to_the_data_example

```markdown
::{#fig-backpropagation-backprop_to_the_data_example}
<iframe
  src="interactive_backpropagation/fig-backpropagation-backprop_to_the_data_example.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Visualizing the optimal image of a cat according to a particular neural net. The net we used is called Contrastive Language-Image Pre-Training (CLIP) @radford2021learning and here we found the image that maximizes a node in CLIP's computation graph that measures how much the image matches the text ``a photo of a cat.'' In @sec-VLMs-CLIP we will cover exactly how the CLIP model works in more detail.
:::
```

