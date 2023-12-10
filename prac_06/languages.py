"""Intermediate Exercise - Programming language client program"""

from prac_06.programming_language import ProgrammingLanguage


def main():
    """Display programming languages that are dynamic"""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)
    print("The dynamically typed languages are: ")
    languages = [python, ruby, visual_basic]
    for language in languages:
        if language.is_dynamic():
            print(language.field)


main()
