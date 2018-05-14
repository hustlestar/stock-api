import os

from flask import Flask
from main import test_plotting
from utils import read_properties

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/plot')
def get_ticker():
    secrets_path = '../secrets/credentials.properties'
    secrets_path = os.path.normpath(secrets_path)
    props = read_properties(secrets_path)
    return test_plotting(props)

if __name__ == '__main__':
    app.run(debug=True)