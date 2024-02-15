import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.search_flight_results import SearchFlightResults
from utilities.utils import Utils


class LaunchPage(BaseDriver):     #It inheriting from the base package  ..#Base-Contains all the common libraries or common methods that will be resusing in our test automation.
    log = Utils.custom_logger()
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    #locators
    DEPART_FROM_FIELD="#BE_flight_origin_city"
    GOING_TO_FIELD="BE_flight_arrival_city"
    GOING_TO_RESULT_LIST="//div[@class='viewport']//div//div/li"
    SELECT_DATE_FIELD="BE_flight_origin_date"
    ALL_DATES="//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD'][@class!='inActiveTD weekend']"
    SEARCH_BUTTON="(//input[@id='BE_flight_flsearch_btn'])[1]"

    def getDepartFromField(self):
        return self.wait_element_to_be_clickable(By.CSS_SELECTOR, self.DEPART_FROM_FIELD)   #Here we are using self.function call. Since we are inhertating the parent cls base_driver

    def getGoingToField(self):
        return self.wait_element_to_be_clickable(By.ID, self.GOING_TO_FIELD)     #refer base_driver for method call

    def getGoingToResults(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.GOING_TO_RESULT_LIST)

    def getDepatureDateField(self):
        return self.wait_element_to_be_clickable(By.ID, self.SELECT_DATE_FIELD)

    def getAllDatesField(self):
        return self.wait_element_to_be_clickable(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD'][@class!='inActiveTD weekend']"). \
                            find_elements(By.XPATH,"//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD'][@class!='inActiveTD weekend']")

    def getSearchButton(self):
        return self.wait_element_to_be_clickable(By.XPATH,self.SEARCH_BUTTON)

    def departfrom(self,departFromlocation):
        self.getDepartFromField().click()          #Here we are using self.function call. Since we are inhertating the parent cls base_driver
        self.log.info("Clicked on depart from")
        time.sleep(2)
        self.getDepartFromField().send_keys(departFromlocation)
        time.sleep(2)
        self.getDepartFromField().send_keys(Keys.ENTER)

    def goingTo(self,goingTolocation):
        self.getGoingToField().click()     #refer base_driver for method call
        self.log.info("Clicked on going To")
        time.sleep(2)
        self.getGoingToField().send_keys(goingTolocation)
        time.sleep(2)
        arr1 = self.getGoingToResults()
        for ar in arr1:
            if "New York (JFK)" in ar.text:
                ar.click()
                break

    def journyDate(self,journeydate):
        self.getDepatureDateField().click()
        all_dates = self.getAllDatesField()

        for dt in all_dates:
            if dt.get_attribute('data-date')==journeydate:
                dt.click()
                break

    def clickSearchbtn(self):
        self.wait_element_to_be_clickable(By.XPATH, "(//input[@id='BE_flight_flsearch_btn'])[1]").click()
        time.sleep(3)


    def searchFlights(self,departlocation,goingtolocation,depaturedate):
        self.departfrom(departlocation)
        self.goingTo(goingtolocation)
        self.journyDate(depaturedate)
        self.clickSearchbtn()
        search_flights_result=SearchFlightResults(self.driver)
        return search_flights_result



