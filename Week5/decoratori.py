# # def decorator_simplu(parametru):
# #     print(f"Apelam functia {parametru.__name__}")
# #     return parametru
# #
# # @decorator_simplu
# # def functie_simpla():
# #     return "Buna seara"
# #
# # functie_simpla()
#
# # def decorator_depozit(functia_noastra):
# #     def ambalaj_metoda(carti):
# #         return f"Ambalam produse din {functia_noastra.__name__} care contine cartea {carti}"
# #     return ambalaj_metoda
# #
# # @decorator_depozit
# # def impachetare_carti(nume):
# #     return nume
#
# # def decorator_depozit(material):
# #     def ambalaj(functia_noastra):
# #         def ambalaj_intern(*carte):
# #             return f"Ambalam produse din {functia_noastra.__name__} cu {material} care contine cartea {', '.join(x for x in carte)}"
# #         return ambalaj_intern
# #     return ambalaj
# #
# # @decorator_depozit("hartie")
# # def impachetare_carti(*nume):
# #     return nume
# # print(impachetare_carti("Baltagul", "Amintiri din copilarie"))
# # print(impachetare_carti("Ion"))
# import time
#
# def calculeaza_timpul(functia):
#     def functia_interioara(parametru):
#         inceput = time.time()
#         suma = functia(parametru)
#         sfarsit = time.time()
#         print(f"Timp total de executie al functiei '{functia.__name__}': {sfarsit - inceput}")
#         return suma
#     return functia_interioara
#
# @calculeaza_timpul
# def adunare(number):
#     suma = 0
#     for i in range(number):
#         suma += i
#     return suma
#
# print(adunare(100))


import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# Send a POST request to the webpage with the date range
url = 'https://www.opcom.ro/piata-spot/grafice/piata-bilateral-energie-electrica'
start_date = '01/01/2021'
end_date = '01/01/2022'
payload = {
    'tip_p': 'P',
    'tip_prod': 'EE',
    'optiune_grafic': 'medie',
    'furnizor': '',
    'data_de_la': start_date,
    'data_pana_la': end_date,
    'submit': 'Vizualizare'
}
response = requests.post(url, data=payload, verify = False)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table element containing the data
table = soup.find('table', {'class': 'border_table'})

# Extract the data from the table
data = []
print(table)
for tr in table.find_all('th')[1:]:
    tds = tr.find_all('td')
    if len(tds) > 1:
        date_str = tds[0].text.strip()
        time_str = tds[1].text.strip()
        datetime_str = f'{date_str} {time_str}'
        datetime_obj = datetime.strptime(datetime_str, '%d.%m.%Y %H:%M')
        ropex_dam_h = float(tds[2].text.strip().replace(',', '.'))
        data.append((datetime_obj, ropex_dam_h))

# Filter the data by the date range and extract the values for each hour of every day
start_date_obj = datetime.strptime(start_date, '%d/%m/%Y')
end_date_obj = datetime.strptime(end_date, '%d/%m/%Y')
date_obj = start_date_obj
while date_obj <= end_date_obj:
    for hour in range(24):
        datetime_obj = datetime(date_obj.year, date_obj.month, date_obj.day, hour)
        data_hour = next((d[1] for d in data if d[0] == datetime_obj), None)
        print(f'{datetime_obj}: {data_hour}')
    date_obj += timedelta(days=1)
