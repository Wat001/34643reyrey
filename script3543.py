from selenium import webdriver
import time
from plyer import notification
import winsound

url = "https://www.roblox.com/groups/3576655/Zombie-Attack-Official#!/about"
text_to_check = "emir"

driver = webdriver.Chrome()
driver.get(url)

while True:
    if text_to_check in driver.page_source:
        print("bulundu!")

        notification.notify(
            title="bulundu!",
            message=f"yazi'{text_to_check}' bulundu{url}.",
            app_name="Webpage Checker"
        )

        duration = 1000
        frequency = 440
        winsound.Beep(frequency, duration)

        # Set a timer to close the notification after 10 seconds
        start_time = time.time()
        while time.time() - start_time < 10:
            time.sleep(1)
        notification.dismiss()

    time.sleep(1)

driver.quit()
