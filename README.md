# How to dev locally?
We need just two things. 

1. One-click install the dependency [`quarto`](https://quarto.org/docs/get-started/). We really just need that page's step-one one `CLI` download. If the install goes right, the executable `quarto` should be callable from the terminal.
   
2. Clone this repo. In the terminal, `cd` into the root of this repo. Run `quarto preview`. If all goes well, a `localhost:<some_port>` link will pop up, and a browser tab will open. That tab will be "live": i.e. it'd be updated as we make local changes. Book chapters are those `*.qmd` files. The syntax is almost identical to `markdown` (which itself is pretty close to LaTeX).
