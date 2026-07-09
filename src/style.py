import matplotlib.pyplot as plt
from src import config


def apply_style():

    # ---------------- Font ----------------
    plt.rcParams["font.family"] = config.FONT_FAMILY
    plt.rcParams["font.size"] = config.FONT_SIZE

    # ---------------- Figure ----------------
    plt.rcParams["figure.dpi"] = 150
    plt.rcParams["savefig.dpi"] = config.DPI

    # ---------------- Axis ----------------
    plt.rcParams["axes.linewidth"] = config.AXIS_WIDTH

    # ---------------- Tick ----------------
    plt.rcParams["xtick.direction"] = "in"
    plt.rcParams["ytick.direction"] = "in"

    plt.rcParams["xtick.major.size"] = 6
    plt.rcParams["ytick.major.size"] = 6

    plt.rcParams["xtick.minor.size"] = 3
    plt.rcParams["ytick.minor.size"] = 3

    # ---------------- Legend ----------------
    plt.rcParams["legend.frameon"] = False

    # ---------------- PDF ----------------
    plt.rcParams["pdf.fonttype"] = 42
    plt.rcParams["ps.fonttype"] = 42