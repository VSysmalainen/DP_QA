from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class TeamManager(BasePage):
    TEAM_MANAGER = (By.XPATH, '//*[@id="app"]/div[1]/ul/li[2]')

    def click_team_manager(self):
        self.click(self.TEAM_MANAGER)

