import requests
import subprocess
import os
import json
import sys


API_URL = "http://127.0.0.1:5000/api/gen_test"


# --helper functions------------------------------------------------------------
def clean_code_block(code_text):
    """
    Removes leading and trailing markdown-style code block markers.
    E.g. ```python\n<code>\n``` becomes <code>
    """
    # 清除開頭 ```python 或 ```，與結尾 ```
    lines = code_text.strip().splitlines()
    if lines and lines[0].strip().startswith("```"):
        lines = lines[1:]
    if lines and lines[-1].strip() == "```":
        lines = lines[:-1]
    return "\n".join(lines)
# --helper functions------------------------------------------------------------

def get_diff_files():
    try:
        output = subprocess.check_output(["python3", "get_diff.py"]).decode()
        modified_files = json.loads(output)

        if not modified_files:
            print("No modified Python files.")
            sys.exit(0)

        return modified_files

    except subprocess.CalledProcessError as e:
        print(f"Error calling get_diff.py: {e}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print("Failed to parse JSON output from get_diff.py")
        print("Raw output:\n", output)
        sys.exit(1)


def get_test_script(file_path):
    """
    Send a .py file's content to the test script generation API via form-data.
    
    Args:
        file_path (str): The path of the .py file to send.
    
    Returns:
        dict: {"html": str} if success, or {"error": str} if failed.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()

    response = requests.post(API_URL, json={
        "filename": file_path,
        "code": code
    })

    if response.status_code == 200:
        return {"response": response.text}
    else:
        return {"error": f"API Error {response.status_code}: {response.text}"}


def save_test_script(response_text, original_filename):
    """
    Save the Gemini response as a .py test file inside the generated_tests/ directory.
    """
    # Ensure output directory exists
    os.makedirs("generated_tests", exist_ok=True)

    base_name = os.path.basename(original_filename)
    name_without_ext = os.path.splitext(base_name)[0]
    test_filename = f"test_{name_without_ext}.py"

    output_path = os.path.join("generated_tests", test_filename)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(json.loads(response_text))

    print(f"Saved test file: {output_path}")


if __name__ == "__main__":
    files = get_diff_files()

    for file in files:
        print(f"📄 Generating test for: {file}")
        result = get_test_script(file)

        if "error" in result:
            print(f"❌ Failed for {file}: {result['error']}")
        else:
            save_test_script(result["response"], file)
