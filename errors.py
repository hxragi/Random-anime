from typing import Optional


class ParseError(Exception):
    def __init__(self, message: str, selector: Optional[str] = None):
        self.message = message
        self.selector = selector
        super().__init__(self.message)


class NameParseError(ParseError):
    def __init__(
        self, message: str = "Failed to parse anime name", selector: Optional[str] = None
    ):
        super().__init__(message, selector)


class EpisodesParseError(ParseError):
    def __init__(
        self, message: str = "Failed to parse anime episodes", selector: Optional[str] = None
    ):
        super().__init__(message, selector)


class GenresParseError(ParseError):
    def __init__(
        self, message: str = "Failed to parse anime genres", selector: Optional[str] = None
    ):
        super().__init__(message, selector)
