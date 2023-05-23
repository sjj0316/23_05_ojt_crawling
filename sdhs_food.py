import requests

# pip install urllib3==1.26.6

data = {"mlsvId": 226050}
response = requests.post(
    "https://sdh.sen.hs.kr/dggb/module/mlsv/selectMlsvDetailPopup.do",
    data=data)
print(response.text)
