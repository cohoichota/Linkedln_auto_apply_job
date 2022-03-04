from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
# from selenium.common.exceptions import NoSuchElementException
import time


ACCOUNT_EMAIL = "zzz@gmail.com"
ACCOUNT_PASSWORD = "zzz"


service = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service)

URL = "https://www.messenger.com/"
driver.get(URL)
driver.maximize_window()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(3)
user_name = driver.find_element(By.NAME, "email")
user_name.send_keys(ACCOUNT_EMAIL)

password = driver.find_element(By.NAME, "pass")
password.send_keys(ACCOUNT_PASSWORD)

time.sleep(3)

log_in = driver.find_element(By.NAME, "login")
log_in.click()

time.sleep(5)

friend_chat = driver.find_element(By.CSS_SELECTOR, "span span .a8c37x1j ")
friend_chat.click()
print(friend_chat.text)



i=0
while i<5:
    chat_box = driver.find_element(By.CSS_SELECTOR, "div div div ._1mf ")
    chat_box.send_keys("check code")
    time.sleep(2)
    chat_box.send_keys(Keys.ENTER)
    i+=1