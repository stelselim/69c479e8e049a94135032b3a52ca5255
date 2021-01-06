from src.europeanCentral import europeanLatestTRY, europeanTRYWithDate
from src.tcmb import tcmbLatestTRY, tcmbLatestTRYWithDate
from src.provider import Provider
import json


# Add to providerList, if needed to increase provider number
def compare():

    providerList = [europeanLatestTRY(), tcmbLatestTRY()]  # Providers

    resp = {}  # Initiliaze Return Dictinoary
    lowestItem = providerList[0]  # Initialize Wiht First
    lowestEuro = providerList[0].euroRate  # Initialize Wiht First

    for item in providerList:
        if item.euroRate < lowestEuro:
            lowestItem = item
            lowestEuro = item.euroRate

    resp["rates"] = {
        "TRY": lowestItem.tryRate,
        "USD": lowestItem.usdRate,
        "EURO": lowestItem.euroRate,
        "Source": lowestItem.providerName
    }

    return json.dumps(resp)


# Add to providerList, if needed to increase provider number
def compareWithDate(year, month, day):

    providerList = [ tcmbLatestTRYWithDate(year, month, day),europeanTRYWithDate(
        year, month, day)]  # Providers

    resp = {}  # Initiliaze Return Dictinoary
    lowestItem = providerList[0]  # Initialize Wiht First
    lowestEuro = providerList[0].euroRate  # Initialize Wiht First

    for item in providerList:
        if item.euroRate < lowestEuro:
            lowestItem = item
            lowestEuro = item.euroRate

    resp["rates"] = {
        "TRY": lowestItem.tryRate,
        "USD": lowestItem.usdRate,
        "EURO": lowestItem.euroRate,
        "Source": lowestItem.providerName
    }

    return json.dumps(resp)
