from django.shortcuts import render

def StockFetcher(request):
    return render(request, 'mainapp/StockFetcher.html')

def StockTracker(request):
    return render(request, 'mainapp/StockTracker.html')