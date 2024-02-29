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
from bs4 import BeautifulSoup


class DesignHandler:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.response = []
        self.max_t = 50

    def design(self, query, max_t):
        try:
            self.response = []
            time.sleep(10)
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
                clicked_element.send_keys('create an image '+query)
                clicked_element.send_keys(Keys.ENTER)
                response_area = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cib-serp-main"))).shadow_root
                a1 = response_area.find_element(By.ID, "cib-conversation-main").shadow_root
                a2 = a1.find_element(By.ID, "cib-chat-main")
                a3 = a2.find_elements(By.TAG_NAME, "cib-chat-turn")[-1].shadow_root
                time.sleep(max_t)
                a4 = a3.find_element(By.CLASS_NAME, "response-message-group").shadow_root
                a5 = a4.find_element(By.CSS_SELECTOR,"[content='IMAGE']").shadow_root
                iframe = a5.find_element(By.CLASS_NAME,"frame")
                time.sleep(max_t)
                self.driver.switch_to.frame(iframe)
                html = self.driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                div_elements = soup.find_all('a', {'class': 'iusc'})
                for div_element in div_elements:
                    href = div_element.get('href')
                    if href:
                        modified_href = 'https://copilot.microsoft.com' + href
                        self.response.append(modified_href)
                
                self.driver.switch_to.default_content()
                return self.response
            
            else:
                raise ElementNotFoundError("The clicked element is not accepting text input.")
        except Exception as e:
            raise ElementNotFoundError(f"Error occurred while asking question: {e}")
        
