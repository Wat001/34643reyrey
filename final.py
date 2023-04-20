import re
from selenium import webdriver
import time

url = input("Enter URL to monitor: ")
text_to_check = "(E|e)mir"
ignore_text = "(D|d)emir"

driver = webdriver.Chrome()
driver.get(url)

matched_strings = set()

while True:
    page_source = driver.page_source
    matches = re.findall(text_to_check, page_source)
    for match in matches:
        if match not in matched_strings and not re.search(ignore_text, match):
            print(f"bulundu! {match}")
            matched_strings.add(match)
    time.sleep(0.25)
