from django.shortcuts import render
from .models import StockData

def dashboard(request):
    stocks = StockData.objects.all()
    return render(request, 'dashboard.html', {'stocks': stocks})
