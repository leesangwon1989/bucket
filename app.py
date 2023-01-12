from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from flask_socketio import SocketIO, send
import bcrypt

app = Flask(__name__)

client = MongoClient('mongodb+srv://test:sparta@cluster0.a1shctu.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/bucket", methods=["POST"])
def bucket_post():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg': 'POST(기록) 연결 완료!'})

@app.route("/bucket/done", methods=["POST"])
def bucket_done():
    bucket_receive = request.form['bucket_give']

    bucket_list = list(db.users.find({}, {'_id': False}))
    count = len(bucket_list)

    )

    doc = {
        'bucket':bucket_receive,
        'num':count,
        'deon':0

    }
    db.bucket.insert_one(doc)

    print(sample_receive)
    return jsonify({'msg': 'POST(완료) 연결 완료!'})

@app.route("/bucket", methods=["GET"])
def bucket_get():
    return jsonify({'msg': 'GET 연결 완료!'})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)