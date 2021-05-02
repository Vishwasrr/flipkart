"""Login automation page"""
from library.file_library import ReadFile
from library.web_utils import WebUtils
from config import XL_PATH, LOCATOR_VALS, TEST_SHEET

web = WebUtils()
read = ReadFile()
element, keys = read.read_objects(XL_PATH, LOCATOR_VALS)
# driver.implicitly_wait(5)


class Login:
    """login"""
    def __init__(self, driver, test_case):
        self.driver = driver
        self.test_case = test_case
        self.username, self.password = read.read_data(
            XL_PATH, TEST_SHEET, self.test_case)

    def enter_username(self):
        """user"""
        web.send_string(self.driver, self.username, element['enter_username'])

    def enter_password(self):
        """password"""
        web.send_string(self.driver, self.password, element['enter_password'])

    def click_login(self):
        """click on login button"""
        web.click_element(self.driver, element['click_login'])

    # def close_window(self):
    #     driver.close()
