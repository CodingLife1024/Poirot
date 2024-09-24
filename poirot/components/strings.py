class StringOperations:
    @staticmethod
    def is_string_empty(string: str) -> bool:
        return not string or string.isspace()

    @staticmethod
    def is_string_not_empty(string: str) -> bool:
        return not StringOperations.is_string_empty(string)

    @staticmethod
    def is_string_none(string: str) -> bool:
        return string is None