import subprocess
import os
import sys
import json

before_sha = os.environ.get("CI_COMMIT_BEFORE_SHA", "")
after_sha = os.environ["CI_COMMIT_SHA"]
is_first_commit = before_sha == "0000000000000000000000000000000000000000"

modified_files = []

if is_first_commit:
    print("🔧 First commit detected. Listing all .py files.")
    all_files = subprocess.check_output(["find", ".", "-type", "f", "-name", "*.py"]).decode().splitlines()
    modified_files = all_files
else:
    print("🔍 Diff-based commit detected.")
    diff_files = subprocess.check_output([
        "git", "diff", "--name-only", before_sha, after_sha
    ]).decode().splitlines()
    modified_files = [f for f in diff_files if f.endswith(".py")]

# 輸出 JSON 字串給後續使用
print(json.dumps(modified_files))
