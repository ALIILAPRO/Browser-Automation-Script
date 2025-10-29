from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

def human_like_search(search_query):
    options = webdriver.ChromeOptions()
    
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--disable-blink-features=AutomationControlled')
    
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    try:
        print("Opening Google...")
        driver.get("https://www.google.com")
        
        time.sleep(random.uniform(2, 4))
        
        print(f"Searching for: {search_query}")
        search_box = driver.find_element(By.NAME, "q")
    
        for char in search_query:
            search_box.send_keys(char)
            time.sleep(random.uniform(0.1, 0.3))
        
        time.sleep(1)
        search_box.send_keys(Keys.RETURN)
        
        time.sleep(random.uniform(3, 5))
        
        print("Finding the first result...")
        results = driver.find_elements(By.CSS_SELECTOR, "h3")
        if results:
            results[0].click()
            print("Success! First result opened.")
        else:
            print("No results found!")
        
        input("Press Enter to close...")
        
    except Exception as e:
        print(f"Error: {e}")
        input("Press Enter...")
    finally:
        driver.quit()

human_like_search("aliilapro")
