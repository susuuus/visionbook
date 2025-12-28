# Integration Snippets for motion_estimation_intro.qmd

Replace the original ![...](figures/...) with these iframe embeds:

### fig-050822_172806__MG_5366

```markdown
::{#fig-050822_172806__MG_5366}
<iframe
  src="interactive_motion_estimation_intro/fig-050822_172806__MG_5366.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Even from a static picture we form a rich representation of the dynamics of the scene. *Source*: Photograph by Fredo Durand
:::
```

### fig-motion_illusion

```markdown
::{#fig-motion_illusion}
<iframe
  src="interactive_motion_estimation_intro/fig-motion_illusion.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Motion-induced visual illusion, after @Murakami2010.  The illusion becomes stronger when viewed peripherally rather than looking directly at the image. Changing the contrast of this image can change the direction of perceived motion.
:::
```

### fig-two_frames_from_palma_street-a

```markdown
::{#fig-two_frames_from_palma_street-a}
<iframe
  src="interactive_motion_estimation_intro/fig-two_frames_from_palma_street-a.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Frame 1
:::
```

### fig-two_frames_from_palma_street-b

```markdown
::{#fig-two_frames_from_palma_street-b}
<iframe
  src="interactive_motion_estimation_intro/fig-two_frames_from_palma_street-b.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Frame 2
:::
```

### algorithm_match.png

```markdown
::{#None}
<iframe
  src="interactive_motion_estimation_intro/fig_algorithm_match.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Patch matching motion estimation. The algorithm starts by chopping the two frames into overlapping patches. Then, for every patch from the first frame, we compute the distance to all the nearby patches in frame 2. Finally, for each input patch we select the closest patch from frame 2 and we record the relative displacement between the two patches. The pseudocode can be rearranged to be more memory efficient.
:::
```

### fig-matching_cost_figure

```markdown
::{#fig-matching_cost_figure}
<iframe
  src="interactive_motion_estimation_intro/fig-matching_cost_figure.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Two frames and best match for an input patch from frame 1 within frame 2. Search is done only within a small neighborhood.
:::
```

### fig-matching_optical_flow_patch_size_effect

```markdown
::{#fig-matching_optical_flow_patch_size_effect}
<iframe
  src="interactive_motion_estimation_intro/fig-matching_optical_flow_patch_size_effect.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Effect of the choice of the patch size parameter, $s$, on the estimated optical flow. When the patch size is just one pixel ($s=0$), the approach fails as there are many similar pixels that correspond to different parts of the scene. Only when the patches are large enough, the image matches correspond to the same scene elements. Large patch sizes are necessary. But too large patches lead to oversmoothing.
:::
```

### fig-motionIllusion1

```markdown
::{#fig-motionIllusion1}
<iframe
  src="interactive_motion_estimation_intro/fig-motionIllusion1.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Space-time signals, building toward the fluted square-wave motion illusion. The first row shows a stationary sine wave. (a) Movie of a motionless sine wave. (b) Space-time plot shows only vertical structure. (c) Spatiotemporal Fourier transform shows all energy on the zero temporal frequency axis because nothing is moving. (d) The second row shows a moving sine wave. (e) In the space-time plot, speed corresponds to
local orientation. (f) The Fourier transform energy is sheared according to
the sine wave’s speed. (g–i) The third row shows a moving square wave. The additional harmonics required to form a square wave are visible in (i) the spatiotemporal Fourier transform.
:::
```

### fig-motionIllusion2

```markdown
::{#fig-motionIllusion2}
<iframe
  src="interactive_motion_estimation_intro/fig-motionIllusion2.html"
  width="100%"
  height="700"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>

Derivation of the fluted square-wave motion illusion, continued from @fig-motionIllusion1 . Top row shows that the square wave moves in 1/4 wavelength jumps, instead of continuously. This staggered motion generates the additional spatiotemporal frequencies shown in (c).  The lowest spatiotemporal frequency (green rectangle) still indicates motion to the left.  Second row shows that if we remove the lowest spatial frequency sine wave of the square wave, creating a* fluted square wave*, then the lowest spatio-emporal frequency now moves in the other direction.  This is also visible from (e) the space time plot and especially in (f) the spatiotemporally low-pass filtered version.
:::
```

