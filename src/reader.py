import pandas as pd


def load_tds_excel(filename):
    """
    读取TDS Excel文件

    返回:
    data = {
        sheet_name:{
            "temperature": 温度,
            "mz": {
                "2": 数据,
                "18": 数据
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

        # 找温度列
        temp_col = None

        for col in df.columns:
            if "Temperature" in str(col):
                temp_col = col
                break


        if temp_col is None:
            print("没有找到温度列")
            continue


        mz_data = {}


        for col in df.columns:

            name = str(col)

            if "m/z" in name:

                mz = (
                    name
                    .replace("m/z","")
                    .strip()
                )

                mz_data[mz] = df[col]


        data[sheet] = {

            "temperature":
                df[temp_col],

            "mz":
                mz_data
        }


    return data