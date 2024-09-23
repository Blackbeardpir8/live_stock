from django.shortcuts import render
from yahoo_fin.stock_info import *

# Create your views here.
def stockpicker(request):
    stock_picker = tickers_nifty50()  
    print(stock_picker)  
    return render(request, "home/stockpicker.html", {"stockpicker": stock_picker})


def stocktracker(request):
    details = get_quote_table('RELIANCE.NS')
    print(details)

    # Passing the stock details to the template
    context = {
        'details': details
    }
    
    return render(request, "home/stocktracker.html", context)
