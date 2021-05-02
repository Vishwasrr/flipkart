"""test products availability"""
from time import sleep
from library.base_fixtures import DriverInit
# from config import XL_PATH, TEST_SHEET2
from pages.get_television_sub_menus import TelevisionSubMenu

# read = ReadFile()
# element, test_cases = read.read_objects(XL_PATH, TEST_SHEET2)


class TestTelevisionSubMenus(DriverInit):
    """tests availability of products"""

    # @pytest.mark.parametrize("testcase", test_cases)
    def test_electronic_menus(self):
        """tests availability of products"""
        obj = TelevisionSubMenu(self.driver)    # pylint:disable=E1101
        self.driver.implicitly_wait(10)   # pylint:disable=E1101
        obj.click_x()
        sleep(2.5)
        obj.search_bar()
        sleep(2.5)
        obj.search_button()
        sleep(2.5)
        obj.hover_on_television()
        sleep(2.5)
        obj.grab_sub_menu_items()
