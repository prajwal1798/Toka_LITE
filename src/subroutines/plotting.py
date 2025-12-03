import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401


def plot_surface(
    X,
    Y,
    Z,
    xlabel: str,
    ylabel: str,
    zlabel: str,
    title: str,
    cmap: str = "viridis",
    elev: float = 30.0,
    azim: float = -60.0,
    figsize=(4.5, 3.2),
    dpi=130,
    savepath=None,
):
    """
    3D surface plot helper for PROCESS-Lite 0D scans.

    Parameters
    ----------
    X, Y, Z : 2D numpy arrays
        Grid values.
    xlabel, ylabel, zlabel : str
        Axis labels.
    title : str
        Plot title.
    cmap : str
        Matplotlib colormap.
    elev, azim : float
        Camera elevation and azimuth.
    figsize : tuple
        Figure size in inches.
    dpi : int
        Resolution.
    savepath : str or None
        If provided, saves figure instead of only displaying.
    """

    fig = plt.figure(figsize=figsize, dpi=dpi)
    ax = fig.add_subplot(111, projection="3d")

    surf = ax.plot_surface(
        X,
        Y,
        Z,
        cmap=cmap,
        linewidth=0,
        antialiased=True,
        shade=True,
    )

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.set_title(title)
    ax.view_init(elev=elev, azim=azim)

    fig.colorbar(surf, shrink=0.65, pad=0.08)
    plt.tight_layout()

    if savepath is not None:
        plt.savefig(savepath, dpi=dpi, bbox_inches="tight")

    return fig, ax
