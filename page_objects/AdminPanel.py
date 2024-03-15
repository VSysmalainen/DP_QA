from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class AdminPanel(BasePage):
    ADMIN_PANEL = (By.XPATH, '//*[@id="app"]/div[1]/ul/li[6]')
    USERS = (By.XPATH, '/html/body/nav/div/ul/li[2]/a')

    def click_admin_panel(self):
        self.click(self.ADMIN_PANEL)

    def click_users(self):
        self.click(self.USERS)
