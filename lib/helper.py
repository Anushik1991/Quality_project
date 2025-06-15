from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from datetime import datetime


class Helper:

# Когда ты используешь фикстуру из conftest.py в параметрах, 
# pytest автоматически вызывает её и передаёт результат — готовый объект.

    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    def go_to_page(self, url, new_window=False):
        if new_window:
            self.driver.execute_script(f"window.open('{url}');")
        else:
            self.driver.get(url)
            self.driver.maximize_window()

    def take_screenshot_with_timestamp(self, name="screenshot"):
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{name}_{timestamp}.png"
            folder = "screenshots"

            folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "screenshots")

            os.makedirs(folder, exist_ok=True)  
            path = os.path.join(folder, filename)
            self.driver.save_screenshot(path)
            self.logger.info(f"Screenshot saved: {path}")
        except Exception as e:
            self.logger.error(f"Could not save screenshot: {e}")
    
    def find_element(self, loc, timeout):
        try:
            elem = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(loc[0]))
            return elem
        except Exception as e:
            self.logger.error(f"{loc[1]} is not found {e}")
            return None
    
    def find_element_presence(self, loc, timeout):
        try:
            elem = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(loc[0]))
            return elem
        except Exception as e:
            self.logger.error(f"{loc[1]} is not found {e}")
            return None
    
    def find_elements(self, loc, timeout):
        try:
            elements = WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(loc[0]))
            return elements
        except Exception as e:
            self.logger.error(f"{loc[1]} are not found {e}")

    def click_element(self, timeout, loc):
        try:
            elem = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(loc[0]))
            elem.click()
        except Exception as e:
            self.logger.error(f"{loc[1]} is not found {e}")

    def element_is_displayed(self, timeout, loc):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(loc[0]))
            return element.is_displayed()
        except Exception as e:
            self.logger.error(f"Element {loc[1]} is not displayed: {e}")
            return False
    
    def get_page_title(self):
        try:
            title = self.driver.title
            self.logger.info(f"Page title is: {title}")
            return title
        except Exception as e:
            self.logger.error(f"Could not get page title: {e}")
            return None
        
    def input_text(self, timeout, loc, text):
        try:
            elem = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(loc[0]))
            elem.clear()
            elem.send_keys(text)
        except Exception as e:
            self.logger.error(f"{loc[1]} is not found {e}")

    def input_text_enter(self, timeout, loc, text):
        try:
            search_box = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(loc[0]))
            search_box.send_keys(text + Keys.ENTER)
            self.logger.info(f"Searched: {text}")
        except Exception as e:
            self.logger.error(f"Search input field: {e}")

    def is_redirected_to(self, expected_url_part, timeout=15):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: expected_url_part in driver.current_url
            )
            current_url = self.driver.current_url
            self.logger.info(f"Current URL after redirect: {current_url}")
            return True
        except Exception as e:
            current_url = self.driver.current_url
            self.logger.error(f"Expected URL part '{expected_url_part}' not found in '{current_url}': {e}")
            self.take_screenshot_with_timestamp("redirect_error")
            return False

    def close_browser(self):
        self.driver.quit()

"""
    def is_redirected_to(self, expected_url_part):
        try:
            current_url = self.driver.current_url
            self.logger.info(f"Current URL: {current_url}")
            return expected_url_part in current_url
        except Exception as e:
            self.logger.error(f"Failed to get current URL: {e}")
            return False
"""


