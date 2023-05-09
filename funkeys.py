import bs4
import requests
from bs4 import BeautifulSoup

# selenium X
def main():
    url = "https://funkeys.co.kr/shop/list.php?ca_id=10"
    response = requests.get(url)
    if response.status_code == 200:
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        productList = soup.select(".item-list")
        for item in productList:
            title = item.select_one(".title").text.strip()
            sale = item.select_one(".dcView").text.strip()
            # print(title.strip())
            switchOption = item.select(".switchop")
            # print(len(switchOption))
            for option in switchOption:
                switch = option.select_one(".optTitle").text
                price = option.select_one(".pull-right").text
                print(title, sale, switch, price)


if __name__ == "__main__":
    main()
