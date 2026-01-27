from .evaluator import run_script

# --------------------------------------------------------------
# Simple step-based simulator
# --------------------------------------------------------------
# Repeatedly applies the rule engine over multiple time steps.
# Variables persist across steps.
# --------------------------------------------------------------

def run_simulation(script: str, initial_vars: dict, steps: int):
    history = []
    current_vars = initial_vars.copy()

    for step in range(steps):
        # Inject current variable values into the script
        init_lines = []
        for k, v in current_vars.items():
            # use repr to preserve string quoting and booleans/numbers correctly
            init_lines.append(f"SET {k} = {repr(v)};")

        full_script = "\n".join(init_lines) + "\n" + script

        # Run one simulation step
        current_vars = run_script(full_script)

        # Save state
        history.append(current_vars.copy())

    return history
if __name__ == "__main__":
    raise RuntimeError(
        "simulator.py is a module and should not be run directly."
    )