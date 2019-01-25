from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.dell.com/pt-br/shop/notebooks-dell/sc/laptops').text

soup = BeautifulSoup(source, 'lxml')

for box in soup.find_all('div', {"id":"seriesVariant"}):

	desc = box.p.text
	print(desc)

	preco_titulo = box.find('div', class_='variant-title-alignment')
	preco = preco_titulo.find_all('h4')[1].text
	print(preco)

	print()

