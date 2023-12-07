class ProgrammingLanguage:
    """Represent information about programming language ."""
    def __init__(self, field, typing, reflection, year):
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.field}, {self.typing} Typing, Reflection = {self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if the typing is dynamic"""
        return self.typing == "Dynamic"
