from pathlib import Path

from src.reader import load_tds_excel
from src.plotter import plot_linear, plot_log
from src.utils import create_output_folder


# ==========================
# Data file
# ==========================

file = "data/1421大气暴露.xlsx"


# 自动获取实验名称
experiment_name = Path(file).stem


# ==========================
# Read data
# ==========================

data = load_tds_excel(file)

# ==========================
# Output folder
# ==========================

linear_path = create_output_folder(
    "output",
    experiment_name,
    "Linear"
)


log_path = create_output_folder(
    "output",
    experiment_name,
    "Log10"
)


# ==========================
# Plot
# ==========================

plot_linear(
    data,
    linear_path
)


plot_log(
    data,
    log_path
)


print("绘图完成")
print("实验:", experiment_name)