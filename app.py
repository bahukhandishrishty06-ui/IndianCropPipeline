# Indian Crop Pipeline App
from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
