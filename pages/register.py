from selenium.webdriver.common.by import By
from lib.helper import Helper


class Register(Helper):
    fld_name = ((By.XPATH, "//div[@class='form-group']/input[@id='name']"), "input_name")
    fld_email = ((By.XPATH, "//div[@class='form-group']/input[@id='email']"), "input_email")
    fld_username = ((By.XPATH, "//div[@class='form-group']/input[@id='username']"), "input_username")
    fld_password = ((By.XPATH, "//div[@class='form-group']/input[@id='password']"), "input_password")
    fld_confirm = ((By.XPATH, "//div[@class='form-group']/input[@id='confirm']"), "input_confirm")
    btn_submit = ((By.XPATH, "//input[@class='btn btn-primary']"), "button_submit")
    register_title = ((By.XPATH, "//small[text()='Register']"), "register_title_table")

    def register_in_system(self, name, email, username, password, confirm_password):
        try:
            self.logger.info("Filling name")
            self.input_text(5, self.fld_name, name)
            
            self.logger.info("Filling email")
            self.input_text(5, self.fld_email, email)

            self.logger.info("Filling username")
            self.input_text(5, self.fld_username, username)

            self.logger.info("Filling username")
            self.input_text(5, self.fld_password, password)

            self.logger.info("Filling username")
            self.input_text(5, self.fld_confirm, confirm_password)
            
            self.logger.info("Clicking submit button")
            self.click_element(5, self.btn_submit)
        except Exception as e:
            self.logger.error(f"Error during registration attempt: {e}")
            self.take_screenshot_with_timestamp("error_register")
    
    def register_title_is_displayed(self):
        try:
            return self.element_is_displayed(15, self.register_title)
        except Exception as e:
            self.logger.error(f"Register title is not displayed: {e}")
            self.take_screenshot_with_timestamp("register_error")
            return False
    
    def get_register_title_text(self):
        try:
            title = self.find_element(self.register_title, 15).text
            self.logger.info(f"Register title text: {title}")
            return title
        except Exception as e:
            self.logger.error(f"Register title is not displayed: {e}")
            self.take_screenshot_with_timestamp("title_error")
            return False