import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import selenium.common.exceptions

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://www.emag.ro/#opensearch')
get_element = browser.find_element(by=By.ID, value='searchboxTrigger')
get_element.send_keys('emitator de sunet FP3')
get_element.submit()
# date = browser.find_element(by=By.CLASS_NAME, value='card-v2')
# for i in date:
#     try:
#         print(i.text)
#         title_of_product = i.find_element(by=By.CLASS_NAME, value='card-v2-title')
#     except selenium.common.exceptions.StaleElementReferenceException:
#         pass
# print(date)
time.sleep(10)