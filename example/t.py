import matplotlib.pyplot as plt
import personal_plot as pp
import numpy as np

pp.set()

fig, ax = plt.subplots()

ax.scatter(np.random.uniform(size=100), np.random.uniform(size=100))
pp.set_title(ax, "Title", "Subtitle", "Optional caption", "author")
pp.savefig(fig, "result.png")
