"""automating buying a product end to end"""
from config import XL_PATH, BUY_PRODUCT_LOCS, BUY_PRODUCT_TESTCASES
from library.file_library import ReadFile
from library.web_utils import WebUtils
web = WebUtils()
read = ReadFile()
element, keys = read.read_objects(XL_PATH, BUY_PRODUCT_LOCS)


class BuyProduct:
    """automating buying a product end to end"""

    def __init__(self, driver, test_case):
        self.driver = driver
        self.test_case = test_case
        self.product, self.price = read.read_data(
            XL_PATH, BUY_PRODUCT_TESTCASES, self.test_case)
        # print(self.product, self.price)

    def click_x(self):
        """clicks on x button"""
        web.click_element(self.driver, element['x_button'])

    def search_box(self):
        """sends value to search box"""
        web.send_string(self.driver, self.product, element['search_box'])

    def search_button(self):
        """clicks on search button"""
        web.click_element(self.driver, element['search_button'])

    def select_product(self):
        """clicks on required product"""
        web.click_element(self.driver, element['select_product'])

    def change_tab(self):
        """switches tab"""
        web.switch_windows(self.driver)

    def scroll(self):
        """scrolls down for element visibility"""
        web.scroll_down(self.driver)

    def price_filter(self):
        """ selects price filter """
        web.select_value_from_box(
            self.driver, self.price, element['price_filter'])

    def rating_filter(self):
        """ selects rating filter """
        web.click_element(self.driver, element['rating_filter'])

    def select_color(self):
        """ chooses color of product """
        web.click_element(self.driver, element['select_color'])

    # def scroll(self):
    #     web.scroll_down(self.driver)

    def select_size(self):
        """ chooses memory size """
        web.click_element(self.driver, element['select_size'])

    def click_buy(self):
        """clicks on buy button """
        web.click_element(self.driver, element['click_buy'])
