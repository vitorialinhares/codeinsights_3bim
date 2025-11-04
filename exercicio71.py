# @cikey 3749a643a52f3d6250bf1405b3469420
# @sid 20251174010010
# @aid V7.1


#begin_inputs
letras = ['t', 'a', 'r', 'd', 'e']
#end_inputs

from string import ascii_lowercase

def letras_disponiveis(letras):
    return [l for l in ascii_lowercase if l not in letras]

print(letras_disponiveis(letras))



