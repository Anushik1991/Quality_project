from selenium.webdriver.common.by import By
from lib.helper import Helper


class Security(Helper):
    access_fail_message = ((By.XPATH, "//div[contains(@class, 'alert-danger')]"), "danger_alert_message")
    access_title = ((By.XPATH, "//small[text()='Enter to Qwallity app']"), "access_title_table")
    fld_email_sec = ((By.XPATH, "//input[@id='email']"), "input_email_field")
    fld_password_sec = ((By.XPATH, "//input[@id='code']"), "input_password_field")
    btn_send = ((By.XPATH, "//button[@id='Send']"), "sen_button")

    def access_to_system(self, email_access, password_access):
        try:
            self.logger.info("Filling email_access")
            self.input_text(5, self.fld_email_sec, email_access)

            self.logger.info("Filling code")
            self.input_text(5, self.fld_password_sec, password_access)
            
            self.logger.info("Clicking send button")
            self.click_element(5, self.btn_send)
        except Exception as e:
            self.logger.error(f"Error during login attempt: {e}")
            self.take_screenshot_with_timestamp("error_entering_in_system")
    
    def get_fail_msg_text(self):
        try:
            text = self.find_element(self.access_fail_message, 10).text
            self.logger.info(f"Fail message text: {text}")
            return text
        except Exception as e:
            self.logger.error(f"Success messga is not displayed: {e}")
            self.take_screenshot_with_timestamp("message_error")
            return False

    def title_is_displayed(self):
        try:
            return self.element_is_displayed(15, self.access_title)
        except Exception as e:
            self.logger.error(f"The title is not displayed: {e}")
            self.take_screenshot_with_timestamp("error_title")
            return False

    def get_table_title(self):
        try:
            title = self.find_element(self.access_title, 10).text
            self.logger.info(f"Fail message text: {title}")
            return title
        except Exception as e:
            self.logger.error(f"Success messga is not displayed: {e}")
            self.take_screenshot_with_timestamp("title_error")
            return False
