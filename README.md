# 🚀 Terraform Plan Reviewer CLI

A GPT-powered CLI tool that summarizes and reviews Terraform plans in plain English.

---

## 🧠 What It Does

- Parses `terraform show -json` plan files
- Uses GPT to generate:
  - Change summaries
  - Risk callouts (deletes, downtimes, replacements)
  - Reviewer checklists
- Outputs in text, Markdown, or JSON
- Works entirely from the command line

---

## 🛠 Installation

**Option 1: Clone & install locally**
```bash
git clone https://github.com/your-username/terraform-plan-reviewer.git
cd terraform-plan-reviewer
python3 -m venv venv && source venv/bin/activate
pip install -e .
```

**Option 2: Install dependencies manually**
```bash
pip install -r requirements.txt
```

---

## ⚙️ Usage

Generate your Terraform plan in JSON:
```bash
terraform plan -out=tfplan.binary
terraform show -json tfplan.binary > tfplan.json
```

Run the reviewer:
```bash
tf-reviewer tfplan.json
```

With options:
```bash
tf-reviewer tfplan.json --model gpt-3.5-turbo --format markdown --output summary.md
```

---

## 🔐 Setup `.env`

Create a `.env` file in the project root:
```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## 📸 Example Output

```
1. ✅ A new resource group named `main` will be created.
2. 🛑 A storage account named `data` will be deleted and recreated.
3. 🔄 A virtual machine will be resized from Standard_B2s to Standard_B4ms.

⚠️ Review risks: data loss, public IP exposure, possible downtime.
```

---

## 💡 Roadmap

- [ ] GitHub PR bot integration
- [ ] Infracost cost estimation support
- [ ] VS Code extension
- [ ] Optional Web UI frontend

---

## 🙌 Contributing

Pull requests and feedback are welcome!  
Please open an issue or fork the project and submit a PR.

---

## 📝 License

[MIT](LICENSE)
