"""test products availability"""
from time import sleep
import pytest
from library.base_fixtures import DriverInit
from library.file_library import ReadFile
from config import XL_PATH, TEST_SHEET2
from pages.search_box import SearchBox

read = ReadFile()
element, test_cases = read.read_objects(XL_PATH, TEST_SHEET2)


class TestProducts(DriverInit):
    """tests availability of products"""

    @pytest.mark.parametrize("testcase", test_cases)
    def test_products(self, testcase):
        """tests availability of products"""
        obj = SearchBox(self.driver, testcase)   # pylint:disable=E1101
        self.driver.implicitly_wait(10)   # pylint:disable=E1101
        obj.x_button()
        sleep(2.5)
        obj.search_bar()
        sleep(2.5)
        obj.search_button()
        sleep(2.5)
        obj.products()
        sleep(2.5)


# tp = TestProducts()
# tp.test_products('test_case1')
# tp.test_products('test_case2')
