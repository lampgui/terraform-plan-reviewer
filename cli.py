import click
from parser import extract_changes
from gpt import generate_summary

@click.command()
@click.argument("plan_file", type=click.Path(exists=True))
def analyze(plan_file):
    """Analyze a Terraform plan JSON file with GPT."""
    print("🔍 Parsing Terraform plan...")
    change_summary = extract_changes(plan_file)

    print("🤖 Sending to GPT for analysis...")
    response = generate_summary(change_summary)

    print("\n🧠 GPT Review Summary:\n")
    print(response)

if __name__ == "__main__":
    analyze()

