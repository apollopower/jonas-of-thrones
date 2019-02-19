from app import app
from flask import request, jsonify

from api.api_caller import *

@app.before_first_request
def _load_main_chars():
    main_chars = ['Jon Snow', 'Daenerys Targaryen', 'Arya Stark', 'Brandon Stark', 'Catelyn Stark','Cersei Lannister', 'Eddard Stark', 'Jaime Lannister', 'Melisandre', 'Petyr Baelish', 'Ramsay Snow', 'Samwell Tarly', 'Sandor Clegane', 'Sansa Stark', 'Theon Greyjoy', 'Tyrion Lannister', 'Daario Naharis', 'Jorah Mormont']
    global main_chars_result
    main_chars_result = []
    
    for char in main_chars:
        char_obj = {}
        char_obj['name'] = char
        char_obj['image'] = get_GOT_char(char)

        main_chars_result.append(char_obj)

@app.route('/')
def index():
    return "WELCOME to JONAS OF THRONES! Search with the '/image?name=' query to get back a image URL for your character" 

@app.route('/image', methods=['GET'])
def get_image():
    char_name = request.args.get("name")
    print(char_name)
    response = {}
    response['name'] = char_name
    response['image'] = get_GOT_char(char_name)
    print(response)
    return jsonify(**response)

@app.route('/characters', methods=['GET'])
def get_main_chars():
    response = {}
    response['characters'] = main_chars_result
    return jsonify(**response)