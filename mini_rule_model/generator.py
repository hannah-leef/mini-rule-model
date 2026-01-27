# --------------------------------------------------------------
# Rule generator
# --------------------------------------------------------------
# Generates simple rule scripts from threshold definitions.
# Useful for simulations or synthetic physiological models.
# --------------------------------------------------------------

def generate_rules(thresholds: dict, include_init: bool = True, init_value=0, action_value=1):
    """
    thresholds example:
    {
        "heart_rate": (100, "tachycardia"),
        "spo2": (92, "hypoxia")
    }

    Parameters:
      - include_init: if True, add a SET line initializing each variable to init_value
      - init_value: initial value to use for SET lines (default 0)
      - action_value: value to assign to the label when threshold is exceeded (default 1)
    """
    lines = []

    for var, (limit, label) in thresholds.items():
        if include_init:
            # Initializes the variable (placeholder value)
            lines.append(f"SET {var} = {init_value};")

        # Generates a simple threshold rule
        lines.append(f"IF {var} > {limit} THEN {label} = {action_value};")

    return "\n".join(lines)