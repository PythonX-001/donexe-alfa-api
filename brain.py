
# Python code for interacting with VisionCraft API
import requests, json




def apiresponce(prompt):
  response = requests.post(
    url="https://api.visioncraft.top/llm",
    data=json.dumps({
      "token": "546197d1-5b74-4f3e-abf1-46210d603801",
      "model": "Mixtral-8x7B-Instruct-v0.1",
      "messages": prompt
    })
  )
  content = response.json()['choices'][0]['message']['content']
  return content

