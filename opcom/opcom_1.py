from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.get('https://www.opcom.ro/grafice-ip-raportPIP-si-volumTranzactionat/ro')
# //*[@id="exampleIII"]/input[2]
zi = browser.find_element(by=By.XPATH, value='//*[@id="exampleIII"]/input[2]')
print(zi)


