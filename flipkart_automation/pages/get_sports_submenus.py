"""automating sports menu hovering"""
from config import XL_PATH, SPORTS_LOCS
from expected_values import SPORTS_SUB_MENUS
from library.web_utils import WebUtils
from library.file_library import ReadFile
web = WebUtils()
read = ReadFile()
element, keys = read.read_objects(XL_PATH, SPORTS_LOCS)


class SportsSubMenu:
    """extracts sports submenu"""  # pylint:disable=R0801

    def __init__(self, driver):
        self.driver = driver

    def click_x(self):
        """clicks on x button"""   # pylint:disable=R0801
        web.click_element(self.driver, element['x_button'])

    def search_bar(self):
        """sends value to search box"""
        web.send_string(self.driver, 'sony vaio', element['search_bar'])

    def search_button(self):
        """clicks on search button"""
        web.click_element(self.driver, element['search_button'])

    def hover_on_menu(self):
        """hovers on sports menu"""
        web.hover(self.driver, element["sports"])

    def grab_sub_menu_items(self):
        """fetches electronic submenus"""
        sub_menus = web.grab_menus(self.driver, element['sub_menus'])
        sub_menus = [item.text for item in sub_menus]

        if sub_menus == SPORTS_SUB_MENUS:
            print('All sub menus present')
        else:
            print('Some menu items maybe absent')


# driver = webdriver.Chrome(CHROME_PATH, options=chrome_options)
# driver.get(URL)
# driver.maximize_window()
# obj = SportsSubMenu(driver)
# # self.driver.implicitly_wait(10)
# obj.click_x()

# sleep(2.5)
# obj.search_bar()
# sleep(2.5)
# obj.search_button()
# sleep(2.5)
# obj.hover_on_menu()
# sleep(2.5)
# obj.grab_sub_menu_items()
