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
                value = eval(raw_value)
            except:
                value = raw_value

            variables[cmd["variable"]] = value

        elif cmd["type"] == "if":
            condition = cmd["condition"]
            action = cmd["action"]

            try:
                if eval(condition, {}, variables):
                    var, val = action.split("=")
                    var = var.strip()
                    val = val.strip()

                    try:
                        val = eval(val, {}, variables)

                    except:
                        pass

                    variables[var] = val

            except Exception as e:
                print(f"Rule error: {e}")

    return variables
