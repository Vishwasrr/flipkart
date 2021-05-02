"""test products availability"""
from time import sleep
import pytest
from config import XL_PATH, BUY_PRODUCT_TESTCASES
from pages.buy_product import BuyProduct
from library.base_fixtures import DriverInit
from library.file_library import ReadFile

read = ReadFile()
element, test_cases = read.read_objects(XL_PATH, BUY_PRODUCT_TESTCASES)


class TestBuyProduct(DriverInit):
    """tests availability of products"""
    @pytest.mark.parametrize("testcase", test_cases)
    def test_buy_product(self, testcase):
        """tests availability of products"""
        obj = BuyProduct(self.driver, testcase)   # pylint:disable=E1101
        self.driver.implicitly_wait(10)  # pylint:disable=E1101
        obj.click_x()
        sleep(2.5)
        obj.search_box()
        sleep(2.5)
        obj.search_button()
        sleep(2.5)
        obj.price_filter()
        sleep(2.5)
        obj.rating_filter()
        sleep(2.5)
        obj.select_product()
        sleep(2.5)
        obj.change_tab()
        sleep(2.5)
        obj.scroll()
        sleep(2.5)
        obj.select_color()
        sleep(2.5)
        obj.scroll()
        sleep(2.5)
        obj.select_size()
        sleep(2.5)
        obj.click_buy()
        sleep(2.5)
