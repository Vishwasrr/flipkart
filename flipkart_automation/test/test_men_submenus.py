"""test products availability"""
from time import sleep
from library.base_fixtures import DriverInit
# from config import XL_PATH, TEST_SHEET2
from pages.get_men_submenus import MenSubMenu

# read = ReadFile()
# element, test_cases = read.read_objects(XL_PATH, TEST_SHEET2)


class TestMenSubMenus(DriverInit):
    """tests availability of products"""

    # @pytest.mark.parametrize("testcase", test_cases)
    def test_men_sub_menus(self):
        """tests availability of products"""
        obj = MenSubMenu(self.driver)   # pylint:disable=E1101,R0801
        self.driver.implicitly_wait(10)   # pylint:disable=E1101,R0801
        obj.click_x()
        sleep(2.5)
        obj.search_bar()
        sleep(2.5)
        obj.search_button()
        sleep(2.5)
        obj.hover_on_menu()
        sleep(2.5)
        obj.grab_sub_menu_items()


"""
errors facing:
test\test_women_submenus.py:1:0: R0801: Similar lines in 7 files
==test.test_baby_submenus:19
==test.test_electronic_menus:21
==test.test_furniture_submenu:18
==test.test_men_submenus:19
==test.test_search_box:21
==test.test_sports_submenu:19
==test.test_television_submenu:19
        sleep(2.5)
        obj.search_bar()
        sleep(2.5)
        obj.search_button()
        sleep(2.5) (duplicate-code)
"""
