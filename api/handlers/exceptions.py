class LoginError(Exception):
    pass

class ElementNotFoundError(LoginError):
    pass

class LoginFailedError(LoginError):
    pass
