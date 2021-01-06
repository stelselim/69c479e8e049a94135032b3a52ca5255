import requests
import json
import datetime
from src.provider import Provider


# Latest Exchange Rate For Turkish Lira, Sourche: European Central Bank
# Returns Provider
def europeanLatestTRY():

    response = requests.get(
        'https://api.exchangeratesapi.io/latest?base=TRY')  # Get Request

    dic = response.json()["rates"]  # Dictionary of Rates

    tryRate = dic["TRY"]  # TRY Rate
    usdRate = dic["TRY"]/dic["USD"]  # USD Rate, with base TRY
    euroRate = dic["TRY"]/dic["EUR"]  # EURO Rate, with base TRY
    return Provider(tryRate, usdRate, euroRate, "European Central Bank")


# Exchange Rate With Specific Date For Turkish Lira Sourche: European Central Bank
# Takes year: int, month: int, day: int
# Returns Provider
def europeanTRYWithDate(year, month, day):

    date = datetime.datetime(year, month, day)
    dayMonthYear = date.strftime('%Y-%m-%d')

    url = 'https://api.exchangeratesapi.io/'+dayMonthYear  # URL For Requst
    response = requests.get(url)  # Get Request

    dic = response.json()["rates"]  # Dictionary of Rates

    tryRate = 1.0  # TRY Rate
    euroRate = dic["TRY"]  # EURO Rate, with base TRY
    usdRate = euroRate/dic["USD"]  # USD Rate, with base EURO

    return Provider(tryRate, usdRate, euroRate, "European Central Bank")
