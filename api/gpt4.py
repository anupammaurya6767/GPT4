from selenium import webdriver
from api.modules.login import LoginHandler
from api.handlers.utils import load_config
from api.handlers.exceptions import LoginFailedError
from api.modules.chat import ChatHandler
from api.modules.design import DesignHandler
import logging
from api.handlers.animation import animated_print,animated_design
from colorama import Fore, Style
from api.handlers.banner import print_banner



class GPT4:
    def __init__(self, config_file):
        
        intro_text = """The GPT4 API project aims to provide an automated interface for interacting with the GPT-4 (Generative Pre-trained Transformer 4) model developed by OpenAI. GPT-4 is a state-of-the-art natural language processing model capable of generating human-like text based on input prompts.
        """
        print_banner()

        print(intro_text)
        logging.basicConfig(level=logging.WARNING)
        options = webdriver.ChromeOptions()
        options.add_argument('--log-level=3')
        options.add_argument('--headless= new')
        self.driver = webdriver.Chrome(options = options)
        self.login_handler = LoginHandler(self.driver)
        self.config = load_config(config_file)
        self.url = "https://copilot.microsoft.com"

    def login(self):
        try:
            username = self.config['CREDENTIALS']['username']
            password = self.config['CREDENTIALS']['password']
            animated_print(Fore.YELLOW + "login...", end='', flush=True)
            animated_print(Fore.YELLOW + "...")
            print(Style.RESET_ALL, end='', flush=True)
            self.driver = self.login_handler.login(username, password,self.url) 
            animated_print(Fore.GREEN + "Login successful",0.1)

        except LoginFailedError as e:
            animated_print(Fore.RED + f"Login failed: {e}")


    def ask_question(self, question,max_t=50):
        animated_print(Fore.MAGENTA + "Generating a suitable response...",3, end='', flush=True)
        self.chat_handler = ChatHandler(self.driver)
        self.chat_handler.ask_question(question,max_t)

    def get_response(self):
        return self.chat_handler.get_response()
    
    def design(self,query,max_t=50):
        animated_design(Fore.BLUE + "Bringing Your Ideas To Life...",5)
        self.design_handler = DesignHandler(self.driver)
        return self.design_handler.design(query,max_t)

    def close(self):
        self.driver.quit()
