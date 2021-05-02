"""auotomates search box"""
from library.file_library import ReadFile
from library.web_utils import WebUtils
from config import XL_PATH, LOC_VALS2, TEST_SHEET2
web = WebUtils()
read = ReadFile()
element, keys = read.read_objects(XL_PATH, LOC_VALS2)
# print(element)
# print(keys)


class SearchBox:
    """search box"""

    def __init__(self, driver, test_case):
        self.driver = driver
        self.test_case = test_case
        self.search_item = read.read_data(
            XL_PATH, TEST_SHEET2, self.test_case)
        # print(self.search_item)

    def x_button(self):
        """ click on x button """
        web.click_element(self.driver, element['x_button'])

    def search_bar(self):
        """send string to search bar"""
        web.send_string(self.driver, self.search_item, element['search_bar'])

    def search_button(self):
        """click on search"""
        web.click_element(self.driver, element['search_button'])

    def products(self):
        """displays products if available"""
        exists = web.element_exists(self.driver, element['products'])
        print(self.driver.title)
        if exists:
            print('Product not avaialable')
        else:
            print('Product available')


# driver = webdriver.Chrome(CHROME_PATH)
# driver.get(URL)
# driver.implicitly_wait(10)
# l = SearchBox(driver, 'test_case1')
# l.x_button()
# sleep(2.5)
# l.search_bar()
# sleep(2.5)
# l.search_button()
# sleep(2.5)
# l.products()
# sleep(2.5)
# l = SearchBox(driver, 'test_case2')
# # l.x_button()
# sleep(2.5)
# l.search_bar()
# sleep(2.5)
# l.search_button()
# sleep(2.5)
# l.products()
# sleep(2.5)
# products unavaiable = //div[@class='_3uTeW4']
# products avaiable = //a[@class='s1Q9rs']
# driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
# driver.find_element_by_name("q").send_keys(
#     "sony vaio laptop i2.5 generation")
# driver.find_element_by_xpath("//button[@type='submit']").click()
# sleep(2.5)
# products = driver.find_elements_by_xpath(
#     "//a[@class='s1Q9rs']")
# if products:
# s1Q9rs
