from selenium.webdriver.common.by import By
from lib.helper import Helper


class Login(Helper):
    reg_success_message = ((By.XPATH, "//div[contains(@class, 'alert-success')]"), "success_alert_message")
    login_title = ((By.XPATH, "//h1/div[@id = 'login']"), "login_title_text")
    
    fld_username_log = ((By.XPATH, "//form[@id='loginForm']/input[@id = 'username']"), "input_username_field")
    fld_password_log = ((By.XPATH, "//form[@id='loginForm']/input[@id = 'password']"), "input_password_field")
    btn_log_in = ((By.XPATH, "//form[@id='loginForm']/button[@id = 'submit_login_page']"), "log-in_button")

    def log_in(self, email, password):
        try:
            self.logger.info("Filling email")
            self.input_text(5, self.fld_username_log, email)

            self.logger.info("Filling password")
            self.input_text(5, self.fld_password_log, password)
            
            self.logger.info("Clicking log_in button")
            self.click_element(5, self.btn_log_in)
        except Exception as e:
            self.logger.error(f"Error during login attempt: {e}")
            self.take_screenshot_with_timestamp("error_log_in")
    
    def success_msg_is_displayed(self):
        try:
            return self.element_is_displayed(15, self.reg_success_message)
        except Exception as e:
            self.logger.error(f"Success messga is not displayed: {e}")
            self.take_screenshot_with_timestamp("message_error")
            return False
        
    def get_success_msg_text(self):
        try:
            text = self.find_element(self.reg_success_message, 10).get_attribute("innerText").strip()
            self.logger.info(f"Success message text: {text}")
            return text
        except Exception as e:
            self.logger.error(f"Success message is not displayed: {e}")
            self.take_screenshot_with_timestamp("message_error")
            return False
    
    def login_title_is_displayed(self):
        try:
            return self.element_is_displayed(15, self.login_title)
        except Exception as e:
            self.logger.error(f"Success messga is not displayed: {e}")
            self.take_screenshot_with_timestamp("message_error")
            return False
    
    def get_login_title_text(self):
        try:
            title = self.find_element(self.login_title, 15).text
            self.logger.info(f"Login title text: {title}")
            return title
        except Exception as e:
            self.logger.error(f"Login title is not displayed: {e}")
            self.take_screenshot_with_timestamp("title_error")
            return False