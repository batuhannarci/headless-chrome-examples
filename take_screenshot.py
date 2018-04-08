#!/usr/bin/python3
import argparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Get url from argument
parser = argparse.ArgumentParser()
parser.add_argument('--url', help='Specify url.', required=True)
args = parser.parse_args()

# URL - take screenshot of this
url = args.url
domain = url.split("//")[-1].split("/")[0].split('?')[0]

# Define constants
CHROME_PATH = "/usr/bin/google-chrome"
CHROMEDRIVER_PATH = "/vagrant/headless-chrome-examples/chromedriver"
SCREENSHOT_PATH = "/vagrant/headless-chrome-examples/screenshots/{}_{}.png"
WINDOW_SIZES = [
    {'width': 1920, 'height': 1080},
    {'width': 1600, 'height': 900},
    {'width': 1360, 'height': 768},
    {'width': 1024, 'height': 768}
]
MOBILE_EMULATIONS = [
    {"deviceName": "iPhone 5/SE"},
    {"deviceName": "Galaxy S5"},
    {"deviceName": "iPad Pro"}
]

# Define options for desktop browser
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.binary_location = CHROME_PATH

# Open browser
browser = webdriver.Chrome(
    executable_path = CHROMEDRIVER_PATH,
    chrome_options = chrome_options
)

# Request URL which we want to take screenshot
print("Loading: {}\n".format(url))
browser.get(url)

# Take screenshot
print("Taking screenshots for desktops...")

for window_size in WINDOW_SIZES:
    print("Set window size to {}x{}".format(window_size["width"], window_size["height"]))
    browser.set_window_size(window_size["width"], window_size["height"])
    browser.save_screenshot(SCREENSHOT_PATH.format(domain, str(window_size["width"]) + "x" + str(window_size["height"])))

# Close browser
print("Closing browser...\n")
browser.close()

# Take screenshot for mobile devices
for mobile_emulation in MOBILE_EMULATIONS:
    chrome_options_mobile = Options()
    chrome_options_mobile.add_argument("--headless")
    chrome_options_mobile.add_experimental_option("mobileEmulation", mobile_emulation)
    chrome_options_mobile.binary_location = CHROME_PATH

    # Open browser
    mobile_browser = webdriver.Chrome(
        executable_path=CHROMEDRIVER_PATH,
        chrome_options=chrome_options_mobile
    )

    # Request URL which we want to take screenshot
    print("Loading for mobile({}): {}".format(mobile_emulation, url))
    mobile_browser.get(url)

    # Take screenshot
    print("Taking screenshot for {}...".format(mobile_emulation))
    mobile_browser.save_screenshot(SCREENSHOT_PATH.format(domain, mobile_emulation))

    # Close browser
    print("Closing mobile browser...\n")
    mobile_browser.close()