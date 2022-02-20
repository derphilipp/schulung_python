# Unbenutzter import; Zudem: Wildcard import.
# pylint: Wildcard import os
from os import *

# Zugriff auf Variable, bevor sie definiert ist
# flake8: 'x' may be undefined, or defined from star imports: os flake8(F405)
print(x)

x = 123

# Passwörter im Programmcode. SCHLECHTE IDEE
SECRET_PASSWORD = 'eimer'

# Unsinnige Schreibweise
def RuN():
    "Runs the program"
    print("Hello World")

# Böser Vergleich von None!
if x == None:
    print("Oh no!")

# Hier kommt ein unnötiges 'else'
def print_username(username=None):
    "Return a username"
    if username is None:
        return "No username given"
    else:
        return "Nice username"
