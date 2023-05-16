from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

option = options.Options()
option.add_experimental_option('detach', True)
option.add_argument("--window-size=1920,1080")
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=option)


def main():
    driver.get("https://search.musinsa.com/ranking/best?new_product_yn=Y")
    driver.find_elements(
        By.CLASS_NAME, "check_box_area")[2].click()
    driver.find_elements(
        By.CLASS_NAME, "check_box_area")[0].click()
    driver.execute_script("mss.ranking.goods.filter.mainCategory('001');")
    items = driver.find_element(By.ID, "goodsRankList") \
        .find_elements(By.CLASS_NAME, "li_box")
    for item in items:
        name = item.find_element(By.CLASS_NAME, "list_info").text
        price = price_formatting(item)
        productURL = item.find_element(By.TAG_NAME, "a").get_attribute("href")
        print(name, price, productURL)


def price_formatting(item):
    if existed_by_tag_name("del", item):
        delName = item.find_element(By.TAG_NAME, "del").text
        price = item.find_element(By.CLASS_NAME, "price").text
        price = price.replace(delName, "")
    else:
        price = item.find_element(By.CLASS_NAME, "price").text
    return price


def existed_by_tag_name(tagName, elements):
    try:
        elements.find_element(By.TAG_NAME, tagName)
        return True
    except NoSuchElementException:
        return False


if __name__ == '__main__':
    main()
