import json
import requests
import time
import datetime

def finland():
    a = "Up-to-date Covid-19 Statistics in Finland:\n"
    print("Up-to-date Covid-19 Statistics in Finland:")
    today_date = str(datetime.date.today().strftime("%B %d, %Y"))
    present_time = str(datetime.datetime.now())[11:19]
    print("-"*(len(a)-1))
    print("On " + today_date + " at " + present_time + " GMT+7" + ":")

    with open('stats.fi', 'r') as fi:
        old_timestamp = fi.readline().strip()
        old_date = fi.readline().strip()
        old_stats = list(map(int, fi.read().split("\n")))

    # Fetch data from api
    req = requests.get('https://coronavirus-19-api.herokuapp.com/countries/finland')
    data = req.json()

    # Print present stats
    print("Cases: %d\nDeaths: %d\nRecovered: %d" % (data["cases"], data["deaths"], data["recovered"]))
    print()

    # if (today_date != old_date):
    # Print comparisions
    print("Compared to last stored data on " + old_date + " at " + old_timestamp + " GMT+7" + ":\nCases: %d\nDeaths: %d\nRecovered: %d" % (data["cases"] - old_stats[0], data["deaths"] - old_stats[1], data["recovered"] - old_stats[2]))

    old_stats = []
    old_stats = [data["cases"], data["deaths"], data["recovered"]]

    with open('stats.fi', 'w') as fi:
        fi.write(present_time)
        fi.write("\n")
        fi.write(today_date)
        fi.write("\n")
        fi.write("%d\n%d\n%d" % (old_stats[0], old_stats[1], old_stats[2]))