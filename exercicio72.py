# @cikey 3749a643a52f3d6250bf1405b3469420
# @sid 20251174010010
# @aid V7.2


#begin_inputs
letras = ['t', 's', 'r', 'd', 'j', 'a', 'e']
palavra = 'tarde'
#end_inputs

def advinhou_palavra(letras, palavra):
    for letra in palavra:
        if letra not in letras:
            return False
    return True
print(advinhou_palavra(letras, palavra))