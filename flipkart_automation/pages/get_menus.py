"""checking menu lists"""
from config import XL_PATH, LOC_VALS3
from expected_values import MENUS
from library.web_utils import WebUtils
from library.file_library import ReadFile

web = WebUtils()
read = ReadFile()
element, keys = read.read_objects(XL_PATH, LOC_VALS3)


class Menu:
    """checking menu lists"""
    def __init__(self, driver):
        self.driver = driver

    def click_x(self):
        """clicks on x button"""
        web.click_element(self.driver, element['x_button'])

    def grab_all_menus(self):
        """fetches all menus"""
        menus = web.grab_menus(self.driver, element['grab_all_menus'])
        menus = [menu.text for menu in menus]
        if menus == MENUS:
            print('All menus are right')
        else:
            print('Some menus may not be right')
