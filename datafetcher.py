from datetime import datetime, timedelta
import urllib.request as request
import json
from urlCreator import urlCreator

# function that will recurse till it finds all the entries
def dataFetcher(url, startDate, endDate, result=None):
    if result is None:
        result = []  # Initialize result here if not provided
    builtURL = urlCreator(url, startDate, endDate) # get the URL with the dates
    with request.urlopen(builtURL) as openURL:
        data = json.load(openURL) # get the json file list
        try:
            actualStart = datetime.fromisoformat(data[0]["dateString"].replace('+00:00',''))
            print(f"Scanning between {actualStart} and {endDate}: {builtURL}")
        except:
            print(f"Scanning between {startDate} and {endDate}: {builtURL}")
        if len(data) >= 1: # if the length of the list is >= the count amount
            result += data
            splittime = (datetime.fromisoformat(data[-1]["dateString"].replace('+00:00',''))-timedelta(seconds=1)) # get the last time obtained and remove a second from it
            splitendDate = splittime.isoformat()
            dataFetcher(url, startDate, splitendDate, result) # set the new enddate (nightscout gets the entries closest to the enddate) and recurse
        else:
            return # if the length is 0
    return result