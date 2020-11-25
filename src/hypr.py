from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time




chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://stageadmin.hypr.pk/login")
time.sleep(5)
elem = driver.find_element_by_xpath('//input[@placeholder="Email"]')
elem.send_keys("admin@hypr.pk")
elem = driver.find_element_by_xpath('//input[@placeholder="Password"]')
elem.send_keys("12345678")
elem = driver.find_element_by_xpath('//button[text()="Log in"]')
elem.click()
time.sleep(5)
elem = driver.find_element_by_xpath('//a/span[text()="Products"]')
elem.click()
