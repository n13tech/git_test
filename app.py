from flask import Flask
app = Flask(__name__)
from utils import dad_joke

@app.route('/')
def hello_world():
    
    return dad_joke()
