import unittest
from api.gpt4 import GPT4

class TestGpt4(unittest.TestCase):
    def setUp(self):
        self.ap = GPT4(config_file='config.ini')

    def test_login(self):
        self.ap.login()
        pass

    def test_ask_question(self):
        question = 'Test question'
        self.ap.login()
        self.ap.ask_question(question,10)
        response = self.ap.get_response()
        pass

    def tearDown(self):
        self.ap.close()

if __name__ == '__main__':
    unittest.main()
