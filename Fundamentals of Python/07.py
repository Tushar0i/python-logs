# Built-in Functions
from enum import Enum


num = -10.2397
print(abs(num)) # 10.23
print(round(num)) # -10
print(round(num,2)) # -10.24


class State(Enum):
    INACTIVE = 0
    ACTIVE = 1
# this the only way to create constants in pythons

print(State.ACTIVE.value)
print(State['ACTIVE'].value)
print(State(0))

print(list(State))
print(len(State))