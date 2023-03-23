from one import one
from Module1 import GLOBAL_VAR
import Module1

def two():
    print('two')
    print(GLOBAL_VAR)
    print(Module1.GLOBAL_VAR)

one()
two()
print()
GLOBAL_VAR = 123
one()
two()
print()
Module1.GLOBAL_VAR = 123
one()
two()