# Integration Snippets for transformers.qmd

Replace the original ![...](figures/...) with these iframe embeds:

### fig-transformers-CNN_limitations

```markdown
::{#fig-transformers-CNN_limitations}
<iframe
  src="interactive_transformers/fig-transformers-CNN_limitations.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Consider a 2-layer CNN with kernel size 3, tasked to compare $x_1$ and $x_7$. It can't do it: there are no neurons that are connected to both $x_1$ and $x_7$. Hatch marks indicate which neurons are connected to $x_1$ and $x_7$ respectively.
:::
```

### fig-transformers-tokenization

```markdown
::{#fig-transformers-tokenization}
<iframe
  src="interactive_transformers/fig-transformers-tokenization.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Tokenization: converting an image to a set of vectors. $\mathbf{W}_{\texttt{tokenize}}$ is a learnable linear projection from the dimensionality of the vectorized crops to $d$ dimensions. This is just one of many possible ways to tokenize an image.
:::
```

### fig-transformers-T_notation

```markdown
::{#fig-transformers-T_notation}
<iframe
  src="interactive_transformers/fig-transformers-T_notation.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

In this chapter, we will represent a set of tokens as a matrix whose rows are the token vectors.
:::
```

### fig-transformers-lin_bomb_neurons_vs_tokens

```markdown
::{#fig-transformers-lin_bomb_neurons_vs_tokens}
<iframe
  src="interactive_transformers/fig-transformers-lin_bomb_neurons_vs_tokens.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Linear combination of neurons versus tokens.
:::
```

### fig-transformers-neural_nets_vs_token_nets

```markdown
::{#fig-transformers-neural_nets_vs_token_nets}
<iframe
  src="interactive_transformers/fig-transformers-neural_nets_vs_token_nets.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Neural nets versus token nets. The arrows here represent any functional dependency between the nodes (note that different arrows represent different types of functions).
:::
```

### fig-transformers-fc_vs_attn

```markdown
::{#fig-transformers-fc_vs_attn}
<iframe
  src="interactive_transformers/fig-transformers-fc_vs_attn.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Fully-connected layers versus attention layers.
:::
```

### fig-transformers-attention_layer_safari_query_cartoon

```markdown
::{#fig-transformers-attention_layer_safari_query_cartoon}
<iframe
  src="interactive_transformers/fig-transformers-attention_layer_safari_query_cartoon.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

How attention can be allocated across different regions (tokens) in an image. The token code vectors consist of multiple dimensions and each can encode a different attribute of the token. To the left we show a dimension that encodes number of animal heads. To the right we show a different dimension that encodes color (or this could be three dimensions, coding RGB). The output token is a weighted sum over all the tokens attended to.
:::
```

### fig-transformers-color_scheme.png

```markdown
::{#None}
<iframe
  src="interactive_transformers/fig_fig-transformers-color_scheme.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fig-transformers-attn_arch1

```markdown
::{#fig-transformers-attn_arch1}
<iframe
  src="interactive_transformers/fig-transformers-attn_arch1.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Mechanics of an attention layer. Queries from the question match keys from the tokens representing the impala; value vectors of the impala tokens then contribute the most to the sum that yields $\mathbf{t}_{\texttt{out}}$'s code vector. (Softmax omitted in this example.)
:::
```

### fig-transformers-self_attn_layer

```markdown
::{#fig-transformers-self_attn_layer}
<iframe
  src="interactive_transformers/fig-transformers-self_attn_layer.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

A self-attention layer.
:::
```

### fig-transformers-attn_arch

```markdown
::{#fig-transformers-attn_arch}
<iframe
  src="interactive_transformers/fig-transformers-attn_arch.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Self-attention layer expanded. The nodes with the dashed outline correspond to each other; they represent one query being matched against one key to result in a scalar similarity value, in the gray box, which acts as a weight in the weighted sum computed by $\mathbf{A}$.
:::
```

### fig-attention_layer_cartoon

```markdown
::{#fig-attention_layer_cartoon}
<iframe
  src="interactive_transformers/fig-attention_layer_cartoon.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

One way self-attention could be used to aggregate information across all patches containing the same object, and thereby arrive at a better representation of the object in $\mathbf{t}_2$, the query patch.
:::
```

### fig-transformers-transformers_attn_ex

```markdown
::{#fig-transformers-transformers_attn_ex}
<iframe
  src="interactive_transformers/fig-transformers-transformers_attn_ex.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Example of self-attention maps where each token is an image patch and the query and key vectors are both set to the mean color of the patch, normalized to be a unit vector.
:::
```

### fig-transformers-transformer_vs_MLP

```markdown
::{#fig-transformers-transformer_vs_MLP}
<iframe
  src="interactive_transformers/fig-transformers-transformer_vs_MLP.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

The basic transformer architecture versus an MLP.
:::
```

### fig-transformers-ViT_arch

```markdown
::{#fig-transformers-ViT_arch}
<iframe
  src="interactive_transformers/fig-transformers-ViT_arch.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

The ViT transformer architecture~\cite{dosovitskiy2020vit}. This set of layers forms a computational block, shaded in gray, that can be repeated $L$ times for a depth $L$ ViT. To clarify where the parameters live in this architecture, we have colored all the edges with learnable parameters in blue (note that the MSA merge, \eqn{\ref{eqn:transformers:MSA_merge}}, is also learnable but not explicitly shown in this diagram).
:::
```

### fig-transformers-permutation_equivariance

```markdown
::{#fig-transformers-permutation_equivariance}
<iframe
  src="interactive_transformers/fig-transformers-permutation_equivariance.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Transformers are permutation equivariant. For notational simplicity, we omit layer indices on the token variables here.
:::
```

### fig-transformers-conv_matmul_equivalence

```markdown
::{#fig-transformers-conv_matmul_equivalence}
<iframe
  src="interactive_transformers/fig-transformers-conv_matmul_equivalence.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

The query, key, and value projections in transformers can be written either as a convolution or a matrix multiply.
:::
```

### fig-transformers-masked_prediction1

```markdown
::{#fig-transformers-masked_prediction1}
<iframe
  src="interactive_transformers/fig-transformers-masked_prediction1.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Masked prediction of time index 4 from time indices 1-3.
:::
```

### fig-transformers-masked_attn_one_matmul

```markdown
::{#fig-transformers-masked_attn_one_matmul}
<iframe
  src="interactive_transformers/fig-transformers-masked_attn_one_matmul.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Masked attention to make multiple causal predictions at once. Black cells are masked; they are filled with zeros.
:::
```

### fig-transformers-multilayer_masked_attention

```markdown
::{#fig-transformers-multilayer_masked_attention}
<iframe
  src="interactive_transformers/fig-transformers-multilayer_masked_attention.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Multilayer masked attention achieves causal prediction with a deep net.
:::
```

### fig-transformers-positional_codes

```markdown
::{#fig-transformers-positional_codes}
<iframe
  src="interactive_transformers/fig-transformers-positional_codes.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Positional codes.
:::
```

### fig-transformers-affine_layer_comparison

```markdown
::{#fig-transformers-affine_layer_comparison}
<iframe
  src="interactive_transformers/fig-transformers-affine_layer_comparison.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

