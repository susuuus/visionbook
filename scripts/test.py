import re

text = r"""$$\begin{aligned}\ell_{\delta_k} \left[n,m\right] &=& \ell\left[n,m\right] \sum_{s=0}^{N/k-1} \sum_{r=0}^{M/k-1} \delta \left[n - sk \, ,m - rk \right] \\
&=&  \ell\left[n,m\right]  \delta_k \left[n,m\right]
#eq-down2
\end{aligned}$$"""

# Regular expression pattern to find all occurrences of \ref{...} and \eqn{\ref{...}}

pattern = r"(\$\$.*?)(#eq-[\w-]+)(.*?\$\$)"
replacement = r"\1\3{\2}"
simplified_text = re.sub(pattern, replacement, text, flags=re.DOTALL)
print(simplified_text)
print("now")

pattern = r"(\$\$.*?)(?:\s*\n){2}(.*?\$\$\{#eq-[\w-]+\})"
replacement = r"\1\2"
simplified_text = re.sub(pattern, replacement, simplified_text, flags=re.DOTALL)
print(simplified_text)
