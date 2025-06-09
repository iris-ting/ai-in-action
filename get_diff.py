import subprocess
import os
import sys
import json

before_sha = os.environ.get("CI_COMMIT_BEFORE_SHA", "")
after_sha = os.environ["CI_COMMIT_SHA"]
is_first_commit = before_sha == "0000000000000000000000000000000000000000"

modified_files = []

if is_first_commit:
    all_files = subprocess.check_output(["find", ".", "-type", "f", "-name", "*.py"]).decode().splitlines()
    modified_files = all_files
else:
    diff_files = subprocess.check_output([
        "git", "diff", "--name-only", before_sha, after_sha
    ]).decode().splitlines()
    modified_files = [f for f in diff_files if f.endswith(".py")]

# 輸出 JSON 字串給後續使用（並排除不需測試的檔案）
excluded_files = {"generate_test_script.py", "get_diff.py", "vertex_ai.py"}

filtered = [f for f in modified_files if os.path.basename(f) not in excluded_files]

print(json.dumps(filtered))