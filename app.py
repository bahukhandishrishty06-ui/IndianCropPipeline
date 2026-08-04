from flask import Flask, render_template, request, jsonify
import pandas as pd
import os

app = Flask(__name__, static_folder='static')
DATASET_PATH = 'India_Districts_Crop_Production_Processed.csv'

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
