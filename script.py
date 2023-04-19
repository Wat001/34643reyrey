driver.get(url)

while True:
    if text_to_check in driver.page_source:
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
        
        break
    
    time.sleep(1)
