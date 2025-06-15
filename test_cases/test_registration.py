import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import allure
from lib.helper import Helper
from pages.enter_qwallity import Security
from pages.home import Home
from pages.register import Register
from pages.login import Login
from data.data_file import name, email, username, password, confirm_password
from config.config_file import url, email_access, password_access


@allure.title("Verify that user is registred to system")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_registration(get_driver, get_logger):
    helper = Helper(get_driver, get_logger)
    enter_qwallity_obj = Security(get_driver, get_logger)
    home_page_obj = Home(get_driver, get_logger)
    register_page_obj = Register(get_driver, get_logger)
    login_page_obj = Login(get_driver, get_logger)

    helper.go_to_page(url)

    enter_qwallity_obj.access_to_system(email_access, password_access)
 
    helper.logger.info("test_2 registrtaion in system")
    home_page_obj.click_register()
    
    assert helper.is_redirected_to("/register"), "Redirect to /register did not happen"

    assert register_page_obj.register_title_is_displayed(), "Register title is not displayed"
    assert register_page_obj.get_register_title_text().strip() == "Register", "Register title text is wrong"
    
    register_page_obj.register_in_system(name, email, username, password, confirm_password)

    assert helper.is_redirected_to("/login"), "Redirect to /login did not happen"

    assert login_page_obj.login_title_is_displayed(), "Login title is not displayed"
    assert login_page_obj.get_login_title_text().strip() == "Login", "Login title text is wrong"

    #assert login_page_obj.success_msg_is_displayed(), "Succes message is not displayed after login"
    #assert login_page_obj.get_success_msg_text() == "Your account has been successfully registered.", "Succes message is wrong"

