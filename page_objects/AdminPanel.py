from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class AdminPanel(BasePage):
    ADMIN_PANEL = (By.XPATH, '//*[@id="app"]/div[1]/ul/li[6]')
    USERS = (By.XPATH, '/html/body/nav/div/ul/li[2]/a')
    CLIENTS = (By.XPATH, '/html/body/nav/div/ul/li[3]/a')
    TEAMS = (By.XPATH, '/html/body/nav/div/ul/li[4]/a')
    INVITES = (By.XPATH, '/html/body/nav/div/ul/li[5]/a')
    CASES = (By.XPATH, '/html/body/nav/div/ul/li[6]/a')
    SPECIALIZATIONS = (By.XPATH, '/html/body/nav/div/ul/li[7]/a')
    STAINS = (By.XPATH, '/html/body/nav/div/ul/li[8]/a')
    REACTIONS = (By.XPATH, '/html/body/nav/div/ul/li[9]/a')
    REFERENCES = (By.XPATH, '/html/body/nav/div/ul/li[10]/a')
    SESSIONS = (By.XPATH, '/html/body/nav/div/ul/li[11]/a')
    FILES = (By.XPATH, '/html/body/nav/div/ul/li[12]/a')
    WEBINARS = (By.XPATH, '/html/body/nav/div/ul/li[13]/a')
    CONSULTATIONS = (By.XPATH, '/html/body/nav/div/ul/li[14]/a')
    METS_COLOR = (By.XPATH, '/html/body/nav/div/ul/li[15]/a')
    CHAT_GROUPS = (By.XPATH, '/html/body/nav/div/ul/li[16]/a')
    ASSISTANT = (By.XPATH, '/html/body/nav/div/ul/li[18]/a')
    PUZZLES = (By.XPATH, '/html/body/nav/div/ul/li[19]/a')
    CORS_DOMAINS = (By.XPATH, '/html/body/nav/div/ul/li[21]/a')

    def click_admin_panel(self):
        self.click(self.ADMIN_PANEL)

    def click_users(self):
        self.click(self.USERS)

    def click_clients(self):
        self.click(self.CLIENTS)

    def click_teams(self):
        self.click(self.TEAMS)

    def click_invites(self):
        self.click(self.INVITES)

    def click_cases(self):
        self.click(self.CASES)

    def click_specializations(self):
        self.click(self.SPECIALIZATIONS)

    def click_stains(self):
        self.click(self.STAINS)

    def click_reactions(self):
        self.click(self.REACTIONS)

    def click_references(self):
        self.click(self.REFERENCES)

    def click_sessions(self):
        self.click(self.SESSIONS)

    def click_files(self):
        self.click(self.FILES)

    def click_webinars(self):
        self.click(self.WEBINARS)

    def click_consultations(self):
        self.click(self.CONSULTATIONS)

    def click_mets_color(self):
        self.click(self.METS_COLOR)

    def click_chat_groups(self):
        self.click(self.CHAT_GROUPS)

    def click_assistant(self):
        self.click(self.ASSISTANT)

    def click_puzzles(self):
        self.click(self.PUZZLES)

    def click_cors_domains(self):
        self.click(self.CORS_DOMAINS)

