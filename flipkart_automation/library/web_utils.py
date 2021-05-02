"""Has generic methods to take care of sending values and clicking elements"""
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException


class WebUtils:
    """Has generic methods to take care of sending values and clicking elements"""
    @staticmethod
    def click_element(driver, element):
        """clicks on the receieved elements"""
        loc_type, loc_value = element
        driver.find_element(loc_type, loc_value).click()

    @staticmethod
    def send_string(driver, string, element):
        """recieves elements, unpacks them into loc_value and loc_type and sends the obtained string
        as a value to be filled in the element"""
        loc_type, loc_value = element
        driver.find_element(loc_type, loc_value).send_keys(Keys.CONTROL+'a')
        driver.find_element(loc_type, loc_value).send_keys(Keys.DELETE)
        driver.find_element(loc_type, loc_value).send_keys(string)

    @staticmethod
    def hover(driver, element):
        """hovers on drop menu"""
        actions = ActionChains(driver)
        loc_type, loc_val = element
        elem = driver.find_element(loc_type, loc_val)
        actions.move_to_element(elem).perform()

    @staticmethod
    def grab_menus(driver, element):
        """grabs all the menus in the pages"""
        loc_type, loc_value = element
        menus = driver.find_elements(loc_type, loc_value)
        return menus

    @staticmethod
    def element_exists(driver, element):  # pylint: disable="(inconsistent-return-statements)"
        """clicks on the receieved elements"""
        loc_type, loc_value = element
        # print(element)
        try:
            elem = driver.find_element(loc_type, loc_value)
            # print(elem.text)
            if elem:
                return True
        except NoSuchElementException:
            return False

    @staticmethod
    def switch_windows(driver):
        """shifts control to new tab"""
        handles = driver.window_handles
        driver.switch_to.window(handles[1])

    @staticmethod
    def scroll_down(driver):
        """scrolls web page according to direction"""
        actions = ActionChains(driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()

    @staticmethod
    def select_value_from_box(driver, value, element):
        """selects a value from box"""
        loc_type, loc_value = element
        prices = driver.find_element(loc_type, loc_value)
        # _by_xpath(
        #     "(//select[contains(@class,'_2YxCDZ')])[2]")
        select = Select(prices)
        select.select_by_value(str(int(value)))

 # pylint: disable="(inconsistent-return-statements)"
