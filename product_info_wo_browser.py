#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

# Define constants
PRODUCT_NAME_SELECTOR = "h1"
PRODUCT_PRICE_SELECTOR = "#originalPrice"
PRODUCT_SALE_PRICE_SELECTOR = "#offering-price"

# URL - Get product info from this
url = "https://www.hepsiburada.com/samsung-galaxy-note-8-64-gb-samsung-turkiye-garantili-p-HBV000007PTJN?magaza=Zenticc&t=product&q=note%208"

# Get page source
print("Loading: {}\n".format(url))
page_source = requests.get(url).text

# Parse page source
parsed_source = BeautifulSoup(page_source, "html.parser")

# Get product name
print("Getting product name...")
product_name = parsed_source.find(PRODUCT_NAME_SELECTOR).text
print("Product Name: {}\n".format(product_name.encode("utf-8")))

# Get product original price
print("Getting product original price...")
product_original_price = parsed_source.select(PRODUCT_PRICE_SELECTOR)[0].text
print("Product Original Price: {}\n".format(product_original_price))

# Get product sale price
print("Getting product sale price...")
product_sale_price = parsed_source.select(PRODUCT_SALE_PRICE_SELECTOR)[0].text
print("Product Sale Price: {}\n".format(product_sale_price))