from mini_rule_model.simulator import run_simulation
from mini_rule_model.visualize import plot_variable

script = """
SET decrement = 5;
IF heart_rate > 100 THEN heart_rate = heart_rate - decrement;
"""

history = run_simulation(
    script,
    initial_vars={"heart_rate": 120},
    steps=5
)

for i, state in enumerate(history):
    print(f"Step {i}: {state}")

plot_variable(history, "heart_rate")