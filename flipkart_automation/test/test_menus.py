"""test login page"""
from time import sleep
from library.base_fixtures import DriverInit
# from config import XL_PATH, TEST_SHEET
from pages.get_menus import Menu


# read = ReadFile()
# element, test_cases = read.read_objects(XL_PATH, TEST_SHEET)


class TestMenus(DriverInit):
    """tests menu list"""
    # @pytest.mark.parametrize("testcase", test_cases)

    def test_menu(self):
        """tests menu page"""
        sleep(2.5)
        obj = Menu(self.driver)   # pylint:disable=E1101
        # self.driver.implicitly_wait(2.5)
        sleep(2.5)
        obj.click_x()
        sleep(2.5)
        obj.grab_all_menus()
        sleep(2.5)
