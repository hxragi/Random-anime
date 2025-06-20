class ParseError(Exception):
    def __init__(self, message: str, selector: str = None):
        self.message = message
        self.selector = selector
        super().__init__(self.message)


class NameParseError(ParseError):
    def __init__(
        self, message: str = "Failed to parse anime name", selector: str = None
    ):
        super().__init__(message, selector)


class EpisodesParseError(ParseError):
    def __init__(
        self, message: str = "Failed to parse anime episodes", selector: str = None
    ):
        super().__init__(message, selector)


class GenresParseError(ParseError):
    def __init__(
        self, message: str = "Failed to parse anime genres", selector: str = None
    ):
        super().__init__(message, selector)
