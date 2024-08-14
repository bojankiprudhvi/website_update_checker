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
    
    return content

def main(driver):
    url = "https://www.example.com"  # Replace with the target website URL
    last_content = ""
    
    while True:
        current_content = get_page_content(url,driver)
        
        # Check if content has changed since the last check
        if current_content != last_content:
            send_notification("Website Update Alert", "New content detected on the webpage!")
            last_content = current_content
        
        time.sleep(10)  # Check for changes every 5 minutes

if __name__ == "__main__":
    driver = initialize_driver()
    main(driver)