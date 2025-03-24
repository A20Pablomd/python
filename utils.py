# utils.py
class StringUtils:
    @staticmethod
    def reverse_string(string):
        """Reverse a given string"""
        return string[::-1]

    @staticmethod
    def capitalize_string(string):
        """Capitalize all letters in a string"""
        return string.upper()

    @staticmethod
    def lowercase_string(string):
        """Convert all letters in a string to lowercase"""
        return string.lower()
