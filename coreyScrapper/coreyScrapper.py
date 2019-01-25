from bs4 import BeautifulSoup
import requests

# retorna um response object
source = requests.get('http://coreyms.com/')

# pega somente o html do objeto
source = requests.get('http://coreyms.com/').text

soup = BeautifulSoup(source, 'lxml')

for article in soup.find_all('article'):
	headline = article.h2.a.text
	print(headline)

	summary = article.find('div', class_='entry-content').p.text
	print(summary)

	vd_src = article.find('iframe')['src']

	vd_yt = vd_src.split('?')[0]
	vd_ulr = vd_yt.split('/')[4]
	link = f'https://www.youtube.com/watch?v={vd_ulr}'
	print(link)

	print()


