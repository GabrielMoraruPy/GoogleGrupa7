from bs4 import BeautifulSoup
import requests

# date_str = input("Enter date in format dd/mm/yyyy: ")

# # Format date string for POST request
# day, month, year = date_str.split("/")
# date_payload = {
#     "day": day,
#     "month": month,
#     "year": year
# }
# response = requests.post("https://www.opcom.ro/grafice-ip-raportPIP-si-volumTranzactionat/ro",data=date_payload, verify=False)
# request_page = requests.get('https://www.opcom.ro/grafice-ip-raportPIP-si-volumTranzactionat/ro')
request_page = requests.get("https://www.opcom.ro/grafice-ip-raportPIP-si-volumTranzactionat/ro", verify=False)
soup = BeautifulSoup(request_page.text, 'html.parser')
main = soup.find_all('div', attrs={'id': 'tab_PIP_Vol'})
tabel = main[0].find_all('table')
# print(type(tabel))

# obiect = soup.find_all('td')
# print(obiect)

# celula = soup.find_tabel('td')

# for row in tabel:
#     cells = row.find_all('td')
#     for cell in cells:
#         print(cell.text)

data = []

for row in tabel:
    cells = row.find_all('td')
    row_data = []
    for cell in cells:
        row_data.append(cell.text)
    data.append(row_data)

# for rows in data:
#     print('\n'.join(rows))

for index, numere in enumerate(data):
    # print(numere)
    for i in range(len(numere)):
        if numere[i].isdigit():
            print(numere[i], numere[i+1])