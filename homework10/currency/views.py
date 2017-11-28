from django.shortcuts import render
import requests
# Create your views here.

def currency(request):
    try:
        url_eur = "https://api.fixer.io/latest?base=EUR&symbols=EUR,RUB"
        url_usd= "https://api.fixer.io/latest?base=USD&symbols=USD,RUB"
        try:
            json_data_usd = getAPI(url_usd)
            json_data_eur = getAPI(url_eur)
        except Exception as e:
            raise  ConnectionError
        rub_usd = json_data_usd['rates']['RUB']
        rub_eur = json_data_eur['rates']['RUB']
        return render(request, 'currency/index_currency.html', {
            'rub_usd' : rub_usd,
            'rub_eur' : rub_eur,

        })

    except ConnectionError:
        return render(request, 'weather/error.html')


def getAPI(url):
    r = requests.get(url)
    return r.json()