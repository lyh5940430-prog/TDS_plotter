from pathlib import Path
from datetime import datetime


def write_compare_report(
    data,
    output_folder,
    experiment_name
):
    """
    生成Compare实验报告
    """

    output_folder = Path(output_folder)

    report_file = output_folder / "Report.txt"

    # ==========================
    # 样品名称
    # ==========================

    sample_list = list(data.keys())

    # ==========================
    # m/z
    # ==========================

    mz_set = set()

    for sample in data:

        mz_set.update(
            data[sample]["mz"].keys()
        )

    mz_list = sorted(
        mz_set,
        key=float
    )

    # ==========================
    # 温度范围
    # ==========================

    first_sample = sample_list[0]

    temperature = data[first_sample]["temperature"]

    temp_min = float(min(temperature))

    temp_max = float(max(temperature))

    # ==========================
    # 写报告
    # ==========================

    with open(
        report_file,
        "w",
        encoding="utf-8"
    ) as f:

        f.write("=" * 60 + "\n")
        f.write("TDS Plotter Report\n")
        f.write("=" * 60 + "\n\n")

        f.write("Experiment\n")
        f.write("-" * 60 + "\n")
        f.write(f"{experiment_name}\n\n")

        f.write("Generated Time\n")
        f.write("-" * 60 + "\n")
        f.write(
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )
        f.write("\n\n")

        f.write("Sample Number\n")
        f.write("-" * 60 + "\n")
        f.write(
            f"{len(sample_list)}\n\n"
        )

        f.write("Samples\n")
        f.write("-" * 60 + "\n")

        for sample in sample_list:

            f.write(sample + "\n")

        f.write("\n")

        f.write("m/z List\n")
        f.write("-" * 60 + "\n")

        for mz in mz_list:

            f.write(f"{mz}\n")

        f.write("\n")

        f.write("Temperature Range\n")
        f.write("-" * 60 + "\n")

        f.write(
            f"{temp_min:.1f} ℃  ~  {temp_max:.1f} ℃\n\n"
        )

        f.write("Software\n")
        f.write("-" * 60 + "\n")

        f.write("TDS Plotter v1.0\n")

    print("Report Saved:")
    print(report_file)