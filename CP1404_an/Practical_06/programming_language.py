
class ProgrammingLanguage:
    def __init__(self, name= "", typing="/",reflection= "/",year = 0):
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.name = name

    def is_dynamic(self):
        if self.typing.title() == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    # Python, Dynamic Typing, Reflection=True, First appeared in 1991 string formatting

