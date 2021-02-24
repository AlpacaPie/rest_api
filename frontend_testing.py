from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(executable_path="/Users/alon/Documents/Selenium/chromedriver",
                          options=chrome_options)

rest_app = 'http://127.0.0.1:5000/users/get_user_data/2'

driver.get(rest_app)
try:
    driver.find_element_by_id('user')
    print('User exists: ', driver.find_element_by_id('user').text)
except NoSuchElementException:
    print('No such id')