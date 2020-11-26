# An example that prints all CSS of the body element

from selenium import webdriver
from time import sleep

SCRIPT = '''function css(el) {
    var sheets = document.styleSheets, ret = [];
    el.matches = el.matches || el.webkitMatchesSelector;
    for (var i in sheets) {
        try {
            var rules = sheets[i].rules || sheets[i].cssRules;
            for (var r in rules) {
                if (el.matches(rules[r].selectorText)) {
                    ret.push(rules[r].cssText);
                }
            }
        } catch(err) {
            console.log(err);
        }
    }
    return ret;
};

var cssList = css(arguments[0]);

var result = "";
cssList.forEach(function(val){result += val + "\\n";});
return result;
'''

if __name__ == "__main__":
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('enable-automation')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disk-cache-size=0')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.page_load_strategy = 'normal'

    driver = webdriver.Chrome(options=chrome_options)
    driver.set_page_load_timeout(30) # 30 seconds

    driver.get('https://www.giantswarm.io/')
    sleep(5)

    elements = driver.find_elements_by_xpath("//div[contains(@class, 'site-header--mega-menu-aug-2020')]")
    for el in elements:
        output = driver.execute_script(SCRIPT, el)
        print(output)
    
    driver.quit()