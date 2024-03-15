from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    __USERNAME = (By.XPATH, '//*[@id="app"]/div[1]/div/form/div[1]/input')
    __PASSWORD = '//*[@id="app"]/div[1]/div/form/div[2]/input'
    __LOGIN_BUTTON = '//*[@id="app"]/div[1]/div/form/button'


    def __init__(self, driver, wait=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait)
        self.actions = ActionChains(driver)
        self.logger = driver.logger
        self.class_name = type(self).__name__

    def open(self, url):
        self.logger.info("%s: Opening url: %s" % (self.class_name, url))
        self.driver.get(url)

    def login(self, username, password):
        self.logger.info("%s: Login as user: %s" % (self.class_name, username))
        self.wait.until(EC.element_to_be_clickable(self.__USERNAME)).send_keys(username)
        self.driver.find_element(By.XPATH, self.__PASSWORD).send_keys(password)
        self.driver.find_element(By.XPATH, self.__LOGIN_BUTTON).click()

    def click(self, locator):
        self.logger.info("%s: Clicking element^ %s" % (self.class_name, str(locator)))
        self.wait.until(EC.element_to_be_clickable(locator)).click()
