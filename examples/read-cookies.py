# A selenium example that loads www.google.com and shows which cookies have been set.

import shutil
import sqlite3
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import TimeoutException

USERDIR = '/opt/chrome-userdir'

if __name__ == "__main__":
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('enable-automation')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disk-cache-size=0')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument(f'--user-data-dir={USERDIR}')
    chrome_options.page_load_strategy = 'normal'

    shutil.rmtree(USERDIR, ignore_errors=True)

    driver = webdriver.Chrome(options=chrome_options)
    driver.set_page_load_timeout(30) # 30 seconds

    print('Loading test page and waiting for some time...')
    driver.get('https://www.google.com/')
    
    sleep(3)
    driver.quit()
    sleep(3)

    cookies = []
    db = sqlite3.connect(f'{USERDIR}/Default/Cookies')
    db.row_factory = sqlite3.Row
    c = db.cursor()
    c.execute("SELECT * FROM cookies")
    for row in c.fetchall():
        cookies.append(dict(row))
    c.close()
    db.close()

    print(f'The server set the following {len(cookies)} cookie(s):')
    for c in cookies:
        print(c)
