import subprocess
import json
import os
from vertex_ai import generate  # 從你的 vertex_ai.py 匯入

# ---- helper function ----

# ❶ 取得變動檔案
def get_diff_files():
    modified_files_raw = subprocess.check_output(["python3", "get_diff.py"]).decode()
    modified_files = json.loads(modified_files_raw)
    if not modified_files:
        print("No modified Python files.")
        exit(0)

def read_file(filepath):
    with open(filepath, "r") as f:
        return f.read()

def save_test_file(original_file, test_code):
    test_dir = "tests"
    os.makedirs(test_dir, exist_ok=True)
    test_filename = f"test_{os.path.basename(original_file)}"
    with open(os.path.join(test_dir, test_filename), "w") as f:
        f.write(test_code)
    print(f"✅ Test file saved: {test_dir}/{test_filename}")


full_prompt = ""

# ❷ 組 prompt：完整 code 或 diff
changed_files = get_diff_files()

for file in changed_files:
    code = read_file(file)
    prompt = (
        "You are a senior Python software test engineer.\n"
        "Please write unit tests using the unittest framework.\n"
        "Only return Python code and explain the test strategy using the comment format in the beginning of py file.\n"
        f"Here is the code to test (from {file}):\n{code}"
    )

    # ❸ 呼叫 Vertex AI
    print("📡 Sending prompt to Vertex AI...")
    test_script = generate(prompt)
    save_test_file(file, test_script)
