"""test login page"""
from time import sleep
import pytest
from library.base_fixtures import DriverInit
from library.file_library import ReadFile
from config import XL_PATH, TEST_SHEET
from pages.login import Login


read = ReadFile()
element, test_cases = read.read_objects(XL_PATH, TEST_SHEET)


class TestLogin(DriverInit):
    """tests login"""
    @pytest.mark.parametrize("testcase", test_cases)
    def test_launch_url(self, testcase):
        """tests login page"""
        sleep(2.5)
        obj = Login(self.driver, testcase)   # pylint:disable=E1101
        # self.driver.implicitly_wait(5)
        sleep(2.5)
        obj.enter_username()
        sleep(2.5)
        obj.enter_password()
        sleep(2.5)
        obj.click_login()
        sleep(2.5)
