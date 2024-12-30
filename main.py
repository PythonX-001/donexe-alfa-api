from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from groq import Groq

client = Groq(api_key="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")

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return '<h1>hi bro</h1>'

@app.route('/chatbot', methods=["POST", "GET"])
def chatbot():
    try:
        data = request.get_json()
        if not data or 'message' not in data or 'token' not in data:
            return jsonify({'error': 'Invalid request payload'}), 400
        
        user_message = data.get('message')
        token = int(data.get('token'))
        

        print(f"User message: {user_message}")
        print(f"Token adjustment: {number}")
        
        # Ensure `user_message` is in the correct format
        if not isinstance(user_message, list):
            return jsonify({'error': 'Message must be a list of dictionaries'}), 400

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
        return jsonify({'response': bot_response})
    
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'An internal server error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True)
