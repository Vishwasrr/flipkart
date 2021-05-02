"""automating appliance menu hovering"""
from config import XL_PATH, APP_LOCS
from expected_values import APPLIANCES_SUB_MENUS  # pylint:disable=R0801
from library.web_utils import WebUtils
from library.file_library import ReadFile
web = WebUtils()
read = ReadFile()
element, keys = read.read_objects(XL_PATH, APP_LOCS)


class ApplianceSubMenu:
    """fetches fashion submenus"""  # pylint:disable=R0801
    def __init__(self, driver):
        self.driver = driver

    def click_x(self):
        """clicks on x button"""
        web.click_element(self.driver, element['x_button'])

    def hover_on_menu(self):
        """hovers on appliance menu"""
        web.hover(self.driver, element["appliances"])

    def grab_sub_menu_items(self):
        """fetches appliance submenus"""
        sub_menus = web.grab_menus(self.driver, element['sub_menus'])
        sub_menus = [item.text for item in sub_menus]
        # print(sub_menus)
        # print(ELECTRONIC_SUB_MENU)
        if sub_menus == APPLIANCES_SUB_MENUS:
            print('All sub menus present')
        else:
            print('Some menu items maybe absent')


# driver = webdriver.Chrome(CHROME_PATH, options=chrome_options)
# driver.get(URL)
# driver.maximize_window()
# obj = ApplianceSubMenu(driver)
# obj.click_x()
# sleep(2.5)
# obj.hover_on_menu()
# sleep(2.5)
# obj.grab_sub_menu_items()
