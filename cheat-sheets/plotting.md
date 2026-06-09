# Matplotlib Cheatsheet

## Setup
```python
import matplotlib.pyplot as plt
import numpy as np
```

## Basic Plots
**Line:** `plt.plot(x, y)` | **Scatter:** `plt.scatter(x, y)` | **Bar:** `plt.bar(x, y)` | **Hist:** `plt.hist(data, bins=20)`

## Plot Customization
```python
plt.title('Title')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.xticks(range(0, 110, 20))
plt.legend()
plt.show()
```

## Font Sizes
`fontsize='x-small'` | `fontsize='small'` | `fontsize='medium'` | `fontsize='large'` | `fontsize=8`

## Stacked Bar Chart
```python
x = np.arange(len(people))
plt.bar(x, data1, label='Type 1')
plt.bar(x, data2, bottom=data1, label='Type 2')
plt.xticks(x, people)
plt.legend()
```

## Subplots with GridSpec
```python
import matplotlib.gridspec as gridspec
fig = plt.figure()
fig.suptitle('Main Title')
gs = gridspec.GridSpec(3, 2, figure=fig)

plt.subplot(gs[0, 0])
plt.plot(x, y)

plt.subplot(gs[2, :])  # Full width
plt.plot(x, y)

plt.subplots_adjust(hspace=0.4, wspace=0.3)
```

## Colormaps & Colors
```python
# Color by values
plt.scatter(x, y, c=z, cmap='plasma')
scatter = plt.scatter(x, y, c=z, cmap='viridis')
plt.colorbar(scatter, label='Label')

# Custom colors
plt.plot(x, y, color='red')
plt.bar(x, y, color='#ff8000')
```

**Common colormaps:** plasma, viridis, cool, hot, RdBu, Blues, Reds, autumn, spring, summer, winter, jet

## 3D Plotting
```python
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

scatter = ax.scatter(x, y, z, c=labels, cmap='plasma')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Title')
plt.colorbar(scatter)
```

## Data Prep
```python
# Normalize
data_means = np.mean(data, axis=0)
norm_data = data - data_means

# PCA (reduce to 3D)
_, _, Vh = np.linalg.svd(norm_data)
pca_data = np.matmul(norm_data, Vh[:3].T)

# Random data
np.random.seed(5)
x = np.random.randn(1000) * 10
```

## Figure Settings
```python
plt.figure(figsize=(6.4, 4.8))
plt.savefig('filename.png', dpi=150)
```

## Common Mistakes
| Mistake | Fix |
|---------|-----|
| `fig = plt.figure` | Add `()`: `plt.figure()` |
| `set_xlable()` | Use `set_xlabel()` |
| `set_ylable()` | Use `set_ylabel()` |
| `set_zlable()` | Use `set_zlabel()` |
| `cmap='plazma'` | Correct spelling: `'plasma'` |
| Labels overlap | `plt.subplots_adjust(hspace=0.4, wspace=0.3)` |
| No colorbar | Call `plt.colorbar(scatter)` after scatter |