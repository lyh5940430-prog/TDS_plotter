import pandas as pd
from pathlib import Path


# =====================================================
# 原始TDS Excel（兼容旧版本）
# =====================================================

def load_tds_excel(filename):
    """
    读取原始TDS Excel

    返回：

    {
        sheet:{
            "temperature":...,
            "mz":{
                "2":...,
                "18":...
            }
        }
    }
    """

    excel = pd.ExcelFile(filename)

    data = {}

    for sheet in excel.sheet_names:

        df = pd.read_excel(
            filename,
            sheet_name=sheet,
            header=3
        )

        print("读取:", sheet)

        temp_col = None

        for col in df.columns:

            if "Temperature" in str(col):

                temp_col = col

                break

        if temp_col is None:

            print("没有找到Temperature列")

            continue

        mz_data = {}

        for col in df.columns:

            name = str(col)

            if "m/z" in name:

                mz = (
                    name
                    .replace("m/z", "")
                    .strip()
                )

                mz_data[mz] = df[col]

        data[sheet] = {

            "temperature": df[temp_col],

            "mz": mz_data

        }

    return data


# =====================================================
# 多Excel（兼容旧版本）
# =====================================================

def load_folder(folder):

    folder = Path(folder)

    all_data = {}

    excel_files = sorted(
        folder.glob("*.xlsx")
    )

    if len(excel_files) == 0:

        raise FileNotFoundError(
            f"没有在 {folder} 中找到xlsx文件"
        )

    print(f"\n发现 {len(excel_files)} 个Excel文件：")

    for file in excel_files:

        print("读取:", file.name)

        sample = file.stem

        all_data[sample] = load_tds_excel(file)

    return all_data


# =====================================================
# Compare Mode
# 一个CSV = 一个样品
# =====================================================

def load_tds_csv(filename):
    """
    读取处理后的CSV文件

    返回：

    {
        "temperature":...,
        "mz":{
            "2":...,
            "18":...
        }
    }
    """

    df = pd.read_csv(filename,skiprows=8)

    temp_col = None

    for col in df.columns:

        if "Temperature1" in str(col):

            temp_col = col

            break

    if temp_col is None:

        raise ValueError("没有找到Temperature列")

    mz_data = {}

    for col in df.columns:

        name = str(col)

        if "m/z" in name:

            mz = (
                name
                .replace("m/z", "")
                .strip()
            )

            mz_data[mz] = df[col]

    return {

        "temperature": df[temp_col],

        "mz": mz_data

    }


# =====================================================
# Compare Mode
# 读取整个CSV文件夹
# =====================================================

def load_compare_folder(folder):

    folder = Path(folder)

    all_data = {}

    csv_files = sorted(
        folder.glob("*.csv")
    )

    if len(csv_files) == 0:

        raise FileNotFoundError(
            f"{folder} 中没有CSV文件"
        )

    print(f"\n发现 {len(csv_files)} 个样品：")

    for file in csv_files:

        print("读取:", file.name)

        sample = file.stem

        all_data[sample] = load_tds_csv(file)

    return all_data