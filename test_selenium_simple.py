
import time
from selenium import webdriver

from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path=r"C:\webdriver\chromedriver.exe")
# driver = webdriver.Firefox()
def test_search_example():
    """ Search some phrase in google and make a screenshot of the page. """

    # Open google search page:
    driver.get('https://google.com')

    time.sleep(1)  # just for demo purposes, do NOT repeat it on real projects!

    # Find the field for search text input:
    search_input = driver.find_element(By.NAME, "q")

    # Enter the text for search:
    search_input.clear()
    search_input.send_keys('first test')

    time.sleep(1)  # just for demo purposes, do NOT repeat it on real projects!

    # Click Search:
    search_button = driver.find_element(By.NAME,'btnK')
    search_button.click()

    time.sleep(1)  # just for demo purposes, do NOT repeat it on real projects!

    # Make the screenshot of browser window:
    driver.save_screenshot('result.png')
    driver.quit()