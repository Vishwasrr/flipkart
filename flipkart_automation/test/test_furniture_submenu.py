"""test products availability"""
from time import sleep
from library.base_fixtures import DriverInit
from pages.get_furniture_submenus import FurnitureSubMenu

# read = ReadFile()
# element, test_cases = read.read_objects(XL_PATH, TEST_SHEET2)


class TestFurnitureSubMenus(DriverInit):
    """tests availability of products"""

    # @pytest.mark.parametrize("testcase", test_cases)
    def test_sub_menus(self):
        """tests availability of products"""
        obj = FurnitureSubMenu(self.driver)  # pylint:disable=E1101,R0801
        self.driver.implicitly_wait(10)   # pylint:disable=E1101
        obj.click_x()
        sleep(2.5)
        obj.search_bar()
        sleep(2.5)
        obj.search_button()
        sleep(2.5)
        obj.hover_on_menu()
        sleep(2.5)
        obj.grab_sub_menu_items()
