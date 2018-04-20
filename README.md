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

# set some mpl params for the minimal theme.
pp.set()

fig, ax = plt.subplots()

ax.scatter(np.random.uniform(size=100), np.random.uniform(size=100))
pp.set_title(ax, "Title", "Subtitle", "Optional caption", "author")
pp.savefig(fig, "result.png")
```

## Result

![](https://github.com/etra0/personal_plot/raw/master/example/result.png)
