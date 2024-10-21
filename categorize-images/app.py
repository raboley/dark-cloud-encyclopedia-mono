from flask import Flask, jsonify, request
import requests
import json

app = Flask(__name__)

# books = [
#     {
#         'name': 'Green egges and Ham',
#         'price': 7.99,
#         'isbn': 1234,
#     },
#     {
#         'name': 'The cat in the hat',
#         'price': 6.99,
#         'isbn': 5678,
#     }
# ]

# @app.route('/books')
# def get_books():
#     return jsonify({'books': books})

@app.route('/steal')
def get_books_from_other_place():
    book = requests.get('http://127.0.0.1:5001/books?isbn=1234').content
    json_decoded_from_bytes = book.decode('utf8').replace("'", '"')
    response = json.loads(json_decoded_from_bytes)
    return jsonify(response)

app.run(port=5001,debug=True)
