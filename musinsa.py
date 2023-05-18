from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome import options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
option = options.Options()
option.add_experimental_option('detach', True)
option.add_argument("--window-size=1920,1080")
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,
                          options=option)
def main():
    driver.get("https://search.musinsa.com/ranking/best?new_product_yn=Y")
    time.sleep(1)
    driver.find_elements(
        By.CLASS_NAME,"check_box_area")[2].click()
    driver.find_elements(
        By.CLASS_NAME,"check_box_area")[0].click()
    driver.execute_script("mss.ranking.goods.filter.mainCategory('001');")

    for i in range(10):
        driver.get("https://search.musinsa.com/ranking/best?period=now&age=ALL&mainCategory=001&subCategory=&leafCategory=&price=&golf=false&kids=false&newProduct=false&exclusive=false&discount=true&soldOut=false&page=1&viewType=small&priceMin=&priceMax=")
        items = driver.find_element(By.ID, "goodsRankList") \
                    .find_elements(By.CLASS_NAME, "li_box")[:10]
        name = items[i].find_element(By.CLASS_NAME,"list_info").text
        price = price_formatting(items[i])
        productURL= items[i].find_element(By.TAG_NAME,"a").get_attribute("href")
        print(name,price,productURL)
        items[i].find_element(By.TAG_NAME, "a").click()

        #driver.get(productURL)
        time.sleep(1)
        brand = driver.find_element\
            (By.CLASS_NAME,"product_article_contents").text
        totalSale = driver.find_element(By.ID,"sales_1y_qty").text
        age = driver.find_element(By.CLASS_NAME,'graph_age').text
        sizes = []
        if existed_by_id_name("size_table",driver):
            sizeTable = driver.find_element(By.ID, "size_table") \
                .find_element(By.TAG_NAME, "tbody") \
                .find_elements(By.TAG_NAME, "tr")
            for i in sizeTable:
                if i.get_attribute("id") == "":
                    size = i.find_element(By.TAG_NAME, "th").text
                    sizes.append(size)

        fit = {}
        if existed_by_class_name("table-simple",driver):
            fitTable = driver.find_element(By.CLASS_NAME,'table-simple')\
                .find_elements(By.TAG_NAME,"tr")
            for item in fitTable:
                key = item.find_element(By.TAG_NAME,"th").text
                value = []
                for i in item.find_elements(By.TAG_NAME,"td"):
                    if i.get_attribute("class")=="active":
                        value.append(i.text)
                fit[key] = value
        print(brand,totalSale,age,size,fit)
        time.sleep(1)
        time.sleep(1)


def price_formatting(item):
    if existed_by_tag_name("del",item):
        delName = item.find_element(By.TAG_NAME, "del").text
        price = item.find_element(By.CLASS_NAME, "price").text
        price  = price.replace(delName,"")
    else:
        price = item.find_element(By.CLASS_NAME, "price").text
    return price

def existed_by_tag_name(tagName,elements):
    try:
        elements.find_element(By.TAG_NAME,tagName)
        return True
    except NoSuchElementException:
        return False

def existed_by_class_name(className,elements):
    try:
        elements.find_element(By.CLASS_NAME,className)
        return True
    except NoSuchElementException:
        return False

def existed_by_id_name(idName,elements):
    try:
        elements.find_element(By.ID,idName)
        return True
    except NoSuchElementException:
        return False

if __name__ == '__main__':
    main()
if __name__ == '__main__':
    main()