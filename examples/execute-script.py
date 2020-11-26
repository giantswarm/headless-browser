# A selenium example that prints the user-agent string of this browser

from selenium import webdriver

if __name__ == "__main__":
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('enable-automation')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--user-data-dir=/opt/chrome-userdir")
    
    driver = webdriver.Chrome(options=chrome_options)

    user_agent = driver.execute_script("return navigator.userAgent;")
    print(f'User agent: {user_agent}')
