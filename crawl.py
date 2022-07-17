from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from datetime import datetime
import json
import glob

# outbreakinfo_mutation_report_data_2021-05-14.json

today = datetime.now().strftime('%Y-%m-%d')

# Chrome web driver in Incognito mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

# Fill in the path to where you want the downloads to go
download_path = "DOWNLOAD PATH"
# Fill in the path to where the chrome driver for Selenium is
driver_path = "CHROME DRIVER PATH"

download_loc = download_path + 'outbreakinfo_mutation_report_data_' + today + '.json'

# Set download location
prefs = {"download.default_directory": download_path}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(driver_path, options=chrome_options)

post_codes = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
              'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI',
              'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH',
              'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

variants = ['B.1.1.7', 'B.1.351', 'P.1', 'B.1.427', 'B.1.429']

os.chdir(download_path)

combined = []
for p in post_codes:
    url = "https://outbreak.info/location-reports?loc=USA_US-" + p + "&pango=B.1.1.7"
    for v in variants:
        url += '&selected=' + v
    driver.get(url)

    time.sleep(7)
    els = driver.find_elements_by_class_name("download-btn")
    while not els:
        time.sleep(2)
        els = driver.find_elements_by_class_name("download-btn")
    el = els[-1]
    el.click()

    time.sleep(2)
    els = driver.find_elements_by_class_name("focustext")
    el = els[2]
    el.click()
    time.sleep(5)

    rename_loc = download_path + 'outbreak_' + p + '_' + today + '.json'
    os.rename(download_loc, rename_loc)

driver.quit()

for p in post_codes:
    rename_loc = download_path + 'outbreak_' + p + '_' + today + '.json'
    result = []

    for f in glob.glob(rename_loc):
        with open(f, "rb") as infile:
            result = json.load(infile)

    for r in result:
        combined.append(r)

with open('outbreak_combined_us_state_data.json', 'w') as fout:
    json.dump(combined, fout)

