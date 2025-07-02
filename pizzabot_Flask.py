# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 17:08:48 2025

@author: mahee
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from pizzabot_Logic import get_response

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json.get('message')
    reply = get_response(message)
    return jsonify({'response': reply})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)

