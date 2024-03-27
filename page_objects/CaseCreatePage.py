from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class CaseCreate(BasePage):
    CREATE_CASE = (By.XPATH, '//*[@id="app"]/div[1]/ul/li[1]/a/div/i')
    CASE_TITLE = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/section[1]/div[1]/div[5]/span')


    SELECT_SPECIALIZATION = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/section[1]/div[1]/div[6]/div/span')
    TEST_SPEC = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/section[1]/div[1]/div[6]/ul/li[1]')
    VETERINARY_SPEC = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/section[1]/div[1]/div[6]/ul/li[2]')
    HEMATOLOGY_SPEC = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/section[1]/div[1]/div[6]/ul/li[3]')
    GYNECOLOGY_SPEC = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/section[1]/div[1]/div[6]/ul/li[4]')
    EYE_SPEC = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/section[1]/div[1]/div[6]/ul/li[5]')
    HEAD_AND_NECK_SPEC = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/section[1]/div[1]/div[6]/ul/li[6]')
    GASTROINTESTIAL_SPEC = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/section[1]/div[1]/div[6]/ul/li[7]')
    INTRAOPERATIONS_SPEC = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/section[1]/div[1]/div[6]/ul/li[8]')
    SKIN_SPEC = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/section[1]/div[1]/div[6]/ul/li[9]')
    BONES_SPEC = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/section[1]/div[1]/div[6]/ul/li[10]')
    MAMMARY_GLAND_SPEC = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/section[1]/div[1]/div[6]/ul/li[11]')
    GENITOURINARY_SPEC = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/section[1]/div[1]/div[6]/ul/li[12]')
    SOFT_FABRICS_SPEC = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/section[1]/div[1]/div[6]/ul/li[13]')
    SCIENTIFIC_RESEARCH_SPEC = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/section[1]/div[1]/div[6]/ul/li[14]')
    UNKNOWN_SPEC = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/section[1]/div[1]/div[6]/ul/li[15]')
    TUMOR_WITHOUT_AIR_DEFENSE = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/section[1]/div[1]/div[6]/ul/li[16]')
    PEDIATRICS_SPEC = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/section[1]/div[1]/div[6]/ul/li[17]')
    THORACIC_SPEC = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/section[1]/div[1]/div[6]/ul/li[18]')
    CNS_SPEC = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/section[1]/div[1]/div[6]/ul/li[19]')
    CITOLOGY_SPEC = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/section[1]/div[1]/div[6]/ul/li[20]')
    ENDOCRINE_SPEC = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/section[1]/div[1]/div[6]/ul/li[21]')

    SELECT_DATE_OF_BIRTH = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/section[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div/span')
    SELECT_DAY = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/section[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/ul/li[1]')
    SELECT_MONTH = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/section[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/ul/li[1]')
    SELECT_YEAR = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/section[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/ul/li[69]')

    SELECT_GENDER = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/section[1]/div[3]/div[1]/div[1]/div[1]/div[3]')
    MALE_GENDER = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/section[1]/div[3]/div[1]/div[1]/div[1]/div[3]/ul/li[2]')
    FEMALE_GENDER = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/section[1]/div[3]/div[1]/div[1]/div[1]/div[3]/ul/li[3]')

    DESCRIPTION = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/section[1]/div[3]/div[1]/div[3]/span')


    def click_create_case(self):
        self.click(self.CREATE_CASE)

    def input_title_case(self, value):
        self.input_and_submit(self.CASE_TITLE, value)

    def select_spec(self, specialization):
        self.click(self.SELECT_SPECIALIZATION)
        if specialization == 'test':
            self.click(self.TEST_SPEC)
        elif specialization == 'Ветеринария':
            self.click(self.VETERINARY_SPEC)
        elif specialization == 'Гематология':
            self.click(self.HEMATOLOGY_SPEC)
        elif specialization == 'Гинекология':
            self.click(self.GYNECOLOGY_SPEC)
        elif specialization == 'Глазное яблоко':
            self.click(self.EYE_SPEC)
        elif specialization == 'ЖКТ':
            self.click(self.GASTROINTESTIAL_SPEC)
        elif specialization == 'Интраоперационные исследования':
            self.click(self.INTRAOPERATIONS_SPEC)
        elif specialization == 'Кожа':
            self.click(self.SKIN_SPEC)
        elif specialization == 'Кости':
            self.click(self.BONES_SPEC)
        elif specialization == 'Молочные железы':
            self.click(self.MAMMARY_GLAND_SPEC)
        elif specialization == 'Мочеполовая система':
            self.click(self.GENITOURINARY_SPEC)
        elif specialization == 'Мягкие ткани':
            self.click(self.SOFT_FABRICS_SPEC)
        elif specialization == 'Научные исследования':
            self.click(self.SCIENTIFIC_RESEARCH_SPEC)
        elif specialization == 'Неизвестный':
            self.click(self.UNKNOWN_SPEC)
        elif specialization == 'Опухоли без ПВО':
            self.click(self.TUMOR_WITHOUT_AIR_DEFENSE)
        elif specialization == 'Педиатрия':
            self.click(self.PEDIATRICS_SPEC)
        elif specialization == 'Торакальные':
            self.click(self.THORACIC_SPEC)
        elif specialization == 'ЦНС':
            self.click(self.CNS_SPEC)
        elif specialization == 'Цитология':
            self.click(self.CITOLOGY_SPEC)
        elif specialization == 'Эндокринная система':
            self.click(self.ENDOCRINE_SPEC)

    def select_date_of_birth(self):
        self.click(self.SELECT_DATE_OF_BIRTH)
        self.click(self.SELECT_DAY)
        self.click(self.SELECT_MONTH)
        self.click(self.SELECT_YEAR)

    def select_gender(self, gender):
        self.click(self.SELECT_GENDER)
        if gender == 'm':
            self.click(self.MALE_GENDER)
        elif gender == 'f':
            self.click(self.FEMALE_GENDER)

    def fill_description(self, value):
        self.input_and_submit(self.DESCRIPTION, value)
