import requests
# pip install urllib3==1.26.6
from bs4 import BeautifulSoup
import datetime
id = 2260500
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
        dateList[1][0].replace("0","")

    dateList[2] = dateList[2].replace("일", "")
    dateList.pop()
    dateResult = datetime.date(int(dateList[0]), int(dateList[1]), int(dateList[2]))
    testdate = datetime.datetime.now().date()
    # print(testdate)
    dateObject = datetime.date(2023,5,23)
    # print(dateObject)
    if dateResult == testdate:
        food = soup.select(".ta_l")[3].text.strip()
        print(food)
        flag = False

    else:
        print(dateResult)
        print(testdate)
        print(id)
        id += 1