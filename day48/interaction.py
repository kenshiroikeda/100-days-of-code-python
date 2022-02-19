from selenium import webdriver
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

DRIVER_PATH = "C:\chromedriver\chromedriver.exe"
URL="https://ja.wikipedia.org/wiki/%E3%83%A1%E3%82%A4%E3%83%B3%E3%83%9A%E3%83%BC%E3%82%B8"

chrome_service = fs.Service(executable_path=DRIVER_PATH)
driver = webdriver.Chrome(service=chrome_service)
driver.get(URL)
element = driver.find_element(by=By.CSS_SELECTOR, value="#number b a")
element.click()

all_portals = driver.find_element(by=By.LINK_TEXT, value="総ページ数")
all_portals.click()

search_box = driver.find_element(by=By.NAME, value="search")
search_box.send_keys("Python")
search_box.send_keys(Keys.ENTER)

# search_button = driver.find_element(by=By.ID, value="searchButton")
# search_button.click()

