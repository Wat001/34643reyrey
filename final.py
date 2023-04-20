import re
from selenium import webdriver
import time

url = "https://www.roblox.com/groups/3576655/Zombie-Attack-Official#!/about"
text_to_check = r"\b[eE][mM][iI][rR]\b"
ignore_text = "(D|d)emir"

driver = webdriver.Chrome()
driver.get(url)

while True:
    page_source = driver.page_source
    matches = re.findall(text_to_check, page_source)
    for match in matches:
        if not re.search(ignore_text, match):
            print(f"bulundu! '{match}'")
            
    time.sleep(0.25)
