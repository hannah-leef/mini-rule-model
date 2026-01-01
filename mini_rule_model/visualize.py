import matplotlib.pyplot as plt


def plot_variable(history, variable_name):
    """
    Plots the value of a variable over simulation steps.

    history: list of dicts (output from run_simulation)
    variable_name: string, e.g. 'heart_rate'
    """
    values = []
    steps = []

    for i, state in enumerate(history):
        if variable_name in state:
            steps.append(i)
            values.append(state[variable_name])

    plt.plot(steps, values, marker="o")
    plt.xlabel("Time step")
    plt.ylabel(variable_name)
    plt.title(f"{variable_name} over time")
    plt.grid(True)
    plt.show()
