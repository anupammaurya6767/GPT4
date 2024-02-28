# LoginHandler

## Class Overview

The `LoginHandler` class is responsible for handling the login functionality for a website using Selenium. It provides methods to perform the login process.

## Class Methods

### `__init__(self, driver)`

Initializes a new instance of the `LoginHandler` class.

- `driver`: The Selenium webdriver instance.

### `login(self, username, password, url)`

Performs the login process.

- `username`: The username or email address for the login.
- `password`: The password for the login.
- `url`: The URL of the login page.

#### Steps:
1. Navigates to the specified URL.
2. Clicks the "Sign in" button.
3. Clicks the "Sign in with Microsoft" button.
4. Enters the email/username.
5. Clicks the "Next" button.
6. Enters the password.
7. Clicks the "Sign in" button.
8. Clicks the "Stay signed in" button.
9. Waits for the home button to be displayed, indicating a successful login.
10. Returns the webdriver instance.

## Exceptions

### `ElementNotFoundError`

Raised when an element is not found during the login process.

### `LoginFailedError`

Raised when the login fails.