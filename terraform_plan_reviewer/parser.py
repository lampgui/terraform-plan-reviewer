import json

def extract_changes(plan_file):
    with open(plan_file, "r") as f:
        plan = json.load(f)

    changes = []

    for res in plan.get("resource_changes", []):
        addr = res["address"]
        actions = res["change"]["actions"]
        action_str = ", ".join(actions).upper()

        if "replace" in res["change"]:
            replacement = res["change"]["replace"]
        else:
            replacement = []

        summary = f"- {action_emoji(actions)} `{addr}` will be {action_str.lower()}"
        if replacement:
            summary += " (⚠️ requires replacement)"
        changes.append(summary)

    return "\n".join(changes)

def action_emoji(actions):
    if "create" in actions and "delete" in actions:
        return "♻️"
    elif "create" in actions:
        return "✅"
    elif "delete" in actions:
        return "🛑"
    elif "update" in actions:
        return "🔄"
    return "❓"
