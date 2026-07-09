import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
from scipy.signal import savgol_filter


COLORS = {
    "vacuum": "black",
    "2h": "blue",
    "first": "red"
}


def smooth_curve(y):

    y = np.array(y, dtype=float)

    if len(y) >= 11:
        return savgol_filter(
            y,
            window_length=11,
            polyorder=3
        )

    return y



def plot_linear(data, output):

    output = Path(output)
    output.mkdir(
        parents=True,
        exist_ok=True
    )


    mz_list = set()

    for sheet in data:
        mz_list.update(
            data[sheet]["mz"].keys()
        )


    for mz in mz_list:

        plt.figure(
            figsize=(5,4)
        )


        for sheet in data:

            if mz not in data[sheet]["mz"]:
                continue


            T = data[sheet]["temperature"]

            y = smooth_curve(
                data[sheet]["mz"][mz]
            )


            plt.plot(
                T,
                y,
                label=sheet,
                linewidth=2,
                color=COLORS.get(sheet)
            )


        plt.xlabel(
            "T1 Temperature (°C)"
        )

        plt.ylabel(
            f"Ion Current (m/z {mz})"
        )


        plt.tick_params(
            direction="in"
        )


        plt.legend(
            frameon=False
        )


        plt.tight_layout()


        plt.savefig(
            output / f"mz_{mz}.png",
            dpi=600
        )


        plt.close()