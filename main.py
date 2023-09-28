import requests
from bs4 import BeautifulSoup

#url = "https://volzhskiy.hh.ru"
url = "https://volzhskiy.hh.ru/search/vacancy?from=suggest_post&search_field=name&search_field=company_name&search_field=description&text=Linux+%D0%B0%D0%B4%D0%BC%D0%B8%D0%BD%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%82%D0%BE%D1%80&enable_snippets=false&L_save_area=true&page=1"
headers = {'User-Agent': 'Mozilla/5.0'} # Добавил данную строку, т.к. получал от сервера 404 при попытке парсинга


response = requests.get(url, headers=headers)