import requests
import xmltodict
import json
import datetime
from provider import Provider


def tcmbLatestTRY() -> Provider:
    url = 'https://www.tcmb.gov.tr/kurlar/today.xml'
    response = requests.get(url)

    x = xmltodict.parse(response.content)
    usd = x['Tarih_Date']['Currency'][0]  # USD
    euro = x['Tarih_Date']['Currency'][3]  # EURO
    usdRate = usd['ForexSelling']
    euroRate = euro['ForexSelling']
    tryRate = 1.0
    return Provider(tryRate, usdRate, euroRate, "TCMB")


def tcmbLatestTRYWithDate(year, month, day) -> Provider:

    date = datetime.datetime(year, month, day)

    dayOfdate = date.weekday()
    # Because at Weekends, there is no records.
    if dayOfdate == 6:
        date = datetime.datetime(year, month, day-2)
    if dayOfdate == 5:
        date = datetime.datetime(year, month, day-1)
    monthYear = date.strftime('%Y%m')
    dayMonthYear = date.strftime('%d%m%Y')

    "https://www.tcmb.gov.tr/kurlar/202012/07122020.xml"
    url = 'https://www.tcmb.gov.tr/kurlar/'+monthYear+'/'+dayMonthYear+'.xml'
    print(url)
    response = requests.get(url)

    x = xmltodict.parse(response.content)
    usd = x['Tarih_Date']['Currency'][0]  # USD
    euro = x['Tarih_Date']['Currency'][3]  # EURO
    usdRate = usd['ForexSelling']
    euroRate = euro['ForexSelling']
    tryRate = 1.0
    return Provider(tryRate, usdRate, euroRate, "TCMB")
