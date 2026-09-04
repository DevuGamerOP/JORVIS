import json
import os

PLUGIN = {
    "name": "todo_list",
    "description": (
        "Manage a to-do list. Use this tool when the user asks to add, remove, or list tasks."
    ),
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "action": {"type": "STRING", "description": "add | remove | list"},
            "item": {"type": "STRING", "description": "The task to add or remove"}
        },
        "required": ["action"],
    },
}

def run(parameters: dict, player=None, session_memory=None) -> str:
    action = parameters.get("action", "").lower()
    item = parameters.get("item", "")

    file_path = "memory/todo_list.json"

    todos = []
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                todos = json.load(f)
        except Exception:
            todos = []

    if action == "add":
        if not item:
            return "Please specify an item to add."
        todos.append(item)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(todos, f)
        if player:
            player.write_log(f"JARVIS: Added '{item}' to the to-do list.")
        return f"Added '{item}' to your to-do list."

    elif action == "remove":
        if not item:
            return "Please specify an item to remove."
        if item in todos:
            todos.remove(item)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(todos, f)
            if player:
                player.write_log(f"JARVIS: Removed '{item}' from the to-do list.")
            return f"Removed '{item}' from your to-do list."
        else:
            return f"I couldn't find '{item}' in your to-do list."

    elif action == "list":
        if not todos:
            return "Your to-do list is empty."
        items = "\n".join(f"- {t}" for t in todos)
        if player:
            player.write_log(f"JARVIS: To-do list:\n{items}")
        return f"Here is your to-do list:\n{items}"

    else:
        return "Invalid action. Please specify 'add', 'remove', or 'list'."
