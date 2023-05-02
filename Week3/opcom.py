from bs4 import BeautifulSoup
import requests
import pandas as pd

# request_page = requests.get('https://www.opcom.ro/grafice-ip-raportPIP-si-volumTranzactionat/ro')
request_page = requests.get("https://www.opcom.ro/grafice-ip-raportPIP-si-volumTranzactionat/ro", verify=False)
link = BeautifulSoup(request_page.text, 'html.parser')
dataset, header_list = [], []
main = link.find_all('div', attrs={'id': 'tab_PIP_Vol'})
print(main[0].find_all('table'))