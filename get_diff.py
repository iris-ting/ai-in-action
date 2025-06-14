import subprocess
import os
import sys
import json

before_sha = os.environ.get("CI_COMMIT_BEFORE_SHA", "0000000000000000000000000000000000000000")
after_sha = os.environ.get("CI_COMMIT_SHA", "8622b5a795a8aa5f66f5aa3c0db0ebcf17124ce0")
is_first_commit = before_sha == "0000000000000000000000000000000000000000"

excluded_files = {"generate_test_script.py", "get_test_script.py", "get_diff.py", "vertex_ai.py", "temp.py"}
excluded_dirs = {"generated_tests", "google-cloud-sdk"}

# def is_excluded(filepath):
#     basename = os.path.basename(filepath)
#     return (
#         basename in excluded_files
#         or any(filepath.startswith(f"{d}/") for d in excluded_dirs)
#     )
def is_excluded(filepath):
    filepath = os.path.normpath(filepath)
    basename = os.path.basename(filepath)
    return (
        basename in excluded_files or
        any(filepath.startswith(os.path.join(d, "")) for d in excluded_dirs)
    )

modified_files = []

if is_first_commit:
    all_files = subprocess.check_output(["find", ".", "-type", "f", "-name", "*.py"]).decode().splitlines()
    modified_files = [f for f in all_files if not is_excluded(f)]
else:
    diff_files = subprocess.check_output([
        "git", "diff", "--name-only", before_sha, after_sha
    ]).decode().splitlines()
    modified_files = [f for f in diff_files if f.endswith(".py") and not is_excluded(f)]


print(json.dumps(modified_files))

# with open("modified_files.json", "w", encoding="utf-8") as f:
#     json.dump(modified_files, f)
