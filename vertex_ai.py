from google import genai
from google.genai import types
import base64

prompt="Please write a Python unit test for an addition function that takes two integers and returns their sum. The test should include cases for positive numbers, negative numbers, and zero. Use the unittest framework."

def generate(text):
  client = genai.Client(
      vertexai=True,
      project="iristest-462021",
      location="global",
  )


  model = "gemini-2.5-pro-preview-06-05"
  contents = [
    types.Content(
      role="user",
      parts=[{"text": text}]
    )
  ]

  generate_content_config = types.GenerateContentConfig(
    temperature = 1,
    top_p = 1,
    seed = 0,
    max_output_tokens = 65535,
    safety_settings = [types.SafetySetting(
      category="HARM_CATEGORY_HATE_SPEECH",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_DANGEROUS_CONTENT",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_HARASSMENT",
      threshold="OFF"
    )],
  )

  for chunk in client.models.generate_content_stream(
    model = model,
    contents = contents,
    config = generate_content_config,
    ):
    print(chunk.text, end="")

generate(prompt)