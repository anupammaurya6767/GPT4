import time

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from api.handlers.exceptions import ElementNotFoundError, LoginFailedError
from selenium.webdriver.common.keys import Keys

class LoginHandler:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login(self, username, password,url):
        try:
            url = "https://copilot.microsoft.com/fd/auth/signin?action=interactive&provider=windows_live_id&return_url=https%3a%2f%2fcopilot.microsoft.com%2f%3fwlexpsignin%3d1%26wlexpsignin%3d1&src=EXPLICIT&sig=18ECF626889A6BE31CD9E21289226A28"
            self.driver.get(url)
            # Click sign in button
           
            
            # sign_in_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/header/div/a/div[1]/span/input")))    
            # sign_in_button.click()
            

            # # Click on the sign-in with Microsoft button
            # microsoft_sign_in_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/header/div/span/ul/li[1]/a")))
            # microsoft_sign_in_button.click()

            # Enter email
            email_input = self.wait.until(EC.presence_of_element_located((By.ID, "i0116")))
            email_input.send_keys(username)

            # Click Next
            next_button = self.wait.until(EC.presence_of_element_located((By.ID, "idSIButton9")))
            if not next_button:
                next_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/form/div[4]/div/div/div/div/button")))

            next_button.click()

            # Enter password
            password_input = self.wait.until(EC.presence_of_element_located((By.ID,"inner")))
            if not password_input:
                password_input = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/form/div[3]/div/div/input")))
            if not password_input:
                password_input = self.wait.until(EC.presence_of_element_located((By.NAME,"passwd")))
            self.driver.switch_to.active_element.send_keys(password)
            
            
           # Click sign in
            sign_in_button = self.wait.until(EC.presence_of_element_located((By.ID, "idSIButton9")))
            if not sign_in_button:
                sign_in_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[5]/div/div/div/div/input")))
            if not sign_in_button:
                 sign_in_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ext-button-item ___frx9oy0")))
            if not sign_in_button:
                 sign_in_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-report-event='Signin_Submit']")))
            sign_in_button.click()
            # self.driver.switch_to.active_element.send_keys(Keys.ENTER)

            # Click stay signed in
            time.sleep(2)
            stay_sign_in = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='post-redirect-form']")))
            self.driver.switch_to.active_element.send_keys(Keys.ENTER)

            # Wait for home button
            # time.sleep(5)
            # home_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "id_avatar")))
            # time.sleep(5)
            # assert home_button.is_displayed(), "Home button not displayed, login failed"
            return self.driver
        
        except TimeoutException as e:
            raise ElementNotFoundError(f"Element not found: {e}")
        
        except NoSuchElementException as e:
            raise ElementNotFoundError(f"Element not found: {e}")
        
        except AssertionError as e:
            raise LoginFailedError(f"Login failed: {e}")
