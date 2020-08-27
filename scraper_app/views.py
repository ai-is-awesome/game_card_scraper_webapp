from django.shortcuts import render
from .forms import ScraperForm
import os
from django.conf import settings
from django.http import HttpResponse, Http404
from src.troll_and_toad import main
from new_proj.main2 import run



# Create your views here.



def index(request):
    form = ScraperForm
    context = {'form' : form}
    return render(request, 'scraper_app/index.html', context)




def scrape(request):
    if request.method == 'GET':
        form = ScraperForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']


    results = main(query)
    context = dict()
    context['results'] = results


    return render(request, 'scraper_app/troll_and_toad.html', context)


def scraper2(request):

    return render(request, 'scraper_app/temp.html', {})





def scraper2_detail(request):
    if request.method == "GET":
        query = request.GET['query']
        print("runing main 2")
        span = run()

    return render(request, 'scraper_app/temp_detail.html', {'span' : span})












