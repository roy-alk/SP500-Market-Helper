
from lxml import html
import requests

def getTicker():
    link = "https://www.barchart.com/stocks/earnings-within-7-days"
    page = requests.get(link)
    if page.status_code == 200:
        tree = html.fromstring(page.content)

        # Find all elements with class "_grid"
        grids = tree.xpath('//div[@class="row _grid_columns"]')

        for grid in grids:
            symbols = grid.xpath('.//div[@class="_cell symbol"]/text()')
            for symbol in symbols:
                print(symbol.strip())
    else:
        print(f"Error: HTTP request failed with status code {page.status_code}")
        print(page.text)  # Print the response content for further analysis

# Call the function to execute it
getTicker()