from selenium import webdriver
from api.modules.login import LoginHandler
from api.handlers.utils import load_config
from api.handlers.exceptions import LoginFailedError
from api.modules.chat import ChatHandler

class GPT4:
    def __init__(self, config_file):

        options = webdriver.ChromeOptions()
        options.add_argument('--headless= new')
        self.driver = webdriver.Chrome(options = options)
        self.login_handler = LoginHandler(self.driver)
        self.config = load_config(config_file)
        self.url = "https://copilot.microsoft.com"

    def login(self):
        try:
            username = self.config['CREDENTIALS']['username']
            password = self.config['CREDENTIALS']['password']
            print("login...")
            self.chat_handler = self.login_handler.login(username, password,self.url) 
            print("Login successful")
        except LoginFailedError as e:
            print(f"Login failed: {e}")


    def ask_question(self, question,max_t=50):
        
        self.chat_handler.ask_question(question,max_t)

    def get_response(self):
        return self.chat_handler.get_response()

    def close(self):
        self.driver.quit()
