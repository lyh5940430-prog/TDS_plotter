from reader import load_tds_excel
from plotter import plot_linear


file = "data/1421大气暴露.xlsx"


data = load_tds_excel(file)


plot_linear(
    data,
    "output/Linear"
)


print("Linear绘图完成")