"""
TDS Plotter Configuration

所有绘图参数集中管理
"""

# ==================================================
# Figure Settings
# ==================================================

# 图片尺寸 (inch)
FIGSIZE = (10, 5)

# 输出分辨率
DPI = 600


# ==================================================
# Font Settings
# ==================================================

FONT_FAMILY = "Arial"

FONT_SIZE = 14

LABEL_SIZE = 14

LEGEND_SIZE = 12

TITLE_SIZE = 16

# =====================================
# Compare Plot
# =====================================

# Compare图片尺寸
COMPARE_FIGSIZE = (10, 5)


# X轴范围
COMPARE_X_MIN = 50
COMPARE_X_MAX = 1200
COMPARE_X_INTERVAL = 100


# Y轴范围
# None = 自动
COMPARE_Y_MIN = None
COMPARE_Y_MAX = None


# 标题
SHOW_TITLE = True

TITLE_FONT_SIZE = 14

# ==================================================
# Line Settings
# ==================================================

# 曲线宽度
LINE_WIDTH = 2.5

# 坐标轴宽度
AXIS_WIDTH = 1.5



# ==================================================
# Color Settings
# ==================================================
COLORS = {

    "vacuum": "black",

    "1h": "#1f77b4",

    "2h": "#0033ff",

    "4h": "#ff8c00",

    "first": "#d62728"

}


# 默认颜色数量不足时使用

AUTO_COLORS = [

    "black",

    "#1f77b4",

    "#d62728",

    "#ff7f0e",

    "#9467bd",

    "#2ca02c",

    "#8c564b",

    "#e377c2",

    "#7f7f7f",

    "#17becf",

]
# ==================================================
# Smoothing Settings
# ==================================================

# 是否开启平滑
SMOOTH_ENABLE = True


# Savitzky-Golay 参数
SMOOTH_WINDOW = 11

SMOOTH_POLY = 3



# ==================================================
# Axis Settings
# ==================================================

# 温度范围

X_MIN = 0

X_MAX = 1200


# x轴刻度间隔

X_INTERVAL = 200



# Log 设置

LOG_BASE = 10


# 负值替换

LOG_MIN_VALUE = 1e-20



# ==================================================
# Export Settings
# ==================================================

SAVE_PNG = True

SAVE_PDF = True

SAVE_SVG = True



# 是否自动关闭顶部和右侧边框

REMOVE_TOP_RIGHT_SPINE = True



# ==================================================
# Theme
# ==================================================

# 以后扩展:
# Nature
# ACS
# IEEE
# Origin

THEME = "Origin"
# ==================================================
# Plot Settings
# ==================================================

LINEAR_FOLDER = "Linear"

LOG_FOLDER = "Log10"

X_LABEL = "T1 Temperature (°C)"

Y_LABEL = "Ion Current"
THEMES = {

    "Origin":{

        "figure_facecolor":"white",

        "grid":False

    },

    "Nature":{

        "figure_facecolor":"white",

        "grid":False

    }

}
# =====================================
# Compare Mode
# =====================================

NAME_MAP = {

    "20260408_GZ_1421_1_3h_SIM_A": "3 h",

    "20260408_GZ_1421_2_7d_SIM_A": "7 d",

    "20260408_GZ_1421_3_14d_SIM_A": "14 d",

    "20260506_GZ_1421_6_28d_SIM_A": "28 d",

}