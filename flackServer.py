
import pymysql
from flask import Flask, jsonify, json
from flask import request


# import requests 아님

app = Flask(__name__)
# app.
db = pymysql.connect(host='localhost', port=3306, user='root', password='1234')  # in db
cursor = db.cursor()


@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/home")
def home():
    user = request.args.get("user", default="0")
    print(user)
    return "home Page"

@app.route("/getData")
def getData():
    typeData = request.args.get("type", default=None)
    selectSQL = "select * from crawler.musinsa_rank where `type` = %s"
    if type == None:
        return "no data", 400
    print(typeData)
    cursor.execute(selectSQL,(typeData))
    rows = cursor.fetchall()
    result = json.dumps(rows,ensure_ascii=False)
    return result

if __name__ == '__main__':
    app.run()