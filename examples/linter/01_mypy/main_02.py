"Example for using mypy"


def greeting(name):
    "Greets a person"
    return "Hello " + name


def greet_all(names: list[str]) -> None:
    "Greets all persons"
    for name in names:
        print(greeting(name))


greet_all(["Peter", "Paul", "Mary"])
greet_all([1, 2, 3])
