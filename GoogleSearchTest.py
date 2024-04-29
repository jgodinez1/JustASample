import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib3
import time


class GoogleSearchTest(unittest.TestCase):
    def setup(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def test_GoogleSearch(self):
        driver_firefox = webdriver.Firefox()
        self.driver = driver_firefox
        driver_firefox.maximize_window()
        driver_firefox.get('http://www.google.com')

        # perform search
        elem = driver_firefox.find_element(By.NAME, "q")
        elem.send_keys("Zimmer/Medstat")
        elem.submit()
        time.sleep(5)

    def tearDown(self):
        # Close the browser
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
