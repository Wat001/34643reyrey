from selenium import webdriver
import time
from plyer import notification
import winsound

url = "https://www.roblox.com/groups/3576655/Zombie-Attack-Official#!/about"
text_to_check= "emir"

driver = webdriver.Chrome()

while True:
    driver.get(url)
    time.sleep(2)
    
    if text_to_check in driver.page_source:
        print("bulundu!")
        
        notification.notify(
            title="bulundu!",
            message=f"yazi'{text_to_check}' bulundu{url}.",
            app_name="Isım aratici",
            timeout=10
        )
        
        duration = 1000
        frequency = 440
        winsound.Beep(frequency, duration)
        
        break
    
    time.sleep(1)

driver.quit()
