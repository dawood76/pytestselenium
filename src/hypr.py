from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.chrome.options import Options
import time
import os
import pytest

def test_login():
  print("wdddd", os.getcwd())

  chrome_options = Options()
  chrome_options.add_argument("--headless")
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('window-size=1920x1080');
  #chrome_options.add_argument("--disable-setuid-sandbox")
  driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install(), chrome_options=chrome_options)
  #driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)
  driver.get("http://localhost:4200")


  time.sleep(10)

  elem = driver.find_element_by_xpath('//input[@placeholder="Email"]')
  elem.send_keys("admin@hypr.pk")
  elem = driver.find_element_by_xpath('//input[@placeholder="Password"]')
  elem.send_keys("12345678")
  elem = driver.find_element_by_xpath('//button[text()="Log in"]')
  elem.click()
  time.sleep(3)
  print(driver.get_screenshot_as_base64())
  elem = driver.find_element_by_xpath('//a/span[text()="Products"]')
  elem.click()

  print(driver.get_screenshot_as_base64())
