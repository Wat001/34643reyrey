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
    matched_names = re.findall(text_to_check, page_source)
    filtered_names = [name for name in matched_names if not re.search(ignore_text, name)]
    new_names = set(filtered_names) - matched_usernames
    if new_names:
        print("bulundu!")
        with open("isimler.txt", "a") as f:
            f.write("\n".join(new_names) + "\n")
        matched_usernames |= new_names

    time.sleep(0.25)
