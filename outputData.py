from datafetcher import dataFetcher
import pandas as pd

def outputData(ptID, url, startDate, endDate):
    data = dataFetcher(url, startDate, endDate)
    df = pd.DataFrame(data).sort_values(by=["dateString"])
    df.to_csv("ptData/" + ptID + "_entries.csv", index=False)
    print(f"Export success!")

