from django.http import JsonResponse
import yfinance as yf
from datetime import datetime, timedelta

def get_stock_data(request):

    name = request.GET['name']
    no_of_share = int(request.GET['no_of_share'])
    bought_date = request.GET['bought_date']
    bought_date_obj = datetime.strptime(bought_date,'%Y-%m-%d')
    res = yf.Ticker(name)
    bought_date_price = res.history(start=bought_date,end=bought_date_obj+timedelta(days=1))['Close'].values[0]
    current_price = get_current_price(name)

    data = {
            "bought_date_price":bought_date_price,
            "current_price":current_price
        }
    if bought_date_price > current_price:
        data["loss_incurred"] = no_of_share * (bought_date_price-current_price)
    else:
        data["profit_earned"] = no_of_share * (current_price-bought_date_price)

    return JsonResponse(data, safe=False)



def get_current_price(name):
    ticker = yf.Ticker(name)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]