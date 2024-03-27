import time
from page_objects.CaseCreatePage import CaseCreate
from env_tmp import dp_url, dp_user, dp_password, db_params_dp
from query import QueryExecutor


case_title = 'test_case_01'
test_description = f'''
Test description for {case_title}.
Some text.
'''
gender = 'm'

specialization = 'ЖКТ'
'''
Specializations:
test, Ветеринария, Гематология, Гинекология, Глазное яблоко, ЖКТ, 
Интраоперационные исследования, Кожа, Кости, Молочные железы, Мочеполовая система, 
Мягкие ткани, Научные исследования, Неизвестный', Опухоли без ПВО, Педиатрия, 
Торакальные, ЦНС, Цитология, Эндокринная система
'''

query_executor_dp = QueryExecutor(db_params_dp)


# def test_case_create(browser):
#     page = CaseCreate(browser)
#     page.open(dp_url)
#     page.login(dp_user, dp_password)
#     # page.click_create_case()
#     page.input_title_case(case_title)
#     page.select_gender(gender)
#     page.select_date_of_birth()
#     page.select_spec(specialization)
#     page.fill_description(test_description)
#     time.sleep(5)


case_dp_qa = f"""
SELECT * FROM cases WHERE title = '{case_title}'
"""
case_result = (query_executor_dp.execute_query(case_dp_qa))[0]


def test_db_title():
    assert case_result[1] == case_title


def test_db_specialization():
    assert case_result[8] == case_title


def test_db_gender():
    assert case_result[10] == gender



