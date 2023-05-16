import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://www.opcom.ro/grafice-ip-raportPIP-si-volumTranzactionat/ro')
get_element = browser.find_element(by=By.__name__, value='data_empty')
get_element.send_keys('14 / 5 / 2023')
get_element.submit()
# date = browser.find_element(by=By.CLASS_NAME, value='card-v2')
# for i in date:
#     try:
#         print(i.text)
#         title_of_product = i.find_element(by=By.CLASS_NAME, value='card-v2-title')
#     except selenium.common.exceptions.StaleElementReferenceException:
#         pass
# print(date)
time.sleep(20)