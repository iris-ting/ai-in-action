# Multi-language version of test generation script.
# Detects file extension, assigns language and testing framework, sends proper prompt to Vertex AI.

import subprocess
import requests
import json
import sys
import os

endpoint = sys.argv[1]
test_file_path = sys.argv[2]

LANGUAGE_MAP = {
    ".py": ("Python", "pytest", "tests/test_generated.py"),
    ".js": ("JavaScript", "jest", "__tests__/generated.test.js"),
    ".ts": ("TypeScript", "jest", "__tests__/generated.test.ts"),
    ".java": ("Java", "JUnit", "test/GeneratedTest.java"),
    ".go": ("Go", "testing", "test/generated_test.go")
}

before_sha = os.environ.get("CI_COMMIT_BEFORE_SHA", "")
after_sha = os.environ["CI_COMMIT_SHA"]
is_first_commit = before_sha == "0000000000000000000000000000000000000000"

modified_files = []

if is_first_commit:
    print("🔧 First commit detected. Sending all supported code files.")
    all_files = subprocess.check_output(["find", ".", "-type", "f"]).decode().splitlines()
    modified_files = [f for f in all_files if os.path.splitext(f)[1] in LANGUAGE_MAP]
else:
    print("🔍 Diff-based commit detected.")
    diff_files = subprocess.check_output([
        "git", "diff", "--name-only", before_sha, after_sha
    ]).decode().splitlines()
    modified_files = [f for f in diff_files if os.path.splitext(f)[1] in LANGUAGE_MAP]

if not modified_files:
    print("No relevant files found.")
    exit(0)

full_prompt = ""
final_output_path = ""

for fname in modified_files:
    ext = os.path.splitext(fname)[1]
    language, framework, test_output = LANGUAGE_MAP[ext]
    final_output_path = test_output

    if is_first_commit:
        with open(fname, "r") as f:
            content = f.read()
        full_prompt += f"You are a senior {language} software test engineer.\n"
        full_prompt += f"Please write unit tests using {framework} for the following {language} file:\n"
        full_prompt += f"### File: {fname}\n```{language.lower()}\n{content}\n```\n\n"
    else:
        file_diff = subprocess.check_output([
            "git", "diff", before_sha, after_sha, "--", fname
        ]).decode()
        full_prompt += f"You are a senior {language} software test engineer.\n"
        full_prompt += f"Based on the following code changes, generate unit tests using {framework}:\n"
        full_prompt += f"### File: {fname}\n{file_diff}\n\n"

print("Sending prompt to GCP AI...")
response = requests.post(endpoint, json={"prompt": full_prompt})

if response.status_code != 200:
    print("❌ Error:", response.text)
    exit(1)

test_code = response.text.strip()

os.makedirs(os.path.dirname(final_output_path), exist_ok=True)
with open(final_output_path, "w") as f:
    f.write(test_code)

print(f"✅ Test script written to {final_output_path}")
