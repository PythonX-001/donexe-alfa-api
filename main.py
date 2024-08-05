from flask import Flask, request, jsonify
from flask_cors import CORS

from brain import apiresponce

app = Flask(__name__)
CORS(app)
@app.route('/')
def index():
    return  '<h1>hi bro</h1>'

@app.route('/chatbot',  methods=["POST", "GET"])
def chatbot():
    # Get the user's message from the request
    data = request.get_json()
    user_message = data.get('message')
    token = data.get('token')
    
    # Here you would add the logic to process the user's message and generate a response
    # For demonstration purposes, we'll just echo the message back
    bot_response = apiresponce(user_message , token)
    
    # Return the response as JSON
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
