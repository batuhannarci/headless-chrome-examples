#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Define constants
CHROME_PATH = "/usr/bin/google-chrome"
CHROMEDRIVER_PATH = "/vagrant/headless-chrome-examples/chromedriver"
WINDOW_SIZE = "1920,1080"
SCREENSHOT_PATH = "/vagrant/headless-chrome-examples/screenshots/{}_execute_script.png"
SCRIPT = "$('.MegaBanner').html('<div style=\"text-align:center;font-size:45px\">Hey! I`m working.</div>')"

# URL - run script in this site
url = "https://hepsiburada.com/"
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
print("Executing script on page...\n")
browser.execute_script(SCRIPT)

# Take screenshot
print("Taking screenshot...\n")
browser.save_screenshot(SCREENSHOT_PATH.format(domain))

# Close browser
print("Closing browser...")
browser.close()