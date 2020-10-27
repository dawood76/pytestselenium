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
base_url = "https://www.autofixa.com/"
driver.get(base_url)
get_product_details_ui.accept_permissions()
count = 0
skip_rows = 1000
rows_skipped = 0
for mpn in product_details_excel:

    if rows_skipped != skip_rows :
        rows_skipped = rows_skipped + 1
        continue


    end_point = mpn + '/p0/'
    if len(product_details_excel[mpn]['sellers_makes']) > 1 and product_details_excel[mpn]['superseded_mpn']=='' :
        url = base_url + end_point
        driver.get(url)

        print(mpn)
        count = count + 1
        print(count)
        product_detail_excel = product_details_excel[mpn]
        product_detail_excel['sellers_makes'] = sorted(product_detail_excel['sellers_makes'], key=lambda i: i['price'])
        product_details_ui = get_product_details_ui.get_product_details(product_detail_excel)
        assert mpn in get_product_details_ui.get_heading()
        otherseller.validate_product_details(product_detail_excel)

        # assert mpn in product_details_ui['mpn']
