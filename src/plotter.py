import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from scipy.signal import savgol_filter
from src.exporter import save_figure
from src.style import apply_style
from src import config
from src.config import COLORS, AUTO_COLORS

# ===========================
# Color Map
# ===========================

COLORS = {
    "vacuum": "black",
    "1h": "#1f77b4",
    "2h": "#0033ff",
    "4h": "#ff7f0e",
    "first": "red"
}


def get_color(sheet):

    if sheet in COLORS:
        return COLORS[sheet]

    index = abs(hash(sheet)) % len(AUTO_COLORS)

    return AUTO_COLORS[index]

# ===========================
# Smooth
# ===========================


def smooth_curve(y):

    y = np.asarray(y, dtype=float)

    if (
        config.SMOOTH_ENABLE
        and len(y) >= config.SMOOTH_WINDOW
    ):
        return savgol_filter(
            y,
            window_length=config.SMOOTH_WINDOW,
            polyorder=config.SMOOTH_POLY
        )

    return y


# ===========================
# Common Plot
# ===========================

def _plot(data, output, log=False):

    apply_style()

    output = Path(output)
    output.mkdir(
        parents=True,
        exist_ok=True
    )

    mz_list = sorted({
        mz
        for sheet in data
        for mz in data[sheet]["mz"].keys()
    })


    for mz in mz_list:

        fig, ax = plt.subplots(
            figsize=config.FIGSIZE
        )


        for sheet in data:

            if mz not in data[sheet]["mz"]:
                continue


            x = np.asarray(
                data[sheet]["temperature"],
                dtype=float
            )


            y = smooth_curve(
                data[sheet]["mz"][mz]
            )


            y = np.asarray(
                y,
                dtype=float
            )


            if log:

                y[y <= 0] = config.LOG_MIN_VALUE


            ax.plot(
                x,
                y,
                label=sheet,
                linewidth=config.LINE_WIDTH,
                color=get_color(sheet)
            )


        # x轴

        ax.set_xlim(
            config.X_MIN,
            config.X_MAX
        )


        ax.set_xticks(
            np.arange(
                config.X_MIN,
                config.X_MAX + 1,
                config.X_INTERVAL
            )
        )


        # log模式

        if log:

            ax.set_yscale(
                "log",
                base=config.LOG_BASE
            )

            ax.minorticks_on()



        # 标签

        ax.set_xlabel(
            config.X_LABEL
        )

        ax.set_ylabel(
            f"{config.Y_LABEL} (m/z {mz})"
        )


        # 图例

        ax.legend(
            fontsize=config.LEGEND_SIZE,
            frameon=False,
            loc="upper left"
        )


        # 去掉边框

        if config.REMOVE_TOP_RIGHT_SPINE:

            ax.spines["top"].set_visible(False)

            ax.spines["right"].set_visible(False)



        # 刻度

        ax.tick_params(
            direction="in",
            length=6,
            width=1.5,
            which="major"
        )


        ax.tick_params(
            direction="in",
            length=3,
            width=1,
            which="minor"
        )


        fig.tight_layout(
            pad=1.2
        )


        save_figure(
            fig,
            output,
            f"mz_{mz}"
        )


        plt.close(fig)
# ===========================
# Linear
# ===========================

def plot_linear(data, output):

    _plot(
        data,
        output,
        log=False
    )


# ===========================
# Log10
# ===========================

def plot_log(data, output):

    _plot(
        data,
        output,
        log=True
    )