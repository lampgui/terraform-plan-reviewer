import os
import httpx
from dotenv import load_dotenv

load_dotenv()

def generate_summary(change_summary, model="gpt-3.5-turbo", provider="openai"):
    prompt = f"""
Here is a Terraform plan summary:

{change_summary}

Please:
1. Summarize what infrastructure is changing in plain English.
2. Highlight any potential risks (e.g. deletions, downtimes, public IPs).
3. List what a reviewer should double-check before approval.
"""

    try:
        if provider == "claude":
            return run_claude(prompt)

        from openai import OpenAI
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("❌ OPENAI_API_KEY is not set in your environment.")

        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are an expert DevOps reviewer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4
        )

        print("✅ GPT response received.")
        print("✏️  Raw response content:")
        print(response.choices[0].message.content)

        return response.choices[0].message.content

    except Exception as e:
        print(f"❌ GPT request failed: {e}")
        return None

def run_claude(prompt):
    api_key = os.getenv("TOGETHER_API_KEY")
    if not api_key:
        raise ValueError("❌ TOGETHER_API_KEY is not set in your environment.")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "claude-3-sonnet-20240229",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 1000
    }

    try:
        response = httpx.post("https://api.together.xyz/v1/chat/completions", headers=headers, json=data)
        response.raise_for_status()
        print("✅ Claude response received.")
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"❌ Claude request failed: {e}")
        return None
