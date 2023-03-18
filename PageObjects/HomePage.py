from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    search_results = (By.XPATH, "//div[@class='Truncate-sc-10p6c43-0 flAIvs']")
    cart_button = (By.XPATH, "//a[text()='View cart & check out']") # (By.CSS_SELECTOR, ".styles__PrimaryHeaderLink-sc-srf2ow-1.styles__CartLink-sc-vxcbjb-0.hamxlk.fZoSdJ")

    def searchResults(self):
        return self.driver.find_elements(*HomePage.search_results)

    def goToCheckout(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='View cart & check out']")))
        self.driver.find_element(*HomePage.cart_button).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage

