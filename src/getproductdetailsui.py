from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import re


class product:
    product_details_ui = {}

    def __init__(self, driver):
        self.product_details_excel = {}
        self.driver = driver

    def get_heading(self):
        element = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH,
                                              "/html/body/div[1]/main/div/div/div[3]/section[1]/form/div[2]/div/div[1]/div[1]/h1"))
        )

        return element.text

    def validate_price(self):

        element = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH,
                                              "/html/body/div[1]/main/div/div/div[3]/section[1]/form/div[3]/div[3]/div[3]/div[1]/div/div/div/div/ul/li/span[2]/span[1]/span"))
        )
        price = element.text.split('£')[1]
        price = price.replace(',','')
        assert float(self.product_details_excel['sellers_makes'][0]['price']) == float(price)


    def get_shipping(self):
        element = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '(//div[@class="status"]/span)[1]'))
        )

        return element.text

    def validate_shipping(self):
        shipping = self.get_shipping()
        if int(float(self.product_details_excel['sellers_makes'][0]['shipping'])) == 0.00:
            assert shipping == "Free"

        else:
            assert float(self.product_details_excel['sellers_makes'][0]['shipping']) == float(shipping.split('£')[1])

    def get_make(self):
        element = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '//li[contains(text(), "Make")]'))
        )

        self.product_details_ui['make'] = element.text.split(": ")[1]

    def get_description(self):
        element = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH,
                                              "/html/body/div[1]/main/div/div/div[3]/section[1]/form/div[3]/div[3]/div[3]/div[4]/div[4]/div[1]/div/ul[1]/li[4]"))
        )
        self.product_details_ui['description'] = element.text

    def validate_suprseded_message(self):
        # if the mpn has been superseded , price will not be shown ,and superceded mpm will be shown.
        element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//li[@class="supersession__messages-li"]'))
        )
        assert element.text == 'This part has been superseded (replaced)\nby part number ' + \
               self.product_details_excel['superseded_mpn']

    def accept_permissions(self):
        try:
            element = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "// *[ @ id = '_ymi0']"))
            )
            element.click()

        except:
            pass

    def validate_quantity(self):
        quantity = self.product_details_excel['sellers_makes'][0]['qty']
        if int(quantity) > 0:
            element = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.XPATH,
                                                  "/html/body/div[1]/main/div/div/div[3]/section[1]/form/div[3]/div[3]/div[3]/div[1]/div/div[2]/div[1]/div/input"))
            )
            element.clear()
            element.send_keys(int(quantity) + 1)

            element = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/html/body/div[1]/main/div/div/div[3]/section[1]/form/div[3]/div[3]/div[3]/div[1]/div/div[2]/div[2]/div/div/div[1]/button"))
            )

            self.driver.execute_script("arguments[0].click();", element)

            element = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.XPATH,
                                                  "/html/body/div[1]/main/div/div/div[3]/section[1]/form/div[3]/div[3]/div[3]/div[1]/div/div[3]/div"))
            )

            assert element.text == 'Maximum Quantity available is ' + quantity

        else:
            element = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.XPATH,
                                                  '//*[@id="product_addtocart_form"]/div[3]/div[3]/div[3]/div[3]/div[1]/span'))
            )
            assert element.text == 'Out Of Stock'
            element = self.driver.find_element_by_xpath(
                '/html/body/div[1]/main/div/div/div[3]/section[1]/form/div[3]/div[3]/div[3]/div[3]/div[3]/button/span')
            assert element.text == 'ENQUIRE'

    def get_product_details(self, product):
        # product with the lowest price is at the 0th index
        self.product_details_excel = product
        if self.product_details_excel['superseded_mpn'] is '':
            self.validate_price()
            # self.get_make()
            self.validate_quantity()

        else:
            self.validate_suprseded_message()
        self.validate_shipping()
        # self.get_description()
        return self.product_details_ui
