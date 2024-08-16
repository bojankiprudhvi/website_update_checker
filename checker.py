import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from plyer import notification

TIMEOUT = 10  # seconds
def initialize_driver():
    """Initialize the Chrome WebDriver."""
    #options = Options()
    #options.headless = True 
    driver = webdriver.Chrome()
    driver.implicitly_wait(TIMEOUT)
    return driver

def send_notification(title, message):
    print("contect chnaged")
    notification.notify(
        title=title,
        message=message,
        timeout=10  # Notification will disappear after 10 seconds
    )

def get_page_content(url,driver):
    driver.get(url)
    
    # Customize this part based on the structure of the webpage
    content = driver.find_element(By.TAG_NAME, 'body').get_attribute('innerHTML')  # Change 'body' as needed
    #driver.quit()
    time.sleep(10)
    return content

def main(driver):
    url = "https://www.netflix.com/in/"  # Replace with the target website URL
    current_content = get_page_content(url, driver)
    
    try:
        with open("last_context.txt", "r",encoding='utf-8') as f:
            last_context = f.read()
    except FileNotFoundError:
        last_context = ""
    
    if last_context != '':
        # Check if content has changed since the last check
        if current_content != last_context:
            send_notification("Website Update Alert", "New content detected on the webpage!")
            
            with open("last_context.txt", "w",encoding='utf-8') as f:
                f.write(current_content)
    else:
        with open("last_context.txt", "w",encoding='utf-8') as f:
            f.write(current_content)
    
    time.sleep(1)  # Check for changes every 5 minutes

if __name__ == "__main__":
    driver = initialize_driver()
    main(driver)