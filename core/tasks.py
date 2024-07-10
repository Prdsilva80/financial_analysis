import os
import requests
from datetime import datetime
from django.utils import timezone
from .models import StockData
from dotenv import load_dotenv

load_dotenv()

def fetch_and_save_stock_data():
    api_token = os.getenv("BRAPI_API_TOKEN")
    stock_symbols = ['PETR4', 'VALE3']  # Adicione os símbolos desejados aqui

    for symbol in stock_symbols:
        url = f'https://brapi.dev/api/quote/{symbol}?token={api_token}'
        response = requests.get(url)
        if response.status_code == 200:
            stock_data = response.json()['results'][0]
            stock, created = StockData.objects.update_or_create(
                symbol=stock_data['symbol'],
                defaults={
                    'long_name': stock_data['longName'],
                    'regular_market_price': stock_data['regularMarketPrice'],
                    'regular_market_volume': stock_data['regularMarketVolume'],
                    'regular_market_time': datetime.fromtimestamp(stock_data['regularMarketTime'], timezone.utc)
                }
            )
