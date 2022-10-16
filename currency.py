from currency_converter import  CurrencyConverter
cc = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip')
print(cc.currencies)
print(cc.convert(1,'USD','KRW'))

import requests
from bs4 import BeautifulSoup
from requests.models import Response
def get_exchange_rate(target1, target2):
  headers = {
      'user-Agent': 'Mozilla/5.0',
      'Contetnt-type': 'text/html; charest=utf-8'
  }

Response = requests.get('https://kr.investing.com/currencies/{}-{}'.format(target1, target2), headers = headers)

content = BeautifulStoneSoup(response, content, 'html.parser')
containers = content.find('span', {'data-test': 'instrument-price-last'})

print(containers.text)
get_exchange_rate('usd', 'krw')