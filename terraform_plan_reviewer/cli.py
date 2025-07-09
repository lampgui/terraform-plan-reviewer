import click
from terraform_plan_reviewer.parser import extract_changes
from terraform_plan_reviewer.gpt import generate_summary
from terraform_plan_reviewer.printer import print_output

@click.command()
@click.argument("plan_file", type=click.Path(exists=True))
@click.option("--model", default="gpt-3.5-turbo", help="Model to use (e.g., gpt-3.5-turbo or gpt-4)")
@click.option("--provider", default="openai", type=click.Choice(["openai", "claude"]), help="LLM provider to use")
@click.option("--format", default="text", type=click.Choice(["text", "markdown", "json"]), help="Output format")
@click.option("--output", default=None, help="Save output to a file (e.g., summary.md)")
def analyze(plan_file, model, provider, format, output):
    """Analyze a Terraform plan JSON file using GPT or Claude."""
    print("🔍 Parsing Terraform plan...")
    change_summary = extract_changes(plan_file)

    print(f"🤖 Sending to {provider.upper()} for analysis...")
    gpt_output = generate_summary(change_summary, model=model, provider=provider)

    if not gpt_output:
        print("❌ GPT returned no output. Check your API key, usage limits, or provider settings.")
        return

    print_output(gpt_output, format=format)

    if output:
        with open(output, "w") as f:
            f.write(gpt_output)
        print(f"📁 Output saved to {output}")

if __name__ == "__main__":
    analyze()
