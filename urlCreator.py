def urlCreator(url, startDate, endDate):
    if url[-1] != "/":
        url = url + "/"
    apiURL = url + "api/v1/entries.json?find[dateString][$gte]=" + str(startDate) + "&find[dateString][$lte]=" + str(endDate) + "&count=" + str(1000)
    return apiURL