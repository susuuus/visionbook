# Integration Snippets for gradient_descent.qmd

Replace the original ![...](figures/...) with these iframe embeds:

### fig-gradient_descent-optimization_schematic

```markdown
::{#fig-gradient_descent-optimization_schematic}
<iframe
  src="interactive_gradient_descent/fig-gradient_descent-optimization_schematic.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

General optimization loop.
:::
```

### alg1.png

```markdown
::{#None}
<iframe
  src="interactive_gradient_descent/fig_alg1.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Gradient descent `GD`. Optimizing a cost function $J: \theta \rightarrow \mathbb{R}$ by descending the gradient $\nabla_{\theta} J$.
:::
```

### alg2.png

```markdown
::{#None}
<iframe
  src="interactive_gradient_descent/fig_alg2.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Gradient descent with learning rate decay algorithm.
:::
```

### alg3.png

```markdown
::{#None}
<iframe
  src="interactive_gradient_descent/fig_alg3.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Gradient descent with momentum algorithm.
:::
```

### fig-gradient_descent-momentum_out1

```markdown
::{#fig-gradient_descent-momentum_out1}
<iframe
  src="interactive_gradient_descent/fig-gradient_descent-momentum_out1.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

(left) A simple loss function $J = \texttt{abs}(\theta)$. (right) Optimization trajectory for three different settings of momentum $\mu$. White line indicates value of the parameter at each iteration of optimization, starting at top and progressing to bottom. Color is value of the loss. Red dot is location where loss first reaches within $0.01$ of optimal value.
:::
```

### fig-gradient_descent-grad_descent_simple_examples

```markdown
::{#fig-gradient_descent-grad_descent_simple_examples}
<iframe
  src="interactive_gradient_descent/fig-gradient_descent-grad_descent_simple_examples.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

How gradient descent behaves on various functions.** In each subplot, the left shows the function $J$, with the red point representing the solution found by gradient descent (GD) with $\eta=0.01$ and $\mu=0.9$. The right shows the trajectory of $x$ values over iterations of GD, plotted on top of $J$ at each iteration. (a) As $\eta$ goes to zero, GD converges for convex functions. (b) Discontinuities pose no essential problem, as long as the gradient is defined on either side. (c) A nearly flat function will exhibit very slow descent. (d) Piecewise constant functions are problematic because the gradient completely vanishes. (e) For the function $J=\texttt{sqrt}(\texttt{abs}(\theta))-0.25$, the gradient goes to infinity at the minimizer, causing instability. (f) When $J$ has multiple local minima, we may not find the global minimum.
:::
```

### alg4.png

```markdown
::{#None}
<iframe
  src="interactive_gradient_descent/fig_alg4.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Evolution strategy algorithm.
:::
```

### fig-gradient_descent-sampling_out1

```markdown
::{#fig-gradient_descent-sampling_out1}
<iframe
  src="interactive_gradient_descent/fig-gradient_descent-sampling_out1.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Using @alg-gradient_descent_ES) to minimize a nondifferentiable (zero-gradient) loss, using $\sigma=1$, $M=10$, and $\eta=0.02$.
:::
```

### alg5.png

```markdown
::{#None}
<iframe
  src="interactive_gradient_descent/fig_alg5.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Gradient clipping algorithm.
:::
```

### fig-gradient_descent-clipped_out1

```markdown
::{#fig-gradient_descent-clipped_out1}
<iframe
  src="interactive_gradient_descent/fig-gradient_descent-clipped_out1.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Using `GD` with clipping to minimize a loss with exploding gradients, using $m=0.1$.
:::
```

### alg6.png

```markdown
::{#None}
<iframe
  src="interactive_gradient_descent/fig_alg6.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Stochastic gradient descent algorithm. Stochastic gradient descent estimates the gradient from a stochastic subset (batch) of the full training data, and makes an update on that basis.
:::
```

