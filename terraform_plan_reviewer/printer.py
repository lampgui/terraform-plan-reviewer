from rich.console import Console
from rich.markdown import Markdown

console = Console()

def print_output(text, format="text"):
    if not text:
        print("⚠️ No content to print.")
        return

    if format == "markdown":
        console.print(Markdown(text))
    elif format == "json":
        import json
        print(json.dumps({"summary": text}, indent=2))
    else:
        print(text)
