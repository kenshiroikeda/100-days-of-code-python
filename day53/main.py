import os

import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome import service as fs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

DRIVER_PATH = "C:\chromedriver\chromedriver.exe"

ZILLOW_URL = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.28447703141124%2C%22east%22%3A-121.88278940934093%2C%22south%22%3A37.702217381064884%2C%22north%22%3A37.928416149069065%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
SHEETS_URL = "https://forms.gle/53SpfXXuQs7P6Uoi9"

header = {
    "Accept-Language" : "ja,en-US;q=0.9,en;q=0.8",
    "User-Agent": os.getenv("USER_AGENT")
}

res = requests.get(ZILLOW_URL, headers=header)

soup = BeautifulSoup(res.text, "html.parser")

price_elem_list = soup.find_all(class_="list-card-price")
link_elem_list = soup.find_all(class_="list-card-link")
addr_elem_list = soup.find_all(class_="list-card-addr")

chrome_service = fs.Service(executable_path=DRIVER_PATH)
driver = webdriver.Chrome(service=chrome_service)


for idx in range(0, len(price_elem_list)):
    driver.get(SHEETS_URL)
    time.sleep(1)
    address = driver.find_elements(by=By.CLASS_NAME, value='quantumWizTextinputPaperinputInput')[0]
    address.send_keys(addr_elem_list[idx].text.split("/")[0])
    link = driver.find_elements(by=By.CLASS_NAME, value='quantumWizTextinputPaperinputInput')[1]
    link.send_keys(link_elem_list[idx]['href'])
    price = driver.find_elements(by=By.CLASS_NAME, value='quantumWizTextinputPaperinputInput')[2]
    price.send_keys(price_elem_list[idx].text)
    send_btn = driver.find_element(by=By.CLASS_NAME, value='appsMaterialWizButtonEl')
    send_btn.click()
