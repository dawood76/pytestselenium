
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re

class product:
    product_details_ui = {}

    def __init__(self, driver):
        self.driver = driver

    def get_mpn(self):
        element = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH,
                                            "/html/body/div[1]/main/div/div/div[3]/section[1]/form/div[2]/div/div[1]/div[1]/h1"))
        )
        mpn = re.findall(r'(?<=\().*?(?=\))',element.text)
        self.product_details_ui['mpn'] = mpn

    def get_price(self):
        element = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div/div[3]/section[1]/form/div[3]/div[3]/div[3]/div[1]/div/div/div/div/ul/li/span[2]/span[1]/span"))
        )
        self.product_details_ui['price'] = element.text.split('£')[1]


    def get_shipping(self):
        element = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH,
                                            "/html/body/div[1]/main/div/div/div[3]/section[1]/form/div[3]/div[3]/div[3]/div[4]/div[3]/div[1]/div/div[1]/div[2]/span"))
        )
        self.product_details_ui['shipping'] = element.text

    def get_make(self):
        make_elem = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[3]/section[1]/form/div[3]/div[3]/div[3]/div[4]/div[4]/div[1]/div/ul[1]/li[6]')
        self.product_details_ui['make'] = make_elem.text.split(": ")[1]

    def get_description(self):
        element = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH,
                                              "/html/body/div[1]/main/div/div/div[3]/section[1]/form/div[3]/div[3]/div[3]/div[4]/div[4]/div[1]/div/ul[1]/li[4]"))
        )
        self.product_details_ui['description'] = element.text

    def accept_permissions(self):
        try:
            element = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.XPATH,
                                                "// *[ @ id = '_ymi0']"))
            )
            element.click()

        except:
            pass

    def get_product_details(self):
        self.accept_permissions()
        self.get_price()
        self.get_make()
        self.get_mpn()
        self.get_shipping()
        self.get_description()
        return self.product_details_ui