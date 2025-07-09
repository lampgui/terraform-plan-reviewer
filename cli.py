import click
from parser import extract_changes
from gpt import generate_summary
from printer import print_output

@click.command()
@click.argument("plan_file", type=click.Path(exists=True))
@click.option("--model", default="gpt-3.5-turbo", help="Model to use (gpt-3.5-turbo or gpt-4)")
@click.option("--format", default="text", type=click.Choice(["text", "markdown", "json"]), help="Output format")
@click.option("--output", default=None, help="Save output to file")
def analyze(plan_file, model, format, output):
    """Analyze a Terraform plan JSON file using GPT."""
    print("🔍 Parsing Terraform plan...")
    change_summary = extract_changes(plan_file)

    print("🤖 Sending to GPT for analysis...")
    gpt_output = generate_summary(change_summary, model=model)

    print_output(gpt_output, format=format)

    if output:
        with open(output, "w") as f:
            f.write(gpt_output)
        print(f"📁 Output saved to {output}")

if __name__ == "__main__":
    analyze()
