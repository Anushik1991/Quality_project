from selenium.webdriver.common.by import By
from lib.helper import Helper


class Home_Logged(Helper):
    welcome_msg = ((By.XPATH, "//div[@id='welcome_text']"), "login_message")

    def greating_logged_text_is_displayed(self):
        try:
            return self.element_is_displayed(15, self.welcome_msg)
        except Exception as e:
            self.logger.error(f"Welcome message is not displayed: {e}")
            self.take_screenshot_with_timestamp("message_error")
            return False
    
    def get_greating_logged_text(self):
        try:
            message = self.find_element(self.welcome_msg, 15).text
            self.logger.info(f"Welcome message text: {message}")
            return message 
        except Exception as e:
            self.logger.error(f"Welcome message is not displayed: {e}")
            self.take_screenshot_with_timestamp("title_error")
            return False