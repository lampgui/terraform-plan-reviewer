from rich.console import Console
from rich.markdown import Markdown
import json

console = Console()

def print_output(text, format="text"):
    if format == "markdown":
        console.print(Markdown(text))
    elif format == "json":
        console.print_json(data=json.dumps({"summary": text}))
    else:
        console.print(text)
