
# Python code for interacting with VisionCraft API
import requests, json
from groq import Groq
client =  Groq(api_key="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")




def apiresponce(prompt, token):
  
    completion = qclient.chat.completions.create(
        model="gemma2-9b-it",
        messages=prompt,
        temperature=1,
        max_tokens=token,
        top_p=1,
        stream=False,
        stop=None,
    )

    return completion.choices[0].message.content



