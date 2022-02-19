from selenium import webdriver
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

DRIVER_PATH = "C:\chromedriver\chromedriver.exe"
URL="http://secure-retreat-92358.herokuapp.com/"

chrome_service = fs.Service(executable_path=DRIVER_PATH)
driver = webdriver.Chrome(service=chrome_service)
driver.get(URL)

f_name = driver.find_element(by=By.NAME, value="fName")
f_name.send_keys("Ken")

l_name = driver.find_element(by=By.NAME, value="lName")
l_name.send_keys("Ike")

email = driver.find_element(by=By.NAME, value="email")
email.send_keys("kenike@mail.com")

btn_signup = driver.find_element(by=By.TAG_NAME, value="button")
btn_signup.click()
