import time
from page_objects.TeamManager import TeamManager
from page_objects.AdminPanel import AdminPanel
from env_tmp import dp_url, dp_user, dp_password


def test_team_manager(browser):
    page = TeamManager(browser)
    page.open(dp_url)
    page.login(dp_user, dp_password)
    page.click_team_manager()
    page.switch()
    page.click_date_range()



def test_admin_panel(browser):
    page = AdminPanel(browser)
    page.open(dp_url)
    page.login(dp_user, dp_password)
    page.click_admin_panel()
    page.switch()
    page.click_users()
