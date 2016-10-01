from flask import Flask
from  flask import jsonify
from flask import render_template
import pymongo

app = Flask(__name__)


@app.route("/")
@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/index/second/')
def second():
    db = pymongo.MongoClient("localhost", 27017).snail
    cursor = db.restaurants.find()
    result = []
    for document in cursor:
        result.append(document)
    return jsonify(result)
