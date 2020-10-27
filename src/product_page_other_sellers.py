from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re


class othersellers():
    product_details_excel = {}

    def __init__(self, driver):
        self.driver = driver

    def click_other_sellers_button(self):
        element = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "/html/body/div[1]/main/div/div/div[3]/section[1]/form/div[3]/div[4]/div/div/a"))
        )
        element.click()

    def get_brand_of_other_seller(self):
        element = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '/html/body/div[1]/main/div/div/div[3]/section[1]/form/div[3]/div[4]/div/div/div/ul/li/form/div[2]/div[1]/img[2]'))
        )
        return element.get_attribute('alt')

    def validate_shipping(self):
        element = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '(//div[@class="status"])[1]/span'))
        )

        if self.product_details_excel['sellers_makes'][0]['price'] == self.product_details_excel['sellers_makes'][1][
            'price']:
            brand = self.get_brand_of_other_seller()
            for seller in self.product_details_excel['sellers_makes']:
                if seller['brand'] == brand:

                    if int(float(self.product_details_excel['sellers_makes'][0]['shipping'])) == 0.00:
                        assert element.text == "Free"
                    else:
                        assert element.text.split('£')[1] == seller['price']

        assert self.product_details_excel['sellers_makes'][1]['shipping'] == element.text.split('£')[1]

    def validate_price(self):
        element = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH,
                                              "/html/body/div[1]/main/div/div/div[3]/section[1]/form/div[3]/div[4]/div/div/div/ul/li/form/div[2]/div[3]/div/h4/span/span[1]/span"))
        )
        price = element.text.split('£')[1]
        price = price.replace(',', '')
        assert float(self.product_details_excel['sellers_makes'][1]['price']) == float(price)

    def validate_quantity(self, product):
        quantity = self.product_details_excel['sellers_makes'][1]['qty']
        if int(quantity) > 0:
            element = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.XPATH,
                                                  '(//div[@class="quinity-block form-inline"]/input)[2]'))
            )
            element.clear()
            element.send_keys(int(quantity) + 1)

    def validate_product_details(self, product):
        self.product_details_excel = product
        self.click_other_sellers_button()
        # self.validate_quantity(product)
        self.validate_price()
        self.validate_shipping()
        pass
