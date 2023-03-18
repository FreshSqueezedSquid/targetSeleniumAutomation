from selenium.webdriver.common.by import By



class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    guest_login = (By.XPATH, "//button[@data-test='checkout-button']")
    email = (By.CSS_SELECTOR, "#username")
    password = (By.CSS_SELECTOR, "#password")
    sign_in = (By.CSS_SELECTOR, "#login")

    def guestLogin(self):
        return self.driver.find_element(*CheckoutPage.guest_login)
    # sends email from
    def sendEmail(self):
        return self.driver.find_element(*CheckoutPage.email)
    # sends password from LoginData
    def sendPassword(self):
        return self.driver.find_element(*CheckoutPage.password)

    def signIn(self):
        return self.driver.find_element(*CheckoutPage.sign_in)

