# popularipy
A little Python package to access popularity metrics for your package

- [x] Downloads history from Pypi
- [x] Stars history from Github
- [ ] GitHub traffic history from Github (See https://github.com/seladb/github-traffic-stats)

## Installation

```
pip install https://github.com/DominiqueMakowski/popularipy/zipball/master
```

## Demo

Example for the [`NeuroKit`](https://github.com/neuropsychology/NeuroKit) package.
```python
import popularipy

# Pypi downloads
data = popularipy.pypi_downloads("neurokit2")
data.plot(x="Date")

# GitHub stars
data = popularipy.github_stars("neuropsychology/neurokit", "myaccesstoken")
data.plot(x="Date")
```
