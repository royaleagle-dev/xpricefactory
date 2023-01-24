from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, ListView
from . models import Product

from bs4 import BeautifulSoup as BS
import requests
import pandas as PD

from xcompare.ScrapeEngine import ScrapeEngine

# Create your views here.

class IndexView(View):
    
    def get(self, request):
        return render(request, "xcompare/index.html")        


class ScrapeView(View):
    def get(self, request):
        search_term = request.GET.get('product_name')
        scrape = ScrapeEngine(search_term)
        jumia_scrape = scrape.scrape_jumia()

        ctx = {
            'data': jumia_scrape
        }

        return render(request, "xcompare/raw_prices.html", ctx)

        




class HistoryView(ListView):
    model = Product
    template_name = "products.html"
    context_object_name = "products"

    def get_queryset(self):
        return Product.objects.all().order_by('-date')
