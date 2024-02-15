import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from base.base_driver import BaseDriver
from utilities.utils import Utils


class SearchFlightResults(BaseDriver):   #It inheriting from base_driver file ,If we want to use that page scroll we can use anywhere
    log=Utils.custom_logger()
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locator
    SEARCH_FLIGHT_RESULTS_BY_ONESTOP="//p[normalize-space()='1']"
    SEARCH_FLIGHT_RESULTS_BY_TWOSTOP="//p[normalize-space()='2']"
    SEARCH_FLIGHT_RESULTS_BY_NONSTOP="//p[normalize-space()='0']"
    FLIGHTS_STOPS_LIST="//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]"

    def getSearchFlightResult_by_onestop(self):
        return self.wait_element_to_be_clickable(By.XPATH,self.SEARCH_FLIGHT_RESULTS_BY_ONESTOP)
    def getSearchFlightResult_by_twostop(self):
        return self.wait_element_to_be_clickable(By.XPATH,self.SEARCH_FLIGHT_RESULTS_BY_TWOSTOP)
    def getSearchFlightResult_by_Nonstop(self):
        return self.wait_element_to_be_clickable(By.XPATH,self.SEARCH_FLIGHT_RESULTS_BY_NONSTOP)
    def getStopsList(self):
        return self.wait_for_presence_of_all_elements(By.XPATH,self.FLIGHTS_STOPS_LIST)

    def filter_flights(self,by_stop):
        if by_stop=="1 Stop":
            self.getSearchFlightResult_by_onestop().click()
            self.log.warning("selected flights with one stop")
            time.sleep(2)
        elif by_stop=="2 Stop":
            self.getSearchFlightResult_by_twostop().click()
            self.log.warning("selected flights with two stop")
            self.log.info("selected flights with two stop info")
            self.log.warn("selected flights with two stop warn")
            self.log.debug("selected flights with two stop debug")
            self.log.error("selected flights with two stop error")
            self.log.critical("selected flights with two stop critical")
            time.sleep(2)
        elif by_stop=="Non Stop":
            self.getSearchFlightResult_by_Nonstop().click()
            self.log.warning("selected flights with Non stop")
            time.sleep(2)
        else:
            self.log.warning("Please provide valid stop")





#super keywork eg

# class Parent:
#     def __init__(self, name):
#         self.name = name
#
#     def greet(self):
#         print(f"Hello, {self.name}!")
#
# class Child(Parent):
#     def __init__(self, name, age):
#         super().__init__(name)  # Call the constructor of the Parent class
#         self.age = age
#
#     def greet(self):
#         super().greet()  # Call the greet() method of the Parent class
#         print(f"You are {self.age} years old.")
#
# # Creating an instance of the Child class
# child = Child("Alice", 10)
# child.greet()
