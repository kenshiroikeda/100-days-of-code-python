from selenium import webdriver
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.common.by import By

DRIVER_PATH = "C:\chromedriver\chromedriver.exe"
URL="https://www.python.org/"

chrome_service = fs.Service(executable_path=DRIVER_PATH)
driver = webdriver.Chrome(service=chrome_service)
driver.get(URL)
elements = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget li")
events_dict = {}
for idx in range(0, len(elements)):
    event_dict = {}
    element = elements[idx]
    event_dict['time'] = element.find_element(by=By.TAG_NAME, value="time").text
    event_dict['name'] = element.find_element(by=By.TAG_NAME, value="a").text
    events_dict[idx] = event_dict

print(events_dict)
driver.quit()
