from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import NoSuchElementException
import time
import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', password='1234')  # in db
cursor = db.cursor()
insertSQL = "INSERT INTO crawler.kream_url (URL, product_id) VALUES(%s, %s);"


option = options.Options()
option.add_experimental_option('detach', True)
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=option)


def get_data():
    selectSQL = "SELECT URL, product_id, flag FROM " \
                "crawler.kream_url where flag = 'N';"
    updateFlagSQL = "UPDATE crawler.kream_url SET flag='Y' WHERE product_id=%s;"
    insertProductSQL = "INSERT INTO crawler.kream_data " \
                       "(productId, brand, name, subName, price, url, releaseDate, color, originPrice, modelNum) " \
                       "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    cursor.execute(selectSQL)
    rows = cursor.fetchall()
    for i in rows:
        driver.get(i[0])
        time.sleep(3)
        box = driver.find_element(By.CLASS_NAME, "main_title_box")
        name = box.find_element(By.CLASS_NAME, "title").text
        print(name)
        image = driver.find_element(By.CLASS_NAME, "item_inner") \
            .find_element(By.TAG_NAME, "img").get_attribute("src")
        if image == "https://kream.co.kr/images/common_thumbs_blank_L.png?type=l":
            driver.refresh()
            continue;

        brand = box.find_element(By.CLASS_NAME, "brand").text
        subname = box.find_element(By.CLASS_NAME, "sub_title").text
        priceBox = driver.find_element(By.CLASS_NAME, "detail_price")
        price = priceBox.find_element(By.CLASS_NAME, "num").text
        # print(brand,name,subname,price)
        detailBox = driver.find_elements(By.CLASS_NAME, 'detail_box')
        modelNum = detailBox[0].find_element(By.CLASS_NAME, "product_info").text
        releaseDate = detailBox[1].find_element(By.CLASS_NAME, "product_info").text
        color = detailBox[2].find_element(By.CLASS_NAME, "product_info").text
        originPrice = detailBox[3].find_element(By.CLASS_NAME, "product_info").text
        cursor.execute(insertProductSQL, (i[1], brand, name,
                                          subname, price, image,
                                          releaseDate, color,
                                          originPrice, modelNum))
        cursor.execute(updateFlagSQL, (i[1]))
        db.commit()

    # for detail in detailBox:
        #     title = detail.find_element(By.CLASS_NAME, "product_title")
        #     info = detail.find_element(By.CLASS_NAME, "product_info")
        #     print(title.text, info.text)


def T_get_data():
    selectSQL = "SELECT URL, product_id, flag FROM " \
                "crawler.kream_url where flag = 'N';"
    updateFlagSQL = "UPDATE crawler.kream_url SET flag='Y' WHERE product_id=%s;"
    insertProductSQL = "INSERT INTO crawler.kream_data " \
                       "(productId, brand, name, subName, price, url, releaseDate, color, originPrice, modelNum) " \
                       "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    cursor.execute(selectSQL)
    rows = cursor.fetchall()
    for i in rows:
        driver.get(i[0])
        time.sleep(3)
        box = driver.find_element(By.CLASS_NAME, "main_title_box")
        name = box.find_element(By.CLASS_NAME, "title").text
        print(name)
        image = driver.find_element(By.CLASS_NAME, "item_inner") \
            .find_element(By.TAG_NAME, "img").get_attribute("src")
        if image == "https://kream.co.kr/images/common_thumbs_blank_L.png?type=l":
            driver.refresh()
            time.sleep(1)
            continue;


        brand = box.find_element(By.CLASS_NAME, "brand").text
        subname = box.find_element(By.CLASS_NAME, "sub_title").text
        priceBox = driver.find_element(By.CLASS_NAME, "detail_price")
        price = priceBox.find_element(By.CLASS_NAME, "num").text
        # print(brand,name,subname,price)
        detailBox = driver.find_elements(By.CLASS_NAME, 'detail_box')
        modelNum = detailBox[0].find_element(By.CLASS_NAME, "product_info").text
        releaseDate = detailBox[1].find_element(By.CLASS_NAME, "product_info").text
        color = detailBox[2].find_element(By.CLASS_NAME, "product_info").text
        originPrice = detailBox[3].find_element(By.CLASS_NAME, "product_info").text
        cursor.execute(insertProductSQL, (i[1], brand, name,
                                          subname, price, image,
                                          releaseDate, color,
                                          originPrice, modelNum))
        cursor.execute(updateFlagSQL, (i[1]))
        db.commit()

    # for detail in detailBox:
        #     title = detail.find_element(By.CLASS_NAME, "product_title")
        #     info = detail.find_element(By.CLASS_NAME, "product_info")
        #     print(title.text, info.text)


def get_url():
    driver.get("https://kream.co.kr/search?tab=44&keyword=에어포스")

    total = driver.find_element(By.CLASS_NAME,
                                "filter_result").text
    total = int(total.replace("상품", "")
                .replace(",", "").strip())
    total = 500
    count = 0
    while count < total:
        driver.execute_script("window.scrollTo"
                              "(0,document.body.scrollHeight)")
        time.sleep(1)
        itemList = driver.find_elements(By.CLASS_NAME, "product_card")
        count = len(itemList)
    for item in itemList:
        href = item.find_element(By.TAG_NAME, "a") \
            .get_attribute("href")
        print(href)
        id = href.split("/")[4]
        print(id)
        cursor.execute(insertSQL, (href, id))
        db.commit()


def main():
    # get_url()
    get_data()


if __name__ == '__main__':
    main()
    # get_data()
    # t_data()

