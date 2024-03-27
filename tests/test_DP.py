import pytest
import time
from page_objects.TeamManager import TeamManager
from page_objects.AdminPanel import AdminPanel
from env_tmp import dp_url, dp_user, dp_password


# @pytest.fixture()
# def start_stop():
#     print("start")
#     yield
#     print("stop")


# @pytest.skip
# def test_team_manager(browser, start_stop):
#     page = TeamManager(browser)
#     page.open(dp_url)
#     page.login(dp_user, dp_password)
#     page.click_team_manager()
#     page.switch()
#     page.click_date_range()



# def test_admin_panel(browser):
#     page = AdminPanel(browser)
#     page.open(dp_url)
#     page.login(dp_user, dp_password)
#     page.click_admin_panel()
#     page.switch()
#     page.click_users()
#     page.click_clients()
#     page.click_teams()
#     page.click_invites()
#     page.click_cases()
#     page.click_specializations()
#     page.click_stains()
#     page.click_reactions()
#     page.click_references()
#     page.click_sessions()
#     page.click_files()
#     page.click_webinars()
#     page.click_consultations()
#     page.click_mets_color()
#     page.click_chat_groups()
#     page.click_assistant()
#     page.click_puzzles()
#     page.click_cors_domains()
