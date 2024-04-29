# import webdriver
from selenium import webdriver
import time

# create webdriver object
driver = webdriver.Firefox()
# get google.co.in
driver.get("https://www.google.com")
time.sleep(5)
driver.close()