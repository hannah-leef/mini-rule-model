# --------------------------------------------------------------
# Rule generator
# --------------------------------------------------------------
# Generates simple rule scripts from threshold definitions.
# Useful for simulations or synthetic physiological models.
# --------------------------------------------------------------

def generate_rules(thresholds: dict):
    """
    thresholds example:
    {
        "heart_rate": (100, "tachycardia"),
        "spo2": (92, "hypoxia")
    }
    """

    lines = []

    for var, (limit, label) in thresholds.items():
        # Initializes the variable (placeholder value)
        lines.append(f"SET {var} = 0;")

        # Generates a simple threshold rule
        lines.append(
            f"IF {var} > {limit} THEN {label} = 1;"
        )

    return "\n".join(lines)
