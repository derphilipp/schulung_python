"Example for using mypy"


def greeting(name: str) -> str:
    "Greets a person"
    return 'Hello ' + name


greeting("Peter")
greeting(123)
