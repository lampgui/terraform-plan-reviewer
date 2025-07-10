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
✅ GPT response received.

1. **Infrastructure Changes Summary:**
   - A new Azure resource group named `main` will be created.
   - A new public IP named `web_ip` will be created.
   - An existing virtual machine named `vm1` will be updated.
   - An existing storage account named `data` will be deleted and recreated, which requires replacement.

2. **Potential Risks:**
   - The recreation of the `azurerm_storage_account.data` may lead to data loss if not handled properly.
   - Any changes to the `azurerm_virtual_machine.vm1` may cause downtime if not managed carefully.
   - The creation of a new public IP `web_ip` may expose services to the public internet, potentially introducing security risks.

3. **Double-Check Before Approval:**
   - Verify if any critical data is stored in the `azurerm_storage_account.data` that needs to be backed up before deletion.
   - Ensure that any updates to `azurerm_virtual_machine.vm1` are thoroughly tested in a non-production environment to mitigate downtime risks.
   - Review the security settings of the new public IP `web_ip` to ensure that only necessary services are exposed to the internet and proper security measures are in place.
   - Confirm that all dependencies and configurations related to the changes are accurately reflected in the Terraform plan.

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
