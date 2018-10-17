from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import series, user, subscription
from .forms import SubscriptionForm
# from .imdb_page import getLinks

import bs4 as bs
import urllib.request
from urllib.request import Request, urlopen


def index(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            serieses = [i.strip() for i in form.cleaned_data['series'].split(',')]
            print (email, serieses)
            imdb_links = []
            for series in serieses:
                link = getLinks(series)
            #     imdb_links.append(link)
            #     print ("Imdb Page for "+series+" is "+link)
            return render(request, 'index.html', {'form': form})
    else:
        form = SubscriptionForm()
    return render(request, 'index.html', {'form': form})


def subscribe(request):
    if request.method == "POST":
        pass
    return render(request, 'subscribed.html')

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
