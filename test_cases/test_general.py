import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.helper import Helper
from pages.enter_qwallity import Security
from pages.home import Home
from pages.register import Register
from pages.login import Login
from pages.home_logged import Home_Logged
from data.data_file import name, email, username, password, confirm_password
from config.config_file import email_access, password_access, url


def test_generaling(get_driver, get_logger):
    helper = Helper(get_driver, get_logger)
    enter_qwallity_obj = Security(get_driver, get_logger)
    home_page_obj = Home(get_driver, get_logger)
    register_page_obj = Register(get_driver, get_logger)
    login_page_obj = Login(get_driver, get_logger)
    #home_logged_obj = Home_Logged(driver)

    helper.go_to_page(url)
    
    helper.logger.info("test_1 entering system")
    enter_qwallity_obj.access_to_system(email_access, password_access)
    
    helper.logger.info("test_2 registrtaion in system")
    home_page_obj.click_register()

    assert helper.is_redirected_to("/register"), "Redirect to /register did not happen"
    register_page_obj.register_in_system(name, email, username, password, confirm_password)

    assert login_page_obj.success_msg_is_displayed(), "Succes message is not displayed after login"
    assert login_page_obj.get_success_msg_text() == "Your account has been successfully registered.", "Succes message is wrong" # не получается

    helper.logger.info("test_3 log in system")
    login_page_obj.log_in(username, password)


