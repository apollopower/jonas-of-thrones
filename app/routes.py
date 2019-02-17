from app import app
from flask import request, jsonify

from api.api_caller import *

@app.route('/')
def index():
    return "WELCOME to JONAS OF THRONES! Search with the '/image?name=' query to get back a image URL for your character" 

@app.route('/image', methods=['GET'])
def get_image():
    char_name = request.args.get("name")
    print(char_name)
    response = {}
    response['image'] = get_GOT_char(char_name)
    print(response)
    return jsonify(**response)