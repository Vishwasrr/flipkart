"""automating menu hovering"""
from config import XL_PATH, BABY_LOCS
from expected_values import BABY_SUB_MENUS   # pylint:disable=R0801
from library.web_utils import WebUtils
from library.file_library import ReadFile
web = WebUtils()
read = ReadFile()
element, keys = read.read_objects(XL_PATH, BABY_LOCS)


class BabySubMenu:
    """fetches baby submenus"""  # pylint:disable=R0801

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
        """hovers on baby sub menu"""
        web.hover(self.driver, element["baby"])

    def grab_sub_menu_items(self):
        """fetches baby submenus"""
        sub_menus = web.grab_menus(self.driver, element['sub_menus'])
        sub_menus = [item.text for item in sub_menus]
        # print(sub_menus)
        # print(ELECTRONIC_SUB_MENU)
        if sub_menus == BABY_SUB_MENUS:
            print('All sub menus present')
        else:
            print('Some menu items maybe absent')


# driver = webdriver.Chrome(CHROME_PATH, options=chrome_options)
# driver.get(URL)
# driver.maximize_window()
# obj = BabySubMenu(driver)
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
