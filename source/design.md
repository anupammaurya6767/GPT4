## DesignHandler

This class is responsible for interacting with the design feature of the website.

### Methods

#### \_\_init\_\_(self, driver)

- Parameters:
    - driver (selenium.webdriver): The WebDriver instance to use for interacting with the website.
    
- Description:
    - Initializes a new instance of the DesignHandler class.

#### design(self, query, max_t)

- Parameters:
    - query (str): The query to ask.
    - max_t (int): The maximum time to wait for the response.
    
- Returns:
    - response (list): A list of image URLs.
    
- Description:
    - Sends a query to the website and retrieves a list of image URLs as a response.