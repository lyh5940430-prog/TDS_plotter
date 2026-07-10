from src.reader import load_compare_folder
from src.plotter import plot_compare

data = load_compare_folder("data")

plot_compare(
    data,
    "output/Compare"
)