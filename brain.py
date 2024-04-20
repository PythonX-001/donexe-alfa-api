
# Python code for interacting with VisionCraft API
import requests, json
from groq import Groq
client = Groq(
    api_key="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",
)




def apiresponce(prompt):
  
  response = chat_completion = client.chat.completions.create(
    messages=prompt,
    model="mixtral-8x7b-32768",
)
  content = chat_completion.choices[0].message.content
  return content

