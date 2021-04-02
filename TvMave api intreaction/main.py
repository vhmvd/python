# For request and json functionality
import requests
# For creation of date generator from a given period. In this case for a year
import time
from datetime import date, datetime, timedelta

# url where we want the data from
url = 'http://api.tvmaze.com/schedule?date='

year_input = input('Enter the year for show search on tvMaze with respect to AirDate: ')

# This function generates the date
def perdelta(start, end, delta):
    curr = start
    while curr < end:
        yield curr
        curr += delta

# This function requests the data from the api. It takes year as the input and makes the call for that 
def tvmaze_year(year):
    # Records the response 
    response = requests.get(url+year)
    # Checks if the data is available or if there is timeout
    if response.status_code == 429:
        print('Too many requests, taking a 10 second nap')
        time.sleep(10)
        tvmaze_year(year)
        return
    elif response.status_code == 422:
        print('Invalid year entered!')
        quit()
    # Converts json object into python object
    data = response.json()
    if not data:
        print(year, '>No data available!')
        return
    # Prints date and the name of the shows
    for data_block in data:
        print(year, data_block['show']['name'])

# Looop to call api for every date in a year
for date_str in perdelta(date(int(year_input), 1, 1), date(int(year_input), 12, 31), timedelta(days=1)):
    tvmaze_year(str(date_str))
