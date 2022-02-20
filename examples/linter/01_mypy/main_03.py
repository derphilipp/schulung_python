"Example for using mypy"


from typing import Union


def normalize_id(user_id: Union[int, str]) -> str:
    "Normalize user id"
    # Erlaube int oder auch str
    if isinstance(user_id, int):
        return "user-{}".format(100000 + user_id)
    else:
        return user_id


print(normalize_id(123))
print(normalize_id("4711"))
