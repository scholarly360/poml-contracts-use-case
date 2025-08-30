
# Env vars:

# AZURE_OPENAI_API_KEY=ddddddsamplelllllllllll
# AZURE_OPENAI_API_VERSION=2024-08-01-preview
# AZURE_OPENAI_ENDPOINT=https:endpoint
# AZURE_MODEL=gpt-4o-mini

import os, glob, json, re, pathlib, sys
import poml
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
DEPLOYMENT = os.getenv("AZURE_OPENAI_API_VERSION")
AZURE_MODEL = os.getenv("AZURE_MODEL")
OUT_DIR = pathlib.Path(os.getenv("OUTPUT_DIR", "./outputs"))
PROMPTS_DIR = pathlib.Path(os.getenv("PROMPTS_DIR", "./prompts"))

if not API_KEY or not ENDPOINT or not DEPLOYMENT:
    print("ERROR: Please set AZURE_OPENAI_API_KEY, AZURE_OPENAI_ENDPOINT, and AZURE_OPENAI_API_VERSION.", file=sys.stderr)
    sys.exit(1)

client = OpenAI(
    api_key=API_KEY,
    base_url=(ENDPOINT.rstrip('/') + "/openai/v1/"),
)

OUT_DIR.mkdir(parents=True, exist_ok=True)

results = []
for path in sorted(PROMPTS_DIR.glob("*.poml")):
    messages_and_params = poml.poml(str(path), context={"doc_path": "../sample_contract.pdf"}, format="openai_chat")
    rules_response = client.chat.completions.create(**messages_and_params, model=AZURE_MODEL)
    results.append(json.loads(rules_response.choices[0].message.content))
print('#################')
with open("output.json", "w") as json_file:
    json.dump(results, json_file)
