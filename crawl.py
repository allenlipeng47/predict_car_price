import requests
from bs4 import BeautifulSoup
import re
import csv
import pandas as pd
import os
import sys
import configparser

config = configparser.ConfigParser()
config.read('./CONFIG')

MODEL_NAME = config['DEFAULT']['MODEL_NAME']
CURRENT_YEAR = int(config['DEFAULT']['CURRENT_YEAR'])

print(f"MODEL_NAME: {MODEL_NAME}")
print(f"CURRENT_YEAR: {CURRENT_YEAR}")

def crawl_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the title text (year)
        title_span = soup.find('span', id='titletextonly')
        year_pattern = re.compile(r"19\d{2}|20\d{2}|21\d{2}|22\d{2}|23\d{2}")
        year_match = year_pattern.search(title_span.text)
        year = year_match.group(0) if year_match else None
        year = int(year)

        # Extract the price
        price_span = soup.find('span', class_='price')
        price = price_span.text.strip('$')
        price.replace(",", "")
        price = int(price.replace(',', '').strip('$'))

        # Extract the odometer
        odometer_text = soup.select_one('span:contains("odometer:") b')
        odometer_text = re.sub(r'(<br>|<\/br>)', '', odometer_text.text.strip())

        # Process the odometer text
        odometer = int(odometer_text.replace(',', ''))
        if (odometer > 10000):
            odometer = int(odometer / 1000)

        # Return the extracted information
        return {
            'year': year,
            'price': price,
            'odometer': odometer,
            'url': url
        }
    else:
        print('Error:', response.status_code)



if __name__ == '__main__':
    if len(sys.argv) == 2:
        url = sys.argv[1]
        car_info = crawl_url(url)

        print(car_info)

        file_data = "./%s/data.csv" % MODEL_NAME

        if not os.path.exists(MODEL_NAME):
            os.makedirs(MODEL_NAME)

        if not os.path.exists(file_data):
            with open(file_data, "w") as f:
                f.write("year,odometer,price,url\n")

        # Append car information to CSV file
        with open(file_data, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['year', 'odometer', 'price', 'url'])
            writer.writerow(car_info)

        # Alternative approach using pandas
        df = pd.read_csv(file_data)
        df = df.append(car_info, ignore_index=True)
        df.to_csv(file_data, index=False)

    else:
        print('Usage: python crawl_url.py <url>')
