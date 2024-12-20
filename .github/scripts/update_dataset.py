import os
import json
from datetime import datetime
from datasets import load_dataset

# Load GitHub event data
with open(os.getenv('GITHUB_EVENT_PATH')) as f:
    event = json.load(f)

issue_body = event['issue']['body']
username = event['issue']['user']['login']
datetime_str = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

# Extract data from issue body
def extract_section(section_name):
    start_marker = f"### {section_name}"
    end_marker = "###"
    start_index = issue_body.find(start_marker) + len(start_marker)
    end_index = issue_body.find(end_marker, start_index)
    return issue_body[start_index:end_index].strip()

query = extract_section("Query")
model_response = extract_section("Model Response")
model = extract_section("Model Name")
user_response = extract_section("Correct Response")

# Create new entry
new_entry = {
    "query": query,
    "model_response": model_response,
    "model": model,
    "user_response": user_response,
    "user": f"@{username}",
    "datetime": datetime_str
}

# Append to dataset.jsonl
with open('dataset.jsonl', 'a', encoding="utf-8") as f:
    f.write(json.dumps(new_entry, ensure_ascii=False) + '\n')

# Commit and push changes
os.system('git config user.name "github-actions[bot]"')
os.system('git config user.email "github-actions[bot]@users.noreply.github.com"')
os.system('git remote set-url origin https://${{ secrets.GITHUB_TOKEN }}@github.com/${{ github.repository }}.git')
os.system('git add dataset.jsonl')
os.system(f'git commit -m "Update dataset with new issue #{event["issue"]["number"]}"')
os.system('git push')

# Push to Hugging Face
dataset = load_dataset("json", data_files="dataset.jsonl", split="train")
dataset.push_to_hub("Ki-Seki/llm-failure-dataset")
