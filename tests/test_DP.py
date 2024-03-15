import time
from page_objects.TeamManager import TeamManager
from page_objects.AdminPanel import
from env_tmp import dp_url, dp_user, dp_password


def test_team_manager(browser):
    TeamManager(browser).open(dp_url)
    TeamManager(browser).login(dp_user, dp_password)
    TeamManager(browser).click_team_manager()

    time.sleep(4)

