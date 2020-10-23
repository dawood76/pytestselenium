from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from src.getproductdetailsexcel import get_product_details_from_csv
from src.getproductdetailsui import product;
import json


chrome_options = webdriver.ChromeOptions()
#chrome_options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
product_details_excel = get_product_details_from_csv()

get_product_details_ui = product(driver)
product_details_ui = {}

for mpn in product_details_excel:
    base_url = "https://www.autofixa.com/"
    end_point = mpn + '/p0/'
    url = base_url + end_point
    driver.get(url)
    product_details_ui = get_product_details_ui.get_product_details()
    assert product_details_excel[mpn]['price'] == product_details_ui['price']
    assert product_details_excel[mpn]['description'] == product_details_ui['description']
    assert product_details_excel[mpn]['make'] == product_details_ui['make']
    assert mpn in product_details_ui['mpn']
    print(product_details_ui)













