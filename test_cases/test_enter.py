import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import allure
from lib.helper import Helper
from pages.enter_qwallity import Security
from pages.home import Home
from config.config_file import url, email_access, password_access
from data.data_file import email, password


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.positve
@allure.title("Verify that user got the access to system with correct credentional")
@allure.severity(allure.severity_level.CRITICAL)
def test_successful_entering_in_system(get_driver, get_logger):
    helper = Helper(get_driver, get_logger)
    enter_qwallity_obj = Security(get_driver, get_logger)
    home_page_obj = Home(get_driver, get_logger)

    helper.go_to_page(url)
    
    helper.logger.info("test_1 entering system with corecct data")
    enter_qwallity_obj.access_to_system(email_access, password_access)
    
    assert helper.is_redirected_to("/home"), "Redirect to /home did not happen"
    assert home_page_obj.greeting_is_displayed(), "Greeting message is not displayed after accsee to system"


@allure.title("Verify that user cant get the access to system with incorrect credentional")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.negative
@pytest.mark.parametrize(
    "email, password, expected_error",
    [
        (email, password_access, "You don't have access to Qwallity app, please contact administrator!"),
        (email_access, password, "You don't have access to Qwallity app, please contact administrator!"),
        ("", "", "You don't have access to Qwallity app, please contact administrator!"),
    ]
)
def test_negative_entering_in_system(get_driver, get_logger, email, password, expected_error):
    helper = Helper(get_driver, get_logger)
    enter_qwallity_obj = Security(get_driver, get_logger)

    helper.go_to_page(url)
    
    helper.logger.info(f"Test 2: Entering system with incorrect data: email={email}, password={password}")
    enter_qwallity_obj.access_to_system(email, password)

    assert enter_qwallity_obj.get_fail_msg_text() == expected_error, "Fail message is wrong"
    assert enter_qwallity_obj.title_is_displayed(), "Accsess title is not displayed"
    assert enter_qwallity_obj.get_table_title().strip() == "Enter to Qwallity app", "Accsess title text is wrong"




