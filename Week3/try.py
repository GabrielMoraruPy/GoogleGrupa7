from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Create a new instance of the Chrome driver
driver = webdriver.edge

driver.get("https://www.opcom.ro/grafice-ip-raportPIP-si-volumTranzactionat/ro")

day_field = driver.find_element(By.NAME, "day")
day_field.clear()
day_field.send_keys("10")
