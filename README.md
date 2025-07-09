# Terraform Plan Reviewer

A CLI tool that parses a Terraform plan JSON and uses an LLM (GPT or Claude) to provide a human-readable summary, highlight risks, and suggest review steps.

---

## 🚀 Features

- 🧠 Summarizes Terraform infrastructure changes using LLMs
- 📛 Identifies potential risks (e.g. downtime, deletion, public exposure)
- ✅ Lists items to double-check before approval
- 🛠 Supports **OpenAI GPT** and **Anthropic Claude** (via Together API)
- 🖥️ Output formats: text, markdown, or JSON
- 📂 Optional output to file

---

## 🛠 Installation

```bash
git clone https://github.com/lampgui/terraform-plan-reviewer.git
cd terraform-plan-reviewer
python3 -m venv venv
source venv/bin/activate
pip install -e .
```

---

## 🔑 API Keys

Create a `.env` file in the root:

```env
OPENAI_API_KEY=sk-...
TOGETHER_API_KEY=...
```

---

## 🧪 Example Usage

```bash
tf-reviewer examples/sample_plan.json --model gpt-3.5-turbo --format markdown
```

Use Claude:

```bash
tf-reviewer examples/sample_plan.json --provider claude --format text
```

Save output:

```bash
tf-reviewer examples/sample_plan.json --output summary.md
```

---

## 🧾 Output Example

```
🔍 Parsing Terraform plan...
🤖 Sending to OPENAI for analysis...

1. **Changes Summary**:
   - Create RG: `main`
   - Update VM: `vm1`
   - Recreate storage: `data`

2. **Risks**:
   - Downtime on VM
   - Potential data loss on storage replace
   - Public IP exposure

3. **Double Check**:
   - Backups for `data`
   - Maintenance window for `vm1`
   - NSG rules on public IP
```

---

## 📂 Project Structure

```
terraform_plan_reviewer/
├── cli.py
├── gpt.py
├── parser.py
├── printer.py
examples/
├── sample_plan.json
pyproject.toml
README.md
```

---

## 🔍 Troubleshooting

- `ModuleNotFoundError`: Ensure all `.py` files are in the `terraform_plan_reviewer/` folder.
- `No output`: Check `.env` is set and API keys are valid.
- `tf-reviewer not found`: Did you run `pip install -e .`?

---

## 📝 License

MIT
