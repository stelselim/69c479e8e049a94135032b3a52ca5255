import requests
import json
import datetime
from provider import Provider


def europeanLatestTRY() -> Provider:
    r = requests.get('https://api.exchangeratesapi.io/latest?base=TRY')
    dic = r.json()["rates"]
    tryRate = dic["TRY"]
    usdRate = dic["TRY"]/dic["USD"]
    euroRate = dic["TRY"]/dic["EUR"]
    print(usdRate)
    print(euroRate)
    print(tryRate)
    return Provider(tryRate,usdRate,euroRate,"European Central Bank")


def europeanTRYWithDate(year,month,day) -> Provider:
    date = datetime.datetime(year,month,day)
    url = 'https://api.exchangeratesapi.io/'+str(date.year)+'-'+str(+date.month)+'-'+str(date.day)
    print(url)
    r = requests.get(url)
    dic = r.json()["rates"]
    euroRate = dic["TRY"]
    usdRate = dic["TRY"]/dic["USD"]
    tryRate = 1.0
    return Provider(tryRate,usdRate,euroRate,"European Central Bank")

