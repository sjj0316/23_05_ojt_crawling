import requests
import xmltodict
# pip install xmltodict
# 03Busapitest

from urllib.parse import urlparse, parse_qs, urlencode

url = "http://ws.bus.go.kr/api/rest/stationinfo/getStationByUid?serviceKey=DRr3Z3dZJqdLd1GnvsPNnStHUzR8%2Bh0eouQ%2Fkdw8IZJaS8cBCDYdPHNKPkFPTN%2F2Zrkr71sWx2WEP3nf3myURA%3D%3D&arsId=03567"
print(parse_qs(urlparse(url).query))

arsid = input()
url2 = "http://ws.bus.go.kr/api/rest/stationinfo/getStationByUid?"

params = {'serviceKey': 'DRr3Z3dZJqdLd1GnvsPNnStHUzR8+h0eouQ/kdw8IZJaS8cBCDYdPHNKPkFPTN/2Zrkr71sWx2WEP3nf3myURA==',
          'arsId': arsid}

resURL = url2+urlencode(params)
resource = requests.get(resURL)
# print(resource.text)
result = xmltodict.parse(resource.text)
items = result['ServiceResult']['msgBody']['itemList']
if type(items) == list:
    for item in items:
        rtNM = item['rtNm']
        arrMsg1 = item['arrmsg1']
        arrMsg2 = item['arrmsg2']
        print(rtNM, '/', arrMsg1, '/', arrMsg2)
else:
    item = result['ServiceResult']['msgBody']['itemList']
    rtNM = item['rtNm']
    arrMsg1 = item['arrmsg1']
    arrMsg2 = item['arrmsg2']
    print(rtNM, '/', arrMsg1, '/', arrMsg2)

# arrMsg1 = item['arrmsg1']
# arrMsg2 = item['arrmsg2']
# print(arrMsg1, '/', arrMsg2)