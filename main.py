from flask import Flask,request
from collections import namedtuple
from brain import apiresponce

app = Flask(__name__)

@app.route('/')
def index():
    return  '<h1>hi bro</h1>'

Response = namedtuple('Response', 'response accuracy')

@app.route('/apitext')

def api():
    user_input = request.args.get('input')
    response = generate_response(user_input)

    json = {
        'input': user_input,
        'response': response.response
    }

    return json

def generate_response(user_input:str) -> Response:
    lc_input = user_input.lower()

    return Response(who_created_me(lc_input),1)



@app.route('/apitext')

def theapi():
    user_input = request.args.get('input')
    response = generate_response(user_input)

    json = {
        'input': user_input,
        'response': response.response
    }

    return json

def generate_response(user_input:str) -> Response:
    lc_input = user_input.lower()

    return Response(apiresponce(lc_input),1)





if __name__ == '__main__':
  app.run(port=5000)  
