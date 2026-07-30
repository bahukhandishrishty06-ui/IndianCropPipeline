# Indian Crop Pipeline App
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_folder='static')

if __name__ == '__main__':
    app.run(debug=True)
