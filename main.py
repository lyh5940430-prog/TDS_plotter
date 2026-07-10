from pathlib import Path
from src.report import write_compare_report
from src.reader import load_compare_folder
from src.plotter import plot_compare


# =====================================
# 实验设置
# =====================================

EXPERIMENT_NAME = "1421_wo_HF"


# =====================================
# 主程序
# =====================================

def main():

    # 输入数据路径

    data_folder = Path(
        "data"
    ) / EXPERIMENT_NAME

    # 输出路径

    output_folder = Path(
        "output"
    ) / EXPERIMENT_NAME

    print("=" * 50)

    print(
        "Experiment:",
        EXPERIMENT_NAME
    )

    print(
        "Input:",
        data_folder
    )

    print(
        "Output:",
        output_folder
    )

    print("=" * 50)

    # 读取数据

    data = load_compare_folder(
        data_folder
    )

    # Linear

    plot_compare(
        data,
        output_folder / "Linear",
        experiment_name=EXPERIMENT_NAME,
        log=False
    )

    # Log10

    plot_compare(
        data,
        output_folder / "Log",
        experiment_name=EXPERIMENT_NAME,
        log=True
    )
    write_compare_report(
        data,
        output_folder,
        EXPERIMENT_NAME
    )


print()

print("=" * 50)

print("Finished!")

print("=" * 50)


if __name__ == "__main__":

    main()
