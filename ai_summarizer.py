import openai
import os
import sys

# Get the plan from a text file generated in the workflow
with open("plan_output.txt", "r") as f:
    plan_text = f.read()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-5.2", # Use the latest 2026-standard model
    messages=[
        {"role": "system", "content": "You are a Senior Platform Architect. Summarize this Terraform plan for a non-technical manager."},
        {"role": "user", "content": f"Analyze this plan and provide: 1. Risk Level (Low/Med/High), 2. Resource count changes, 3. Critical warnings: \n\n{plan_text[:4000]}"}
    ]
)

print(response.choices[0].message.content)
