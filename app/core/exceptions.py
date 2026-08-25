

class ServerErrorException(Exception):
    """Exception raised for server errors."""
    def __init__(self , message : str ):
        self.message = message
        super().__init__(self.message)