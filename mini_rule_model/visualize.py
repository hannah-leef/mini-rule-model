import matplotlib.pyplot as plt
import math


def plot_variable(history, variable_name, ax=None, show=True, save_path=None):
    """
    Plots the value of a variable over simulation steps.

    history: list of dicts (output from run_simulation)
    variable_name: string, e.g. 'heart_rate'
    ax: optional matplotlib Axes to plot into (if None a new figure is created)
    show: boolean, whether to call plt.show() (set False in tests/headless)
    save_path: optional path to save the figure (e.g., "out.png")

    Returns the matplotlib Figure object.
    """
    values = []
    steps = []

    for i, state in enumerate(history):
        if variable_name in state:
            val = state[variable_name]
            # try to coerce to numeric if possible
            try:
                # handle booleans and ints/floats; avoid converting lists/dicts
                if isinstance(val, bool):
                    num = int(val)
                else:
                    num = float(val)
                values.append(num)
                steps.append(i)
            except Exception:
                # non-numeric value — skip or handle as NaN
                values.append(float("nan"))
                steps.append(i)

    if ax is None:
        fig, ax = plt.subplots()
    else:
        fig = ax.figure

    if not steps:
        ax.text(0.5, 0.5, f"No data for '{variable_name}'", ha="center", va="center")
        ax.set_xlabel("Time step")
        ax.set_ylabel(variable_name)
        ax.set_title(f"{variable_name} over time")
    else:
        ax.plot(steps, values, marker="o")
        ax.set_xlabel("Time step")
        ax.set_ylabel(variable_name)
        ax.set_title(f"{variable_name} over time")
        ax.grid(True)

    if save_path:
        fig.savefig(save_path, bbox_inches="tight")

    if show:
        plt.show()

    return fig