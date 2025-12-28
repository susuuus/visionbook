# Integration Snippets for neural_nets.qmd

Replace the original ![...](figures/...) with these iframe embeds:

### fig-neural_nets-fig1_net

```markdown
::{#fig-neural_nets-fig1_net}
<iframe
  src="interactive_neural_nets/fig-neural_nets-fig1_net.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

A neural network can be drawn as a directed graph.
:::
```

### fig-neural_nets-perceptron_fig2

```markdown
::{#fig-neural_nets-perceptron_fig2}
<iframe
  src="interactive_neural_nets/fig-neural_nets-perceptron_fig2.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

A simple model for a neuron is the perceptron.
:::
```

### fig-neural_nets-perceptron_as_classifier

```markdown
::{#fig-neural_nets-perceptron_as_classifier}
<iframe
  src="interactive_neural_nets/fig-neural_nets-perceptron_as_classifier.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Value of hidden unit ($z$) and output unit ($y$) in a perceptron, as a function of the input data.
:::
```

### fig-neural_nets-fitting_a_perceptron

```markdown
::{#fig-neural_nets-fitting_a_perceptron}
<iframe
  src="interactive_neural_nets/fig-neural_nets-fitting_a_perceptron.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Different possible decision surfaces of a perceptron.
:::
```

### fig-neural_nets-fan_out

```markdown
::{#fig-neural_nets-fan_out}
<iframe
  src="interactive_neural_nets/fig-neural_nets-fan_out.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Multiple outputs fan out from a neuron.
:::
```

### fig-neural_nets-MLP1

```markdown
::{#fig-neural_nets-MLP1}
<iframe
  src="interactive_neural_nets/fig-neural_nets-MLP1.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Mutilayer perceptron.
:::
```

### transformations.png

```markdown
::{#None}
<iframe
  src="interactive_neural_nets/fig_transformations.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

A multilayer network is a sequence of transformations $f_1, \ldots, f_L$ that produce a series of activations $\mathbf{x}_1, \ldots, \mathbf{x}_L$.
:::
```

### fig-neural_nets-params_vs_activations

```markdown
::{#fig-neural_nets-params_vs_activations}
<iframe
  src="interactive_neural_nets/fig-neural_nets-params_vs_activations.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Learning is a function that maps a dataset to parameters. Inference, through a neural net, is a function that maps a datapoint to activations.
:::
```

### fig-deep_nets

```markdown
::{#fig-deep_nets}
<iframe
  src="interactive_neural_nets/fig-deep_nets.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Deep nets consist of linear layers interleaved with nonlinearities.
:::
```

### fig-neural_nets-nonseparable_dataset

```markdown
::{#fig-neural_nets-nonseparable_dataset}
<iframe
  src="interactive_neural_nets/fig-neural_nets-nonseparable_dataset.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Dataset that is not linearly separable.
:::
```

### fig-neural_nets-simple_MLP_network

```markdown
::{#fig-neural_nets-simple_MLP_network}
<iframe
  src="interactive_neural_nets/fig-neural_nets-simple_MLP_network.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

A simple MLP network.
:::
```

### fig-neural_nets-simple_MLP_network_values

```markdown
::{#fig-neural_nets-simple_MLP_network_values}
<iframe
  src="interactive_neural_nets/fig-neural_nets-simple_MLP_network_values.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Values of hidden units and output unit for the MLP shown in \fig{\ref{fig-neural_nets-simple_MLP_network}}.
:::
```

### fig-neural_nets-curve_as_bump

```markdown
::{#fig-neural_nets-curve_as_bump}
<iframe
  src="interactive_neural_nets/fig-neural_nets-curve_as_bump.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Any function from $\mathbb{R} \rightarrow \mathbb{R}$ can be approximated arbitrarily well by a sum of elementary bumps.
:::
```

### fig-neural_nets-bump_as_relus

```markdown
::{#fig-neural_nets-bump_as_relus}
<iframe
  src="interactive_neural_nets/fig-neural_nets-bump_as_relus.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

A bump can be represented as a weighted sum of shifted and scaled relu functions.
:::
```

### fig-neural_nets-simple_MLP_network_tensors_and_batches

```markdown
::{#fig-neural_nets-simple_MLP_network_tensors_and_batches}
<iframe
  src="interactive_neural_nets/fig-neural_nets-simple_MLP_network_tensors_and_batches.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

The tensors that represent one pass through the MLP in @fig-neural_nets-simple_MLP_network
:::
```

### fig-neural_nets-3D_tensor_example

```markdown
::{#fig-neural_nets-3D_tensor_example}
<iframe
  src="interactive_neural_nets/fig-neural_nets-3D_tensor_example.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

A 3D tensor that could represent an $C \times H \times W$ color image.
:::
```

### fig-neural_nets-pointwise_nonlinearities

```markdown
::{#fig-neural_nets-pointwise_nonlinearities}
<iframe
  src="interactive_neural_nets/fig-neural_nets-pointwise_nonlinearities.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Common pointwise nonlinearities.
:::
```

### fig-neural_nets-batchnorm_vs_layernorm_diagram

```markdown
::{#fig-neural_nets-batchnorm_vs_layernorm_diagram}
<iframe
  src="interactive_neural_nets/fig-neural_nets-batchnorm_vs_layernorm_diagram.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Batchnorm vs layernorm. Gray indicates the region over which mean and variance are computed. See also Figure 2 of \cite{wu2018group} for more such visualizations.
:::
```

