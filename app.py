from flask import Flask, jsonify, request
from flask_cors import CORS # type: ignore

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 1