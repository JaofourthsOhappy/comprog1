class Error(Exception):
   """Base class for other exceptions"""
   pass
class InvalidInput(Error):
   """Raised when the input is invalid"""
   pass
class AccountNotFound(Error):
    pass