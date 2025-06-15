from selenium.webdriver.common.by import By
from lib.helper import Helper


class Home(Helper):
    greeting_msg = ((By.ID, "welcome_text"), "greeting_message_entering")
    btn_register = ((By.ID, "nav_register"), "register_button")
    # btn login

    def click_register(self):
        try:
            self.click_element(10, self.btn_register)
        except Exception:
            self.logger.error("Error during click on register button")
            self.take_screenshot_with_timestamp("error_click_register")

    def greeting_is_displayed(self):
        try:
            return self.element_is_displayed(15, self.greeting_msg)
        except Exception as e:
            self.logger.error(f"Error during login attempt: {e}")
            self.take_screenshot_with_timestamp("error_entering_in_system")
            return False