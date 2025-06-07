import subprocess
import json
import os
from vertex_ai import generate  # 從你的 vertex_ai.py 匯入

before_sha = os.environ.get("CI_COMMIT_BEFORE_SHA", "")
after_sha = os.environ["CI_COMMIT_SHA"]
is_first_commit = before_sha == "0000000000000000000000000000000000000000"

# ❶ 取得變動檔案
modified_files_raw = subprocess.check_output(["python3", "get_diff.py"]).decode()


if not modified_files:
    print("No modified Python files.")
    exit(0)

modified_files = json.loads(modified_files_raw)

full_prompt = ""

# ❷ 組 prompt：完整 code 或 diff
for fname in modified_files:
    if is_first_commit:
        with open(fname, "r") as f:
            content = f.read()
        full_prompt += f"You are a senior Python software test engineer.\n"
        full_prompt += f"Please write unit tests using unittest for the following file:\n"
        full_prompt += f"### File: {fname}\n```python\n{content}\n```\n\n"
    else:
        file_diff = subprocess.check_output([
            "git", "diff", before_sha, after_sha, "--", fname
        ]).decode()
        full_prompt += f"You are a senior Python software test engineer.\n"
        full_prompt += f"Based on the following code changes, generate unit tests using unittest:\n"
        full_prompt += f"### File: {fname}\n{file_diff}\n\n"

# ❸ 呼叫 Vertex AI
print("📡 Sending prompt to Vertex AI...")
print("Prompt preview:\n" + full_prompt[:500] + "...\n")  # 前 500 字節預覽
print("🧪 Generating test script...\n")

# 這會直接印出 test script
generate(full_prompt)
