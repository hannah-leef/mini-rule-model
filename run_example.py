from pathlib import Path

from mini_rule_model.simulator import run_simulation
from mini_rule_model.visualize import plot_variable


# load rule script
script = Path("scripts/heart_rate_rules.txt").read_text()

# run simulation
history = run_simulation(
    script,
    initial_vars={
        "heart_rate": 120,
        "oxygen": 95
    },
    steps=5
)

# print results
for i, state in enumerate(history):
    print(f"Step {i}: {state}")

# visualize variables
plot_variable(history, "heart_rate")
plot_variable(history, "oxygen")
