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
from pages.home_logged import Home_Logged
from data.data_file import name, email, username, password, confirm_password
from config.config_file import url, email_access, password_access


@allure.title("Verify that user is logged to system")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.positve
def test_registration(get_driver, get_logger):
    helper = Helper(get_driver, get_logger)
    enter_qwallity_obj = Security(get_driver, get_logger)
    home_page_obj = Home(get_driver, get_logger)
    register_page_obj = Register(get_driver, get_logger)
    login_page_obj = Login(get_driver, get_logger)
    logged_home_obj = Home_Logged(get_driver, get_logger)

    helper.go_to_page(url)

    enter_qwallity_obj.access_to_system(email_access, password_access)
    home_page_obj.click_register()
    register_page_obj.register_in_system(name, email, username, password, confirm_password)

    assert helper.is_redirected_to("/login"), "Redirect to /login did not happen"
    assert login_page_obj.login_title_is_displayed(), "Login title is not displayed"
    assert login_page_obj.get_login_title_text().strip() == "Login", "Login title text is wrong"

    helper.logger.info("test_3 log in system")
    login_page_obj.log_in(username, password)
    assert helper.is_redirected_to("/home"), "Redirect to /home did not happen"
    assert logged_home_obj.greating_logged_text_is_displayed(), "Welcome message is not displayed"
    assert logged_home_obj.get_greating_logged_text() == f"Welcome {username}!", "Welcome message text is wrong"

