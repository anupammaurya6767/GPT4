import unittest
import os
from api.gpt4 import GPT4

class TestGpt4(unittest.TestCase):
    def setUp(self):
        # Read username and password from environment variables
        username = os.environ.get('USERNAME')
        password = os.environ.get('PASSWORD')
        url = os.environ.get('URL')
        
        # Write username and password to a temporary config file
        temp_config_path = 'temp_config.ini'
        with open(temp_config_path, 'w') as config_file:
            config_file.write("[CREDENTIALS]\n")
            config_file.write(f"username = {username}\n")
            config_file.write(f"password = {password}\n")
            config_file.write("url = https://bit.ly/49A8Ufe\n")
            config_file.write("driver_path = None\n")

        # Initialize GPT4 with the temporary config file
        self.ap = GPT4(config_file=temp_config_path)

    # def test_login(self):
    #     self.ap.login()
    #     pass

    # def test_ask_question(self):
    #     question = 'Test question'
    #     self.ap.login()
    #     self.ap.ask_question(question,20)
    #     response = self.ap.get_response()
    #     pass
    
    def test_design(self):
        question = 'A cow'
        self.ap.login()
        self.ap.design(question)
        pass

    def tearDown(self):
        os.remove('temp_config.ini')
        self.ap.close()

if __name__ == '__main__':
    unittest.main()
