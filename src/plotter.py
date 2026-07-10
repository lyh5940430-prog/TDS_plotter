import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from scipy.signal import savgol_filter
from src.exporter import save_figure
from src.style import apply_style
from src import config
from src.config import COLORS, AUTO_COLORS
import re


def get_sample_label(sample):
    """
    自动从文件名提取图例名称

    例如：

    20260408_GZ_1421_1_3h_SIM_A
        ↓
        3 h

    20260506_GZ_1421_6_28d_SIM_A
        ↓
        28 d
    """

    m = re.search(r"_(\d+)([hd])_", sample)

    if m:

        number = m.group(1)

        unit = m.group(2)

        if unit == "h":
            return f"{number} h"

        if unit == "d":
            return f"{number} d"

    return sample


def get_sample_time(sample):
    """
    返回样品对应的小时数，用于排序

    例如：

    0 h  -> 0
    6 h  -> 6
    24 h -> 24
    7 d  -> 168
    14 d -> 336
    """

    label = get_sample_label(sample)

    m = re.search(r"(\d+)\s*([hd])", label.lower())

    if m is None:
        return 999999

    value = int(m.group(1))

    unit = m.group(2)

    if unit == "h":
        return value

    if unit == "d":
        return value * 24

    return value
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


def plot_compare(
    data,
    output,
    experiment_name="",
    log=False
):
    """
    Compare Mode

    一个CSV = 一个样品
    同一个m/z画在一张图中
    """

    # ==========================
    # 初始化
    # ==========================

    output = Path(output)

    output.mkdir(
        parents=True,
        exist_ok=True
    )

    apply_style()

    # ==========================
    # 获取全部m/z
    # ==========================

    mz_list = sorted(

        {
            mz

            for sample in data

            for mz in data[sample]["mz"]

        },

        key=float

    )

    # ==========================
    # 样品排序
    # ==========================
    sample_names = list(data.keys())


    ordered_samples = sorted(

    sample_names,

    key=get_sample_time

)

    # ==========================
    # 颜色映射
    # ==========================

    color_map = {}

    for i, sample in enumerate(ordered_samples):

        color_map[sample] = AUTO_COLORS[
            i % len(AUTO_COLORS)
        ]
    # ==========================
    # 绘图
    # ==========================

    for mz in mz_list:

        fig, ax = plt.subplots(
            figsize=config.COMPARE_FIGSIZE
        )

        # --------------------------
        # 绘制不同样品
        # --------------------------

        for sample in ordered_samples:

            if mz not in data[sample]["mz"]:
                continue

            x = np.asarray(
                data[sample]["temperature"],
                dtype=float
            )

            y = smooth_curve(
                data[sample]["mz"][mz]
            )

            y = np.asarray(
                y,
                dtype=float
            )

            # Log处理

            if log:

                y[y <= 0] = config.LOG_MIN_VALUE


            ax.plot(

                x,

                y,

                label=get_sample_label(sample),

                linewidth=config.LINE_WIDTH,

                color=color_map[sample]

            )

        # --------------------------
        # 坐标轴
        # --------------------------

        ax.set_xlim(

            config.COMPARE_X_MIN,

            config.COMPARE_X_MAX

        )

        if log:

            ax.set_yscale(

                "log",

                base=config.LOG_BASE

            )

            ax.minorticks_on()


        # Y轴手动范围

        if (

            config.COMPARE_Y_MIN is not None

            and

            config.COMPARE_Y_MAX is not None

        ):

            ax.set_ylim(

                config.COMPARE_Y_MIN,

                config.COMPARE_Y_MAX

            )


        # --------------------------
        # 标签
        # --------------------------

        ax.set_xlabel(

            config.X_LABEL

        )

        ax.set_ylabel(

            f"{config.Y_LABEL} (m/z {mz})"

        )


        # --------------------------
        # 标题
        # --------------------------

        if config.SHOW_TITLE:

            ax.set_title(

                f"{experiment_name}\nm/z {mz}",

                fontsize=config.TITLE_FONT_SIZE

            )


        # --------------------------
        # 图例
        # --------------------------

        ax.legend(

            frameon=False,

            fontsize=max(

                config.LEGEND_SIZE - 2,

                8

            ),

            loc="upper left",

            bbox_to_anchor=(1.02, 1.00)

        )


        # --------------------------
        # 刻度
        # --------------------------

        ax.tick_params(

            direction="in",

            which="major"

        )

        ax.tick_params(

            direction="in",

            which="minor"

        )


        # --------------------------
        # 边框
        # --------------------------

        if config.REMOVE_TOP_RIGHT_SPINE:

            ax.spines["top"].set_visible(False)

            ax.spines["right"].set_visible(False)


        # --------------------------
        # 保存
        # --------------------------

        fig.tight_layout(

            rect=[0, 0, 0.82, 1]

        )

        save_figure(

            fig,

            output,

            f"mz_{mz}"

        )


        plt.close(fig)
