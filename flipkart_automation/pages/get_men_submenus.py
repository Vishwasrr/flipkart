"""automating men menu hovering"""
from config import XL_PATH, MEN_LOCS
from expected_values import MEN_SUB_MENUS
from library.web_utils import WebUtils
from library.file_library import ReadFile
web = WebUtils()
read = ReadFile()
element, keys = read.read_objects(XL_PATH, MEN_LOCS)


class MenSubMenu:
    """retrieves men submenus"""  # pylint:disable=R0801
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
        """hovers on men menu"""
        web.hover(self.driver, element["men"])

    def grab_sub_menu_items(self):
        """fetches men submenus"""
        sub_menus = web.grab_menus(self.driver, element['sub_menus'])
        sub_menus = [item.text for item in sub_menus]
        if sub_menus == MEN_SUB_MENUS:
            print('All sub menus present')
        else:
            print('Some menu items maybe absent')


# driver = webdriver.Chrome(CHROME_PATH, options=chrome_options)
# driver.get(URL)
# driver.maximize_window()
# obj = MenSubMenu(driver)
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


# driver.find_element_by_xpath('//button[@class="_2KpZ6l _2doB4z"]').click()
# driver.find_element_by_name("q").send_keys("sony vaio laptop")
# driver.find_element_by_xpath("//button[@type='submit']").click()

# driver.implicitly_wait(5)
# action = ActionChains(driver)
# sleep(5)
# # elem = driver.find_element_by_xpath(
# #     "//span[contains(@class,'_2I9KP_')]")   # submenu
# elem = driver.find_element_by_xpath(
#     "//span[text()='Men']")   # submenu
# action.move_to_element(elem).perform()

# sub_menus = driver.find_elements_by_xpath(
#     "//a[@class='_3QN6WI _1MMnri _32YDvl']")
# sub_menus = [item.text for item in sub_menus]
# # for item in sub_menus:
# #     print(item.text)
# print(sub_menus)
