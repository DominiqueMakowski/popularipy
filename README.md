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
downloads = popularipy.pypi_downloads("neurokit2")
downloads.plot(x="Date")

# GitHub stars
stars = popularipy.github_stars("neuropsychology/neurokit", "myaccesstoken")
stars.plot(x="Date")
```

Combine the data:

```python
import pandas as pd

data = downloads.merge(stars)
data.plot.area(x="Date", y=["Downloads", "Stars"], subplots=True)
```

![](demo.png)
