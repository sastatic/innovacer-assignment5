from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import series, user, subscription
from .forms import SubscriptionForm
from .imdb_page import getLinks
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
                imdb_links.append(link)
                print ("Imdb Page for "+series+" is "+link)
            # print (imdb_links)
            return render(request, 'index.html', {'form': form})
    else:
        form = SubscriptionForm()
    return render(request, 'index.html', {'form': form})


def subscribe(request):
    if request.method == "POST":
        pass
    return render(request, 'subscribed.html')