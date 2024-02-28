from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from api.handlers.exceptions import ElementNotFoundError, LoginFailedError
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import re


class ChatHandler:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.response = ""
        self.max_t = 50

    def ask_question(self, question, max_t):
        try:

            total_area = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cib-serp-main"))).shadow_root

            self.driver.maximize_window()
            self.max_t = max_t

            a1_ = total_area.find_element(By.ID, "cib-action-bar-main").shadow_root
            a2 = total_area.find_element(By.CSS_SELECTOR,"cib-side-panel").shadow_root

            a4 = a1_.find_element(By.CSS_SELECTOR,"cib-text-input").shadow_root

            textarea = a4.find_element(By.CLASS_NAME,"text-area")
            textarea.click()

            # Check if the clicked element is accepting text input
            clicked_element = self.driver.switch_to.active_element
            if clicked_element.is_enabled() and clicked_element.is_displayed():
                # Type the question in the element
                clicked_element.send_keys(question)
                clicked_element.send_keys(Keys.ENTER)
            else:
                raise ElementNotFoundError("The clicked element is not accepting text input.")
        except Exception as e:
            raise ElementNotFoundError(f"Error occurred while asking question: {e}")
        
        pass

    def get_response(self):
        try:
            response_area = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cib-serp-main"))).shadow_root
            a1 = response_area.find_element(By.ID, "cib-conversation-main").shadow_root
            a2 = a1.find_element(By.ID, "cib-chat-main")
            a3 = a2.find_elements(By.TAG_NAME, "cib-chat-turn")[-1].shadow_root
            time.sleep(self.max_t)
            a4 = a3.find_element(By.CLASS_NAME, "response-message-group").shadow_root
            a7 = a4.find_element(By.CLASS_NAME, "header")
            a5 = a4.find_element(By.CSS_SELECTOR, "cib-message").shadow_root
            a6 = a5.find_element(By.CSS_SELECTOR, "cib-shared").find_elements(By.CLASS_NAME, "ac-textBlock")

            for txt in a6:
                self.response += re.sub(r'(?i)copilot', 'gpt4', txt.text)

            if not self.response:
                print("enter your query")
                return {"response": "Please Enter your query"}
            else:
                return {"response": self.response}
        
        except NoSuchElementException as e:
            raise ElementNotFoundError(f"Element not found: {e}")
