import pytest
import logging
import datetime
import os.path
from selenium import webdriver
from selenium.webdriver import FirefoxOptions, ChromeOptions, EdgeOptions


def pytest_addoption(parser):
    parser.addoption("--browser", default="Chrome")
    parser.addoption("--maximize", action="store_true", default=True)
    parser.addoption("--log_level", action="store_true", default="DEBUG")


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    maximize = request.config.getoption("--maximize")
    log_level = request.config.getoption("--log_level")

    current_time = str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
    files_dir = os.path.dirname(__file__) + '\\files'

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs\\{request.node.name}_log_{current_time}.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===> Test %s started at %s" % (request.node.name, datetime.datetime.now()))

    if browser_name == "Edge":
        driver = webdriver.Edge()
        options = EdgeOptions()
        options.add_experimental_option('prefs', {
            "download.default_directory": files_dir,
            "download.prompt_for_download": False,
            "safebrowsing.enabled": "false",
            "plugins.always_open_pdf_externally": True
        }
                                        )
    elif browser_name == "Chrome":
        options = ChromeOptions()
        options.add_experimental_option('prefs', {
            "download.default_directory": files_dir,
            "download.prompt_for_download": False,
            "safebrowsing.enabled": "false",
            "plugins.always_open_pdf_externally": True
        }
                                        )
        driver = webdriver.Chrome()
        if maximize:
            driver.maximize_window()
    elif browser_name == "Firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Driver {browser_name} not supported")

    driver.logger = logger

    logger.info("Browser %s started" % browser_name)

    def fin():
        driver.quit()
        logger.info("===> Test %s finished at %s" % (request.node.name, datetime.datetime.now()))

    request.addfinalizer(fin)
    return driver


