""""fetches television submenus"""
from config import XL_PATH, TELEVISION_LOCS
from expected_values import TELEVISION
from library.web_utils import WebUtils
from library.file_library import ReadFile
web = WebUtils()
read = ReadFile()
element, keys = read.read_objects(XL_PATH, TELEVISION_LOCS)
# driver = webdriver.Chrome(CHROME_PATH, options=chrome_options)
# driver.get(URL)


class TelevisionSubMenu:
    """"fetches television submenus"""  # pylint:disable=R0801
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

    def hover_on_television(self):
        """hovers on electronics menu"""
        web.hover(self.driver, element["television"])

    def grab_sub_menu_items(self):
        """fetches television submenus"""
        sub_menus = web.grab_menus(self.driver, element['sub_menus'])
        sub_menus = [item.text for item in sub_menus]
        # print(sub_menus)
        # print(ELECTRONIC_SUB_MENU)
        if sub_menus == TELEVISION:
            print('All sub menus present')
        else:
            print('Some menu items maybe absent')


# driver.find_element_by_xpath('//button[@class="_2KpZ6l _2doB4z"]').click()
# driver.find_element_by_name("q").send_keys("sony vaio laptop")
# driver.find_element_by_xpath("//button[@type='submit']").click()

# driver.implicitly_wait(5)
# action = ActionChains(driver)
# elem = driver.find_element_by_xpath(
#     "//span[contains(@class,'_2I9KP_')]")
# action.move_to_element(elem).perform()

# sub_menus = driver.find_elements_by_xpath(
#     "//a[@class='_3QN6WI _1MMnri _32YDvl']")
# sub_menus = [item.text for item in sub_menus]
# print(sub_menus)
