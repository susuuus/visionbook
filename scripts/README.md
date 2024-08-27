We use the `conv.sh` script to perform the overall conversion. There are a few steps in the conversion process, and we will list them here.

1. .tex to .tex conversion
- [ ] read in the customized macros and \newCommands, so returned .tex can all be standalone
- [ ] turn colons in various places into hyphens
    - [ ] turn `\label{whatever:label} to \label{whatever-label}`, in fact there might be multiple colons in the label, so we need to turn all of them to hyphens
    - [ ] turn `\ref{whatever:label} to \ref{whatever-label}`, similar for the multiple colons
    - [ ] turn `\cite{whatever:label} to @{whatever-label}`, and similar for the multiple colons
- [ ] get rid of \[x inch\] or \[x cm\] 
- [ ] adding or removing line breaks
- [ ] margin note declarative

2. Equation clean up
3. Figure clean up
4. Table clean up
5. Bibliography clean up
6. Cross-referencing clean up
7. Footnote clean up
8. Margin note clean up
9. Customized macros clean up


# 2. Cleaned up .tex to .qmd
- [ ] pandoc conversion
- [] some customized filters


