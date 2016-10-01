from flask import Flask
from  flask import jsonify
from flask import render_template
import pymongo

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/index/')
def index():
    name = "World"
    return render_template('index.html', name=name)


@app.route('/index/second/')
def second():
    print('index/second')
    db = pymongo.MongoClient("localhost", 27017).snail
    cursor = db.restaurants.find()
    result = []
    for document in cursor:
        result.append(document)
    return jsonify(result)
