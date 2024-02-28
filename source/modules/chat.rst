ChatHandler documentation
=========================

This class represents a chat handler for a chatbot. It is responsible for interacting with the chat interface and retrieving responses.

Constructor
-----------

_init_(self, driver)
~~~~~~~~

- *driver* - an instance of the Selenium WebDriver

Properties
----------

- *driver*: The Selenium WebDriver instance used by the ChatHandler.
- *wait*: An instance of WebDriverWait used for waiting for elements to be present.
- *response*: A string that holds the response obtained from the chatbot.
- *max_t*: An integer that represents the maximum time to wait for a response from the chatbot.

Methods
-------

ask_question(self, question, max_t)
~~~~~~~~~~~~

This method is used to ask a question to the chatbot.

- *question* - a string representing the question to ask the chatbot.
- *max_t* - an integer representing the maximum time to wait for a response.

get_response(self)
~~~~~~

This method is used to retrieve the response from the chatbot.

Returns a dictionary with the response, or raises an exception if the response cannot be retrieved.

DesignHandler
=============

This class is responsible for interacting with the design feature of the website.

Methods
-------

\\init\\(self, driver)
~~~~~~~~~

- Parameters:
    - *driver* (selenium.webdriver): The WebDriver instance to use for interacting with the website.
    
- Description:
    - Initializes a new instance of the DesignHandler class.

design(self, query, max_t)
~~~~~~~~~~

- Parameters:
    - *query* (str): The query to ask.
    - *max_t* (int): The maximum time to wait for the response.
    
- Returns:
    - *response* (list): A list of image URLs.
    
- Description:
    - Sends a query to the website and retrieves a list of image URLs as a response.