class InvalidTreeException(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)

class PeakNotFoundException(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)