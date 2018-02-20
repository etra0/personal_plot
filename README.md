# Monkey customization for matplotlib

Just a monkey customization for matplotlib.

to install run

```bash
pip install .
```

to use it:
```python
import matplotlib.pyplot as plt
import personal_plot as pp
import numpy as np

fig, ax = plt.subplots()

ax.scatter(np.random.uniform(size=100), np.random.uniform(size=100))
pp.set_title(ax, "Title", "Subtitle", "Optional caption", "author")
pp.savefig(fig, "result.png")
```

# Image Example:

![](https://user-images.githubusercontent.com/19335821/36036165-e39a32a2-0d97-11e8-8827-b1ad45a78961.png)
