import pymongo
from flask import Flask, render_template, jsonify
from bson.json_util import dumps
from config import USER, PASSWORD
import pandas as pd

conn = f'mongodb+srv://{USER}:{PASSWORD}@weatherviz-andy-5dubo.mongodb.net/gtds_p3?retryWrites=true'
client = pymongo.MongoClient(conn)
db = client.weatherviz
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=False)
