import re
from selenium import webdriver
import time

url = input("Enter URL to monitor: ")
text_to_check = "^(E|e)mir.*"
ignore_text = "(D|d)emir.*"
output_file = input("Dosya yolu: ")

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
        with open(output_file, "a", encoding="utf-8") as f:
            for name in new_names:
                f.write(name + "\n")
        matched_usernames |= new_names

    time.sleep(0.25)
