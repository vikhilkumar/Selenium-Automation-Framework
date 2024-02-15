#Session 48
import time
import pytest
import softest
from pages.Yatra_Launch_page import LaunchPage
from utilities.utils import Utils
from ddt import ddt,data,unpack,file_data

@ddt
@pytest.mark.usefixtures("setup")   #It will call the function fixture from conftest file   #Use of conftest file is It allows you to define fixtures and other configurations that are common across multiple test files or directories within your project
class TestSearchFlights(softest.TestCase):    #softest.TestCase is a soft assertion - that allows you to continue executing a test even after encountering failures.
    log = Utils.custom_logger()
    @pytest.fixture(autouse=True)   #autouse=True indicates that the fixture should be automatically used by all tests in the module without explicitly requesting it in the test function's arguments.
    def class_setup(self):
        self.lp=LaunchPage(self.driver)
        self.ut=Utils()

    #If we want to give the journey details over,we need to use like this
    # @data(("Chennai","New York","21/12/2024","1 Stop"),("mumbai","New York","05/12/2024","2 Stop"))
    # @unpack

    #if want to pass through yaml means we have to give like this
    #@file_data("../testdata/test_data.yaml")  For yaml file, first we need to pip install pyyaml

    # if want to pass through json means we have to give like this
    #@file_data("../testdata/test_data.json")

    ##if want to pass through excel means we have to give like this
    # @data(*Utils.read_data_from_excel("C:\\Users\\vikhi\\PycharmProjects\\Selenium_Automation_Framework_POM\\testdata\\journeyData.xlsx","Sheet1"))
    # @unpack

    ##if want to pass through csv means we have to give like this
    # *-It will tell python list of data will you have to handle it and unpack
    @data(*Utils.read_data_from_csv("C:\\Users\\vikhi\\PycharmProjects\\Selenium_Automation_Framework_POM\\testdata\\tdata.csv"))
    @unpack
    def test_flights(self,goingfrom,goingto,ddate,stops):
        #Launching the webdriver and opening the travel website
        #It will automatically launch the browser using conftest file as source file


        flight_result=self.lp.searchFlights(goingfrom,goingto,ddate)   #since it return obj we have created the variable
        flight_result.filter_flights(stops)
        self.lp.page_scroll()
        self.log.info(len(flight_result.getStopsList()))
        self.ut.assertListItemText(flight_result.getStopsList(), stops)



        # Providing from location
        # lp.departfrom("Mumbai")
        #
        # # Providing going to location
        # lp.goingTo("New York")
        #
        # # To resolve sync issue
        # # To select depature date
        # lp.journyDate("21/12/2024")
        #
        # # click on flight search button
        # lp.clickSearchbtn()


        #Selects the filter 1 stop
        # sf = SearchFlightResults(self.driver)
        # flight_result.filter_flights('2 Stop')

        #TO scroll to the bottom of the page
        # self.lp.page_scroll()



        # alternate xpath for 1 stop -
        # all_stops=driver.find_elements(By.XPATH,"//div//div//div//div//div//div//span[@class='dotted-borderbtm']")
        # self.log.info(len(flight_result.getStopsList()))

        #Verify that the filtered results show flights having only 1 stop
        # self.ut.assertListItemText(flight_result.getStopsList(),"2 Stop")


#Since we are using the pytest framework we no need to call the class obj
