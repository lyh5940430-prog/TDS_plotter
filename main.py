from src.reader import load_tds_excel
from src.plotter import plot_linear,plot_log


file = "data/1421大气暴露.xlsx"


data = load_tds_excel(file)


plot_linear(
    data,
    "output/Linear"
)
plot_log(
    data,
    "output/Log10"
)

print("Linear绘图完成")