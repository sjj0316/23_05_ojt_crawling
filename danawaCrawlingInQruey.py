from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome import options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import NoSuchElementException
import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', password='1234')  #in db

curser = db.cursor()
sql = "insert into crawler.danawacrawler " \
      "(name, price, `option`) values (%s, %s, %s)"   #값 입력 구분


def main():
    option = options.Options()
    option.add_experimental_option('detach',True)
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service,
                              options=option)
    driver.get("https://www.danawa.com/")
    driver.find_element(By.ID,"AKCSearch").send_keys("노트북"+Keys.ENTER)
    time.sleep(2)
    ########
    for pageNo in range(3):
        driver.execute_script("getPage("+str(pageNo+1)+")")
        time.sleep(2)
        products = driver.find_element(By.CLASS_NAME, "main_prodlist_list") \
            .find_elements(By.CLASS_NAME, "prod_item")
        for item in products:
            if item.get_attribute("id") != "":
                # print(item.get_attribute("id"))
                name = item.find_element(By.CLASS_NAME, "prod_name").text
                try:
                    item \
                        .find_element(By.CLASS_NAME, "more_prod_pricelist") \
                        .find_element(By.TAG_NAME, "a").click()

                except NoSuchElementException:
                    pass
                prices = item. \
                    find_element(By.CLASS_NAME, "prod_pricelist") \
                    .find_elements(By.TAG_NAME, "li")
                for item in prices:
                    price = item \
                        .find_element(By.CLASS_NAME, "price_sect") \
                        .find_element(By.TAG_NAME, "a")
                    option = item.find_element(By.CLASS_NAME,
                                               "memory_sect").text
                    if '1위' in option:
                        option = option.replace("1위 ", "")
                    if '2위' in option:
                        option = option.replace("2위 ", "")
                    curser.execute(sql, (name, price.text, option))  # 값 집어넣기
                    db.commit();

                    print(name, price.text, option)


if __name__ == '__main__':
    main()