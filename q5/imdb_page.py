import bs4 as bs
import urllib.request
from urllib.request import Request, urlopen
from .models import series

def getLinks(search):
	search = search.strip()
	search = search.replace(" ", "+")
	url = 'https://www.imdb.com/find?ref_=nv_sr_fn&q='+search+'&s=tt'

	req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	source = urlopen(req).read()

	soup = bs.BeautifulSoup(source, 'lxml')
	Mdiv = soup.find('table', {'class':'findList'})
	table = Mdiv.find_all('td', {'class':'result_text'})

	tag = 'tv series'

	for row in table:
		if tag.upper() in row.get_text().strip().upper():
			link = 'https://www.imdb.com'+row.find('a').get('href')
			break

	return link