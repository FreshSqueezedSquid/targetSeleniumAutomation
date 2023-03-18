import time
import pytest
from selenium.webdriver.common.by import By
from PageObjects.HomePage import HomePage
from TestData.LoginData import LoginData
from TestData.SearchData import SearchData
from utilities.BaseClass import BaseClass
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestTarget(BaseClass):

    def test_groceryShopping(self, getData, loginData):
        log = self.getLog()
        wait = WebDriverWait(self.driver, 15)
        log.info("Searching for first item: BREAD")
        time.sleep(2)

        self.searchItem(getData["item1"])
        time.sleep(1.4)
        self.clickSearch()
        self.findItem(getData["item1"])
        log.info("BREAD was found and added to cart")
        wait.until(EC.element_to_be_clickable((By.XPATH, ".//button[@aria-label='close']")))
        self.continueShopping()

        time.sleep(2)
        self.clearSearch()
        log.info("Searching for second item: MILK")

        time.sleep(2.4)
        self.searchItem(getData["item2"])
        time.sleep(2)
        self.clickSearch()
        self.findItem(getData["item2"])
        log.info("MILK was found and added to cart")
        wait.until(EC.element_to_be_clickable((By.XPATH, ".//button[@aria-label='close']")))
        self.continueShopping()

        time.sleep(3)
        self.clearSearch()
        log.info("Searching for third item: EGG")
        time.sleep(1.8)

        self.searchItem(getData["item3"])
        time.sleep(3)
        self.clickSearch()
        self.findItem(getData["item3"])
        log.info("EGG was found and added to cart")

        self.scrollDown()

        checkoutPage = HomePage.goToCheckout(self)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-test='checkout-button']")))
        checkoutPage.guestLogin().click()
        log.info("Sending email now")
        time.sleep(2.5)
        checkoutPage.sendEmail().send_keys(loginData["email"])
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#password")))
        time.sleep(3)
        log.info("Sending password now")
        checkoutPage.sendPassword().send_keys(loginData["password"])
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#login")))
        time.sleep(1)
        checkoutPage.signIn().click()
        # will fail right here, as methinks site detects when bots are trying to buy things automatically
        # "Checkout" will not become visible within given time frame
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkout-header")))

    @pytest.fixture(params=SearchData.test_search_data)
    def getData(self, request):
        return request.param

    @pytest.fixture(params=LoginData.test_login_data)
    def loginData(self, request):
        return request.param
