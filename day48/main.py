from selenium import webdriver
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.common.by import By

DRIVER_PATH = "C:\chromedriver\chromedriver.exe"
URL="https://www.amazon.co.jp/GARMIN-%E3%82%AC%E3%83%BC%E3%83%9F%E3%83%B3-%E3%82%B9%E3%83%9E%E3%83%BC%E3%83%88%E3%82%A6%E3%82%A9%E3%83%83%E3%83%81-Slate%E3%80%90%E6%97%A5%E6%9C%AC%E6%AD%A3%E8%A6%8F%E5%93%81%E3%80%91-010-02430-61/dp/B094VSZPPP/ref=sr_1_7?keywords=%E3%82%B9%E3%83%9E%E3%83%BC%E3%83%88%E3%82%A6%E3%82%A9%E3%83%83%E3%83%81&qid=1645105184&refinements=p_89%3A%E3%82%AC%E3%83%BC%E3%83%9F%E3%83%B3(GARMIN)&rnid=2321255051&s=electronics&sr=1-7&th=1"

chrome_service = fs.Service(executable_path=DRIVER_PATH)
driver = webdriver.Chrome(service=chrome_service)
driver.get(URL)
price = driver.find_element(by=By.CLASS_NAME, value="a-price-whole")
print(price.text)
driver.quit()
