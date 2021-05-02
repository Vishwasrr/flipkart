"""automating fashion menu hovering"""
from config import XL_PATH, FASHION_LOCS
from expected_values import FASHION_SUB_MENUS   # pylint:disable=R0801
from library.web_utils import WebUtils
from library.file_library import ReadFile
web = WebUtils()
read = ReadFile()
element, keys = read.read_objects(XL_PATH, FASHION_LOCS)


class FashionSubMenu:
    """fetches fashion submenus"""  # pylint:disable=R0801
    def __init__(self, driver):
        self.driver = driver

    def click_x(self):
        """clicks on x button"""
        web.click_element(self.driver, element['x_button'])

    def hover_on_menu(self):
        """hovers on fashion menu"""
        web.hover(self.driver, element["fashion"])

    def grab_sub_menu_items(self):
        """fetches electronic submenus"""
        sub_menus = web.grab_menus(self.driver, element['sub_menus'])
        sub_menus = [item.text for item in sub_menus]
        if sub_menus == FASHION_SUB_MENUS:
            print('All sub menus present')
        else:
            print('Some menu items maybe absent')


# driver = webdriver.Chrome(CHROME_PATH, options=chrome_options)
# driver.get(URL)
# driver.maximize_window()
# obj = FashionSubMenu(driver)
# obj.click_x()
# sleep(2.5)
# obj.hover_on_menu()
# sleep(2.5)
# obj.grab_sub_menu_items()
