import re

def parse_script(script: str):
    commands = []

    lines = script.strip().splitlines()
    for line in lines:
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        if line.upper().startswith("SET"):
            match = re.match(r"SET\s+(\w+)\s*=\s*(.+);", line, flags=re.IGNORECASE)
            if match:
                commands.append({
                    "type": "set",
                    "variable": match.group(1),
                    "value": match.group(2).strip()
                })

        elif line.upper().startswith("IF"):
            # parse condition and action (action broken into variable and value)
            match = re.match(r"IF\s+(.+?)\s+THEN\s+(\w+)\s*=\s*(.+);", line, flags=re.IGNORECASE)
            if match:
                commands.append({
                    "type": "if",
                    "condition": match.group(1).strip(),
                    "action": {
                        "variable": match.group(2),
                        "value": match.group(3).strip()
                    }
                })

    return commands