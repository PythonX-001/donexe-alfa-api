from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from brain import apiresponce
from groq import Groq
client =  Groq(api_key="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")


app = Flask(__name__)
CORS(app)
@app.route('/')
def index():
    return  '<h1>hi bro</h1>'

@app.route('/chatbot',  methods=["POST", "GET"])
def chatbot():
    data = request.get_json()
    user_message =data.get('message')
    print(user_message)
    token = data.get('token')
    token = int(token)  
    number = token - 800
    print (number)
    completion = client.chat.completions.create(
        model="gemma2-9b-it",
        messages=user_message,
        temperature=1,
        max_tokens=token,
        top_p=1,
        stream=False,
        stop=None,
    )

    bot_response = completion.choices[0].message.content
    # Get the user's message from the request

    
    # Here you would add the logic to process the user's message and generate a response
    # For demonstration purpjsonify(user_message)oses, we'll just echo the message backjsonify(user_message)
    
    # Return the response as JSON
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
