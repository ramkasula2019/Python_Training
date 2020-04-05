# importing fibo function from fibonacci.py

#importing fibo function from module itself
from fibonacci import fibo
print(fibo(8))
print(fibo(20))

#importing whole module
import fibonacci
print(fibonacci.fibo(20000))

# import all names defined in module
from fibonacci import *
print(fibo(5))

from fibonacci import fibo as fibo_alias
print(fibo_alias(20))
