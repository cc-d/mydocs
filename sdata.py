#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

# Define the stock symbol and date range
symbol = 'AAPL'
start_date = '2019-01-01'
end_date = '2022-03-22'

# Build the URL for the historical data page
url = f'https://ycharts.com/companies/{symbol}/historical_data/{start_date}/{end_date}'

# Define the user agent string to use
user_agent = (
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like'
    ' Gecko) Chrome/58.0.3029.110 Safari/537.3'
)

# Define the headers to use in the request
headers = {'User-Agent': user_agent}

# Send a GET request to the URL with the custom headers
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find the table containing the historical data
    table = soup.find('table', class_='histDataTable')
    # Extract the column headers from the table
    headers = [th.text.strip() for th in table.find_all('th')]
    # Extract the data rows from the table
    rows = []
    for tr in table.find_all('tr')[1:]:
        row = [td.text.strip() for td in tr.find_all('td')]
        rows.append(row)
    # Print the column headers and data rows
    print(headers)
    for row in rows:
        print(row)
else:
    print(f'Request failed with status code {response.status_code}')
