# Modules

import math
print(math.sqrt(16))

from math import pi, floor
print(pi)
import random as rnd #alias
print(rnd.randint(1,10))

# Custom Modules
from helpers import greet
print(greet("Vir"))


"""
Virtual environments (one isolated set of packages per project)

python -m venv venv                # create
venv\Scripts\activate              # Windows
source venv/bin/activate           # Mac/Linux

pip install requests               # install a package
pip list                           # see what's installed
pip freeze > requirements.txt      # save dependencies
pip install -r requirements.txt    # recreate them elsewhere
deactivate                         # leave the venv
"""

import requests
r = requests.get("https://api.github.com")
print(r.status_code)
print(r.json())

import mathutils as m
print(m.is_prime(17))
print(m.factorial(5))

import requests
try: 
    r = requests.get("https://api.github.com/users/octocat")
    data = r.json()
    print(data.get('name'))
    print(data.get('public_repos'))
except requests.exceptions.RequestException as e:
    print(e)

