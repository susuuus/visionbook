# Integration Snippets for graphical_models.qmd

Replace the original ![...](figures/...) with these iframe embeds:

### x1.png

```markdown
::{#None}
<iframe
  src="interactive_graphical_models/fig_x1.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

A graphical model with only one node.
:::
```

### x1x2.png

```markdown
::{#None}
<iframe
  src="interactive_graphical_models/fig_x1x2.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Two independent variables.
:::
```

### x1bx2.png

```markdown
::{#None}
<iframe
  src="interactive_graphical_models/fig_x1bx2.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Two dependent variables.
:::
```

### fig-3node

```markdown
::{#fig-3node}
<iframe
  src="interactive_graphical_models/fig-3node.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Three dependent variables.
:::
```

### 3node.png

```markdown
::{#None}
<iframe
  src="interactive_graphical_models/fig_3node.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Conditioning on the variable $x_2$ is indicated by the filled circle.
:::
```

### fig-chain

```markdown
::{#fig-chain}
<iframe
  src="interactive_graphical_models/fig-chain.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

A clique is any set of nodes where each node is connected to
every other node in the same clique.
:::
```

### cliques2.png

```markdown
::{#None}
<iframe
  src="interactive_graphical_models/fig_cliques2.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

A maximal clique is the largest possible clique.
:::
```

### x1x2x3y1y2y3.png

```markdown
::{#None}
<iframe
  src="interactive_graphical_models/fig_x1x2x3y1y2y3.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Markov chain  with three observed variables, shaded, and three unobserved variables.
:::
```

### fig-leafs

```markdown
::{#fig-leafs}
<iframe
  src="interactive_graphical_models/fig-leafs.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Two-dimensional Markov random field.
:::
```

### fig-leafs-a

```markdown
::{#fig-leafs-a}
<iframe
  src="interactive_graphical_models/fig-leafs-a.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fig-leafs-b

```markdown
::{#fig-leafs-b}
<iframe
  src="interactive_graphical_models/fig-leafs-b.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### directed.png

```markdown
::{#None}
<iframe
  src="interactive_graphical_models/fig_directed.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

A directed graphical model with three variables.
:::
```

### fig-chain2

```markdown
::{#fig-chain2}
<iframe
  src="interactive_graphical_models/fig-chain2.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Same three-node Markov chain of @fig-chain.
:::
```

### fig-3bpc

```markdown
::{#fig-3bpc}
<iframe
  src="interactive_graphical_models/fig-3bpc.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Summary of the messages (partial sums) for a simple belief propagation example.
:::
```

### fig-bpmotivator2

```markdown
::{#fig-bpmotivator2}
<iframe
  src="interactive_graphical_models/fig-bpmotivator2.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Example motivating belief propagation update rule. (a) Marginalization of a graph with no loops.  (b) Shows how the partial sums at $x_j$ distribute over nodes.
:::
```

### fig-bpdiscrete

```markdown
::{#fig-bpdiscrete}
<iframe
  src="interactive_graphical_models/fig-bpdiscrete.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Pictorial depiction of belief propagation message passing rules of equation (@eq-bpupdate), where $\odot$ indicates elementwise multiplication (i.e., the Hadamard product).
:::
```

### fig-bpi

```markdown
::{#fig-bpi}
<iframe
  src="interactive_graphical_models/fig-bpi.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

To compute the marginal probability at node $i$, we multiply together all the incoming messages at that node: $p_{i}$ as another message.
:::
```

### fig-canoe1-a

```markdown
::{#fig-canoe1-a}
<iframe
  src="interactive_graphical_models/fig-canoe1-a.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fig-canoe1-b

```markdown
::{#fig-canoe1-b}
<iframe
  src="interactive_graphical_models/fig-canoe1-b.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fig-canoe1-c

```markdown
::{#fig-canoe1-c}
<iframe
  src="interactive_graphical_models/fig-canoe1-c.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fig-canoe1-d

```markdown
::{#fig-canoe1-d}
<iframe
  src="interactive_graphical_models/fig-canoe1-d.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fig-canoe3

```markdown
::{#fig-canoe3}
<iframe
  src="interactive_graphical_models/fig-canoe3.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Graphical model for the posterior probability for stereo disparity offset between the left and right camera views from a stereo rig.
:::
```

### fig-canoe4

```markdown
::{#fig-canoe4}
<iframe
  src="interactive_graphical_models/fig-canoe4.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Belief propagation applied to graphical model, @fig-canoe3, for the stereo problem. (a) Right and (b) left camera views. The black line shows the analyzed row. (c) Local evidence for each depth disparity at left camera. (d) Final rightward and (e) leftward belief propagation messages at each position. (f) Final marginalized posterior probability at each left camera pixel accurately finds the depth discontinuity.
:::
```

### fig-numerical

```markdown
::{#fig-numerical}
<iframe
  src="interactive_graphical_models/fig-numerical.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Undirected graphical model used in belief propagation example.
:::
```

