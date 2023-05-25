
import pymysql
from flask import Flask, jsonify, json
from flask import request
from flask_cors import CORS
import requests
# pip install urllib3==1.26.6
from bs4 import BeautifulSoup
import datetime


# import requests 아님

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False


@app.route("/")
def hello_world():
    return "Hello World"


@app.route("/food")
def food():
    flag = True
    count = 0
    id = 2260500
    while flag and count < 10:
        data = {"mlsvId": str(id)}
        response = requests.post(
            "https://sdh.sen.hs.kr/dggb/module/mlsv/selectMlsvDetailPopup.do",
            data=data)

        soup = BeautifulSoup(response.text, "html.parser")
        foodDate = soup.select(".ta_l")[1].text.strip()
        dateList = foodDate.split(" ")
        dateList[0] = dateList[0].replace("년", "")
        dateList[1] = dateList[1].replace("월", "")
        if dateList[1][0] == "0":
            dateList[1][0].replace("0", "")

        dateList[2] = dateList[2].replace("일", "")
        dateList.pop()
        dateResult = datetime.date(int(dateList[0]), int(dateList[1]), int(dateList[2]))
        testdate = datetime.datetime.now().date()
        print(testdate)
        # dateObject = datetime.date(2023, 5, 25)
        if dateResult == testdate:
            food = soup.select(".ta_l")[3].text.strip()
            result = {"food": food}
            return json.dumps(result, ensure_ascii=False)
            flag = False
        else:
            # print(dateResult)
            # print(dateObject)
            # print(id)
            id += 1
            count += 1


@app.route("/foodTest")
def foodTest():
    data = {"food": "칼슘찹쌀밥, 뼈없는감자탕(수제비), 아구까스&카사바칩&매콤마요소스, 계란부추짜박이, 궁채들깨볶음, 깍두기"}
    return json.dumps(data, ensure_ascii=False)


if __name__ == '__main__':
    app.run()