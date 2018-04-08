#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Define constants
CHROME_PATH = "/usr/bin/google-chrome"
CHROMEDRIVER_PATH = "/vagrant/headless-chrome-examples/chromedriver"
WINDOW_SIZE = "1920,1080"
SCREENSHOT_PATH = "/vagrant/headless-chrome-examples/screenshots/{}_product.png"
PRODUCT_NAME_SELECTOR = "h1"
PRODUCT_PRICE_SELECTOR = "originalPrice"
PRODUCT_SALE_PRICE_SELECTOR = "offering-price"

# URL - Get product info from this
url = "https://hepsiburada.com/samsung-galaxy-note-8-64-gb-samsung-turkiye-garantili-p-HBV000007PTJN?magaza=Zenticc&t=product&q=note%208"
domain = url.split("//")[-1].split("/")[0].split('?')[0]

# Define options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size={}".format(WINDOW_SIZE))
chrome_options.binary_location = CHROME_PATH

# Open browser
browser = webdriver.Chrome(
    executable_path = CHROMEDRIVER_PATH,
    chrome_options = chrome_options
)

# Request URL which we want to take screenshot
print("Loading: {}\n".format(url))
browser.get(url)

# Get product name
print("Getting product name...")
product_name = browser.find_element_by_tag_name(PRODUCT_NAME_SELECTOR).text
print("Product Name: {}\n".format(product_name.encode("utf-8")))

# Get product original price
print("Getting product original price...")
product_original_price = browser.find_element_by_id(PRODUCT_PRICE_SELECTOR).text
print("Product Original Price: {}\n".format(product_original_price))

# Get product sale price
print("Getting product sale price...")
product_sale_price = browser.find_element_by_id(PRODUCT_SALE_PRICE_SELECTOR).text
print("Product Sale Price: {}\n".format(product_sale_price))

# Take screenshot
print("Taking screenshot...")
browser.save_screenshot(SCREENSHOT_PATH.format(domain))

# Close browser
print("Closing browser...")
browser.close()