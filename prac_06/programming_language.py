"""
Programming Language
Current time: 13:55
Estimate: 30 minutes
Actual:   37 minutes
"""


class ProgrammingLanguage:
    """Display a programming language object."""

    def __init__(self, name='', typing='', reflection=False, year=None):
        """Initialize a ProgrammingLanguage object."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a representation of the programming language in strings."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Check the programming language is dynamically typed."""
        return self.typing == 'Dynamic'