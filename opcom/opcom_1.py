from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.get('https://www.opcom.ro/grafice-ip-raportPIP-si-volumTranzactionat/ro')
# //*[@id="Data_table"]   //*[@id="tab_PIP_Vol"]/table/tbody/tr[1]/th[1]
table = browser.find_element(by=By.XPATH, value='//*[@id="tab_PIP_Vol"]/table/tbody/tr[1]/th[1]')
print(table)
