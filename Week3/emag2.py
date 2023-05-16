from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

from selenium import webdriver
from selenium.webdriver.common.by import By

# Assuming you have already set up your WebDriver instance
driver = webdriver.Chrome()
driver.get("https://www.opcom.ro/grafice-ip-raportPIP-si-volumTranzactionat/ro")

# Find the form element by name
form = driver.find_element(By.NAME, 'data_select')

# Find the input elements inside the form
hidden_token_input = form.find_element(By.NAME, '_token')
day_input = form.find_element(By.NAME, 'day')
month_input = form.find_element(By.NAME, 'month')
year_input = form.find_element(By.NAME, 'year')
refresh_button = form.find_element(By.NAME, 'buton')

# Accessing attribute values of the input elements
hidden_token_value = hidden_token_input.get_attribute('value')
day_value = day_input.get_attribute('value')
month_value = month_input.get_attribute('value')
year_value = year_input.get_attribute('value')
refresh_button_value = refresh_button.get_attribute('value')

# Printing the attribute values
print(hidden_token_value)
print(day_value)
print(month_value)
print(year_value)
print(refresh_button_value)



# driver.get("https://webscraper.io")

# search = driver.find_element(By.XPATH, '/html/body/div[2]/div[6]/div[1]/table/tbody/tr/td[2]/div/form/span/input[2]')
# search.send_keys("10")
# search.send_keys(Keys.RETURN)

# refresh = driver.find_element(By.NAME, "buton").click()

time.sleep(15)


driver.quit()

