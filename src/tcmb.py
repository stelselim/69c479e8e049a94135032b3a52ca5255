import requests
import xmltodict
import json
import datetime
from src.provider import Provider


# Latest Exchange Rate For Turkish Lira, Sourche: TCMB
# Returns Provider
def tcmbLatestTRY():

    url = 'https://www.tcmb.gov.tr/kurlar/today.xml'

    response = requests.get(url)  # Get Requst

    # XML to Python Dictionary
    dic = xmltodict.parse(response.content)

    usd = dic['Tarih_Date']['Currency'][0]  # USD
    euro = dic['Tarih_Date']['Currency'][3]  # EURO

    usdRate = usd['ForexBuying']  # USD Rate, with base TRY
    euroRate = euro['ForexBuying']  # EURO Rate, with base TRY
    tryRate = 1.0  # TRY Rate

    return Provider(tryRate, usdRate, euroRate, "TCMB")


# Exchange Rate With Specific Date For Turkish Lira Sourche: TCMB
# Takes year: int, month: int, day: int
# Returns Provider
def tcmbLatestTRYWithDate(year, month, day):

    date = datetime.datetime(year, month, day)
    dayOfdate = date.weekday()

    # Because at Weekends, there is no records.
    # If the date is sunday or saturday, it should be changed to last friday.
    if dayOfdate == 6:
        date = datetime.datetime(year, month, day-2)
    if dayOfdate == 5:
        date = datetime.datetime(year, month, day-1)

    # Url Routes For API
    monthYear = date.strftime('%Y%m')
    dayMonthYear = date.strftime('%d%m%Y')

    url = 'https://www.tcmb.gov.tr/kurlar/'+monthYear + \
        '/'+dayMonthYear+'.xml'  # URL For Request

    response = requests.get(url)  # Get Request

    # XML to Python Dictionary
    dic = xmltodict.parse(response.content)

    usd = dic['Tarih_Date']['Currency'][0]  # USD
    euro = dic['Tarih_Date']['Currency'][3]  # EURO

    usdRate = usd['ForexBuying']  # USD Rate, with base TRY
    euroRate = euro['ForexBuying']  # EURO Rate, with base TRY
    tryRate = 1.0  # TRY Rate

    return Provider(tryRate, usdRate, euroRate, "TCMB")
