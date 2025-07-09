import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_summary(change_summary, model="gpt-3.5-turbo"):
    prompt = f"""
Here is a Terraform plan summary:

{change_summary}

Please:
1. Summarize what infrastructure is changing in plain English.
2. Highlight any potential risks (e.g. deletions, downtimes, public IPs).
3. List what a reviewer should double-check before approval.
"""
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are an expert DevOps reviewer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4
    )

    return response.choices[0].message.content
