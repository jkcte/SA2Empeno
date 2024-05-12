import requests
import pandas as pd
from datetime import datetime


def fetch_data(limit, timestamp=None):
    url = 'https://min-api.cryptocompare.com/data/v2/histoday'
    parameters = {
        'fsym': 'ETH',
        'tsym': 'USD',
        'limit': limit,  # the maximum number of data points per call
        'api_key': 'your_api_key_here',
        'toTs': timestamp  # used for pagination
    }
    response = requests.get(url, params=parameters)
    data = response.json()
    return data['Data']['Data']


def main():
    end_time = int(datetime(2024, 4, 15).timestamp())  # end date as a Unix timestamp
    results = []

    for x in range(2):
        if x != 2:

            data = fetch_data(2000, 1438905600+(x+1)*86400*2000)
            if not data:
                break
            results.extend(data)
            end_time = data[0]['time']  # update end_time to the earliest time in the fetched data
        else:

            data = fetch_data(504, 1,714,521,600)
            if not data:
                break
            results.extend(data)

    df = pd.DataFrame(results)
    df['time'] = pd.to_datetime(df['time'], unit='s')  # convert timestamp to datetime
    df.to_csv('ethereum_daily_data.csv', index=False)
    print('Data fetched successfully!')


if __name__ == "__main__":
    main()
