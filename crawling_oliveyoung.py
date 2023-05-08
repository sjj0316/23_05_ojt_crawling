#pip install beautifulsoup4
#pip install requests

import requests
import bs4
from bs4 import BeautifulSoup


def main():
    url = "https://www.oliveyoung.co.kr/store/main/getHotdealPagingListAjax.do?date=20230508&pageIdx=1&fltCondition=02&fltDispCatNo=&prdSort=rank"
    data = requests.get(url)

    if data.status_code == 200:
        soup = bs4.BeautifulSoup(data.text, "html.parser")
        prodList = soup.find_all("li")
        for product in prodList:
            print(product.find("img")["src"])
            print(product.select_one(".Pnum").text)
            print(product.select_one(".prod-name").text)
            print(product.select_one(".total").text)
            print("--------------------------------")

if __name__ == '__main__':
    main()