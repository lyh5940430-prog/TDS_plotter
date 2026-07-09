"""
layout.py

Reserved for future multi-panel layouts.
"""

from math import ceil
import matplotlib.pyplot as plt


def create_grid(n_plots, max_cols=2, figsize_single=(6.5, 5.0)):
    """
    Create a figure and axes grid.

    Parameters
    ----------
    n_plots : int
        Number of subplots.
    max_cols : int
        Maximum number of columns.
    figsize_single : tuple
        Width, height of one subplot.

    Returns
    -------
    fig, axes
    """
    cols = min(max_cols, max(1, n_plots))
    rows = ceil(n_plots / cols)

    fig, axes = plt.subplots(
        rows,
        cols,
        figsize=(figsize_single[0] * cols,
                 figsize_single[1] * rows),
        squeeze=False
    )

    axes = axes.ravel()

    for ax in axes[n_plots:]:
        ax.remove()

    return fig, axes[:n_plots]
