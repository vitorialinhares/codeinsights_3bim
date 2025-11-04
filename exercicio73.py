# @cikey 3749a643a52f3d6250bf1405b3469420
# @sid 20251174010010
# @aid V7.3

import random

def quinadavirada():
    numeros = random.sample(range(1, 41), 25)
    numeros.sort()
    return numeros
print(quinadavirada())