window.MathJax = {
  loader: {load: ['[tex]/mhchem']},
  tex: {
    packages: {'[+]': ['mhchem']},
    inlineMath: [["\\(", "\\)"], ["$", "$"]],
    displayMath: [["\\[", "\\]"], ["$$", "$$"]],
    processEscapes: true,
    processEnvironments: true,
    tags: "ams",
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

// document$.subscribe(() => { 
//   MathJax.startup.output.clearCache()
//   MathJax.typesetClear()
//   MathJax.texReset()
//   MathJax.typesetPromise()
// })

document$.subscribe(() => {
  MathJax.startup.output.clearCache()
  MathJax.typesetClear()
  MathJax.texReset()
  // First pass: registers all \labels and assigns numbers
  MathJax.typesetPromise().then(() => {
    // Second pass: resolves \eqref now that labels are known
    MathJax.typesetPromise()
  })
})