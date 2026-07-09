from pathlib import Path
from src import config


def save_figure(fig, output_folder, filename):
    """
    保存图片

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        当前Figure

    output_folder : str or Path
        输出目录

    filename : str
        文件名（不带后缀）
    """

    output_folder = Path(output_folder)
    output_folder.mkdir(
        parents=True,
        exist_ok=True
    )

    # PNG
    if config.SAVE_PNG:
        fig.savefig(
            output_folder / f"{filename}.png",
            dpi=config.DPI,
            bbox_inches="tight"
        )

    # PDF
    if config.SAVE_PDF:
        fig.savefig(
            output_folder / f"{filename}.pdf",
            bbox_inches="tight"
        )

    # SVG
    if config.SAVE_SVG:
        fig.savefig(
            output_folder / f"{filename}.svg",
            bbox_inches="tight"
        )