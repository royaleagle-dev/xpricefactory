from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, ListView
from . models import Product

# Create your views here.

class IndexView(View):
    
    def get(self, request):
        return render(request, "xcompare/index.html")

    def post(self, request):
        pass


class HistoryView(ListView):
    model = Product
    template_name = "products.html"
    context_object_name = "products"

    def get_queryset(self):
        return Product.objects.all().order_by('-date')
