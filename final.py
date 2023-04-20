import re
from selenium import webdriver
import time

url = input("Enter URL to monitor: ")
text_to_check = "(E|e)mir.*"
ignore_text = "(D|d)emir.*"

driver = webdriver.Chrome()
driver.get(url)

matched_usernames = set()

while True:
    page_source = driver.page_source
    matched_names = re.finditer(text_to_check, page_source)
    new_names = set()
    for name in matched_names:
        name = name.group()
        if not re.search(ignore_text, name):
            if name not in matched_usernames:
                new_names.add(name)
    if new_names:
        print("bulundu!")
        with open("isimler.txt", "a") as f:
            f.write("\n".join(new_names) + "\n")
        matched_usernames |= new_names

    time.sleep(0.25)
