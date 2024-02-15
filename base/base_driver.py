import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:                        #   Base-Contains all the common libraries or common methods that will be resusing in our test automation.
    def __init__(self,driver):
        self.driver=driver

    def page_scroll(self):
        # TO scroll to the bottom of the page
        # Get initial page height
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll to the bottom of the page
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait for some time to let new content load
            time.sleep(2)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                # If the scroll height hasn't changed, we've reached the bottom
                break
            last_height = new_height
        time.sleep(2)


    def wait_for_presence_of_all_elements(self,locator_type,locator):
        wait = WebDriverWait(self.driver, 10)
        list_of_elements=wait.until(expected_conditions.presence_of_all_elements_located((locator_type,locator)))
        return list_of_elements

    def wait_element_to_be_clickable(self,locator_type,locator):
        wait = WebDriverWait(self.driver, 10)
        element=wait.until(expected_conditions.element_to_be_clickable((locator_type,locator)))
        return element

