# Integration Snippets for transfer_learning.qmd

Replace the original ![...](figures/...) with these iframe embeds:

### fig-transfer_learning-finetuning_basic

```markdown
::{#fig-transfer_learning-finetuning_basic}
<iframe
  src="interactive_transfer_learning/fig-transfer_learning-finetuning_basic.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Transfer learning consists of two phases: first we pretrain a model on one task and then we adapt that model to perform a new task.
:::
```

### fig-transfer_learning-finetuning.png

```markdown
::{#None}
<iframe
  src="interactive_transfer_learning/fig_fig-transfer_learning-finetuning.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Finetuning. Using gradient descent to train one model and then finetuning to produce a second model.
:::
```

### fig-transfer_learning-finetuning_stages

```markdown
::{#fig-transfer_learning-finetuning_stages}
<iframe
  src="interactive_transfer_learning/fig-transfer_learning-finetuning_stages.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### lock.png

```markdown
::{#None}
<iframe
  src="interactive_transfer_learning/fig_lock.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fire.png

```markdown
::{#None}
<iframe
  src="interactive_transfer_learning/fig_fire.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fig-transfer_learning-finetuning_certain_modules_example

```markdown
::{#fig-transfer_learning-finetuning_certain_modules_example}
<iframe
  src="interactive_transfer_learning/fig-transfer_learning-finetuning_certain_modules_example.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Finetuning certain subsets of a computation graph. Here we show some modules that have been pretrained (those with a shaded background) and one that is trained from scratch at finetuning time.
:::
```

### fig-transfer_learning-learning_from_examples.png

```markdown
::{#None}
<iframe
  src="interactive_transfer_learning/fig_fig-transfer_learning-learning_from_examples.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fig-transfer_learning-learning_from_teacher.png

```markdown
::{#None}
<iframe
  src="interactive_transfer_learning/fig_fig-transfer_learning-learning_from_teacher.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fig-transfer_learning-knowledge_distillation.png

```markdown
::{#None}
<iframe
  src="interactive_transfer_learning/fig_fig-transfer_learning-knowledge_distillation.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>


:::
```

### fig-transfer_learning-KD_diagram

```markdown
::{#fig-transfer_learning-KD_diagram}
<iframe
  src="interactive_transfer_learning/fig-transfer_learning-KD_diagram.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Comparing knowledge distillation to supervised learning from labels.
:::
```

### fig-transfer_learning-prompting

```markdown
::{#fig-transfer_learning-prompting}
<iframe
  src="interactive_transfer_learning/fig-transfer_learning-prompting.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Prompting: a prompt $\mathbf{p}$ is combined with the input $x$ to change the output $y$.
:::
```

### fig-transfer_learning-pixel_prompt

```markdown
::{#fig-transfer_learning-pixel_prompt}
<iframe
  src="interactive_transfer_learning/fig-transfer_learning-pixel_prompt.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

A prompt can be made out of pixels: a prompt image (which looks like a border of noise here) is added to the input image in order to change the model's behavior. Three different prompts are shown, one that adapts the model to perform scene classification, a second for aesthetics classification, and a third for object classification. Modified from @bahng2022exploring
:::
```

### fig-transformers-prompting_a_transformer

```markdown
::{#fig-transformers-prompting_a_transformer}
<iframe
  src="interactive_transfer_learning/fig-transformers-prompting_a_transformer.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Prompting a transformer with a learnable input token. The prompt token is mixed into the network via attention; therefore \textit{no} parameters of the original network have to be updated (see @sec-transformers).
:::
```

### domain_adaptation_by_translation1.png

```markdown
::{#None}
<iframe
  src="interactive_transfer_learning/fig_domain_adaptation_by_translation1.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Unpaired domain adaptation via adversarial translation.
:::
```

