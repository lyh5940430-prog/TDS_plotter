from pathlib import Path


def create_output_folder(base, experiment, mode):

    """
    创建输出目录

    base:
        output

    experiment:
        数据文件名

    mode:
        Linear / Log10
    """

    path = (
        Path(base)
        / experiment
        / mode
    )

    path.mkdir(
        parents=True,
        exist_ok=True
    )

    return path