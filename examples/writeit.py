from dataclasses import dataclass
import json

from types import SimpleNamespace


@dataclass
class Laptop:
    name: str
    unit_price: float
    quantity_on_hand: int = 0


l = Laptop("MacBook Pro", 999.99, 3)
x = json.dumps(l.__dict__)
print(x)

l1 = Laptop("MacBook Air", 1813.99, 2)
l2 = Laptop("MacBook Pro", 999.99, 3)


lst = [l1, l2]
x = json.dumps(lst, default=lambda o: o.__dict__, indent=4, sort_keys=True)
print(x)


my_element = json.dumps(l1, default=lambda o: o.__dict__, indent=4, sort_keys=True)
print(my_element)
j = json.loads(my_element)
lx = Laptop(**j)
print(lx)
