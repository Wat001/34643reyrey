import re
from selenium import webdriver
import time
from plyer import notification
import winsound

url = "https://www.roblox.com/groups/3576655/Zombie-Attack-Official#!/about"
text_to_check = "(E|e)mir"
ignore_text = "(D|d)emir"

driver = webdriver.Chrome()
driver.get(url)

while True:
    page_source = driver.page_source
    if re.search(text_to_check, page_source) and not re.search(ignore_text, page_source):
        print("bulundu!")

        notification.notify(
            title="bulundu!",
            message=f"yazi'{text_to_check}' bulundu{url}.",
            app_name="Webpage Checker",
            timeout=10
        )

        duration = 1000
        frequency = 440
        winsound.Beep(frequency, duration)

    time.sleep(0.25)
