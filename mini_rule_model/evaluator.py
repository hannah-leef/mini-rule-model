from .parser import parse_script

# --------------------------------------------------------------
# Evaluator for parsed rules
# --------------------------------------------------------------
# Executes rules and stores variables in a dictionary
# --------------------------------------------------------------

def run_script(script: str):
    commands = parse_script(script)
    variables = {}

    for cmd in commands:
        if cmd["type"] == "set":
            raw_value = cmd["value"]

            try:
                # evaluate using current variables as locals (no globals)
                value = eval(raw_value, {}, variables)
            except Exception:
                # fallback: keep raw string (strip surrounding quotes if present)
                value = raw_value.strip()
                if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
                    value = value[1:-1]

            variables[cmd["variable"]] = value

        elif cmd["type"] == "if":
            condition = cmd["condition"]
            action_var = cmd["action"]["variable"]
            action_val_raw = cmd["action"]["value"]

            try:
                if eval(condition, {}, variables):
                    try:
                        val = eval(action_val_raw, {}, variables)
                    except Exception:
                        val = action_val_raw.strip()
                        if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                            val = val[1:-1]

                    variables[action_var] = val

            except Exception as e:
                print(f"Rule error evaluating condition '{condition}': {e}")

    return variables