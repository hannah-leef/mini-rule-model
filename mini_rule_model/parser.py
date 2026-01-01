import re

def parse_script(script: str):
    commands = []

    lines = script.strip().splitlines()
    for line in lines:
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        if line.startswith("SET"):
            match = re.match(r"SET\s+(\w+)\s*=\s*(.+);", line)
            if match:
                commands.append({
                    "type": "set",
                    "variable": match.group(1),
                    "value": match.group(2)
                })

        elif line.startswith("IF"):
            match = re.match(r"IF\s+(.+)\s+THEN\s+(.+);", line)
            if match:
                commands.append({
                    "type": "if",
                    "condition": match.group(1),
                    "action": match.group(2)
                })

    return commands
