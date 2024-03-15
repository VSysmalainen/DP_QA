from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class TeamManager(BasePage):
    TEAM_MANAGER = (By.XPATH, '//*[@id="app"]/div[1]/ul/li[2]')
    SEARCH_BY_TITLE = (By.XPATH, '//*[@id="app"]/div[2]/div/div[3]/div')
    DATE_RANGE = (By.XPATH, '//*[@id="app"]/div[2]/div/div[1]/div/div/button')

    def click_team_manager(self):
        self.click(self.TEAM_MANAGER)

    def click_date_range(self):
        self.click(self.DATE_RANGE)

    def search_by_title(self, value='test'):
        self.input_and_submit(self.SEARCH_BY_TITLE, value)

