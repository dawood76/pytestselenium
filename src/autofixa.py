from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from src.getproductdetailsexcel import get_product_details_from_csv
from src.product_page_other_sellers import othersellers
from src.getproductdetailsui import product;
import json

chrome_options = webdriver.ChromeOptions()
# chrome_options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
product_details_excel = get_product_details_from_csv()
otherseller = othersellers(driver)

get_product_details_ui = product(driver)
product_details_ui = {}

for mpn in product_details_excel:
    base_url = "https://www.autofixa.com/"
    end_point = mpn + '/p0/'
    if len(product_details_excel[mpn]['sellers_makes']) > 1:
        url = base_url + end_point
        driver.get(url)
        print(mpn)
        product_detail_excel = product_details_excel[mpn]
        #product_detail_excel = sorted(product_detail_excel['sellers_makes'], key=lambda i: i['price'])
        product_details_ui = get_product_details_ui.get_product_details(product_detail_excel)
        otherseller.validate_product_details(product_detail_excel)
    # for seller_make in product_detail['sellers_makes']:

    # assert mpn in product_details_ui['mpn']
    # print(product_details_ui)
