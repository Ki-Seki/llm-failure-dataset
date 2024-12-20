# LLM Failure Dataset

This repository collects and curates a dataset of failure cases from large language models (LLMs).

## Dataset Description

The dataset is stored in `.jsonl` format with the following columns:

- **query**: The user input to the LLM.
- **model_response**: The incorrect or undesired response generated by the LLM.
- **model**: The name of the LLM (e.g., GPT-4, Claude).
- **user_response**: The correct or expected response provided by the user.
- **user**: The GitHub username of the contributor.
- **datetime**: The UTC timestamp when the entry was submitted.

### Example Entry

```json
{
  "query": "Strawberry 中有几个 r ？",
  "model_response": "\"Strawberry\" 中有两个 **r**。",
  "model": "GPT-4o mini",
  "user_response": "\"Strawberry\" 中有 **3 个字母 r**。",
  "user": "@Ki-Seki",
  "datetime": "2024-12-20T05:52:54Z"
}
```

## How to Contribute

We welcome contributions from the community! If you encounter a failure case, follow these steps to submit it:

1. Open a [new issue](https://github.com/Ki-Seki/llm-failure-dataset/issues/new?template=new-failure.yml).
2. Fill out the provided YAML form with the details of the failure case:
   - **Query**: The input you provided to the LLM.
   - **Model Response**: The incorrect or bad response.
   - **Model Name**: The name of the LLM used.
   - **Correct Response**: Your expected or correct response.

Once you submit, the dataset will be automatically updated via GitHub Actions, and your entry will be added to the dataset.

## Automated Workflow

This repository uses GitHub Actions to streamline the contribution and update process:

1. **Submit an Issue**: Contributors submit new cases via GitHub Issues.
2. **Update Dataset**: Each new issue triggers an action to append the data to `dataset.jsonl`.
3. **Push to Hugging Face**: The updated dataset is automatically pushed to [Hugging Face Datasets](https://huggingface.co/).

## Dataset Access

The dataset is hosted on Hugging Face and can be accessed at:

[🔗 LLM Failure Dataset on Hugging Face](https://huggingface.co/datasets/Ki-Seki/llm-failure-dataset)

You can load the dataset in Python using the `datasets` library:

```python
from datasets import load_dataset

dataset = load_dataset("Ki-Seki/llm-failure-dataset")
```
