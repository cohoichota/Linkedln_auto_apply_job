from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import time

ACCOUNT_EMAIL = "xxx@gmail.com"
ACCOUNT_PASSWORD = "xxx"
PHONE = "0123456789"


service = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service)

URL = "https://www.linkedin.com/jobs/search/?currentJobId=2798059664&f_AL=true&geoId=106808692&keywords=python%20developer&location=malaysia"
driver.get(URL)
driver.maximize_window()

time.sleep(2)
sign_in = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
sign_in.click()

time.sleep(5)
user_name = driver.find_element(By.ID, "username")
user_name.send_keys(ACCOUNT_EMAIL)

pass_input = driver.find_element(By.ID, "password")
pass_input.send_keys(ACCOUNT_PASSWORD)

time.sleep(5)

sign_in_button = driver.find_element(By.CLASS_NAME, "from__button--floating")
sign_in_button.click()
time.sleep(3)

# 1 time auto apply
# easy_apply = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
# easy_apply.click()
#
# time.sleep(2)
# phone_number = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
# phone_number.send_keys(PHONE)
#
# time.sleep(3)
# next_1 = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
# next_1.click()
#
# time.sleep(3)
# next_2 = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
# next_2.click()
#
# time.sleep(3)
# quest_1 = driver.find_element(By.NAME, "urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2851886527,40149667,numeric)")
# quest_1.send_keys("1")
#
# quest_2 = driver.find_element(By.NAME, "urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2851886527,40149659,numeric)")
# quest_2.send_keys("1")
#
# quest_3 = driver.find_element(By.NAME, "urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2851886527,40149651,numeric)")
# quest_3.send_keys("1")
#
# time.sleep(3)
#
# review = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
# review.click()
#
# time.sleep(5)
#
# submit_application = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
# submit_application.click()



#Apply for all jobs
# all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
#
# for listing in all_listings:
#     print("called")
#     listing.click()
#     time.sleep(2)
#     try:
#         apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
#         apply_button.click()
#
#         time.sleep(5)
#         phone = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
#         if phone.text == "":
#             phone.send_keys(PHONE)
#
#         submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
#         if submit_button.get_attribute("data-control-name") == "continue_unify":
#             close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
#             close_button.click()
#
#             time.sleep(2)
#             discard_button = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
#             discard_button.click()
#             print("Complex application, skipped.")
#             continue
#         else:
#             submit_button.click()
#
#         time.sleep(2)
#         close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
#         close_button.click()
#
#     except NoSuchElementException:
#         print("No application button, skipped.")
#         continue
#
# time.sleep(5)
# driver.quit()

