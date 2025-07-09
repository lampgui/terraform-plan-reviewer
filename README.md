# Terraform Plan Reviewer (CLI)

🔍 GPT-powered CLI tool that summarizes and reviews Terraform plan JSON files.

## Features
- AI-generated summaries of infra changes
- Risk callouts (e.g. deletions, replacements)
- Reviewer checklist suggestions

## Usage

1. Generate a Terraform plan JSON:
```bash
terraform plan -out=tfplan.binary
terraform show -json tfplan.binary > tfplan.json
