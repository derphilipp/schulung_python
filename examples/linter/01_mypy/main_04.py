"Example for using mypy"


from typing import Optional

def greeting(name: Optional[str] = None) -> str:
    "Greets a person"
    # Optional[str] ist das gleiche wie Union[str, None]
    if name is None:
        name = 'stranger'
    return 'Hello, ' + name


print(greeting())
print(greeting("Paul"))
