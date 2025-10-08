# @cikey 3749a643a52f3d6250bf1405b3469420
# @sid 20251174010010
# @aid V5.1


#begin_inputs

#end_inputs
somatorio = 0
peso = int(input('Digite o peso:'))
somatorio += peso
while somatorio <= 500:
    peso = int(input('Digite o peso:'))
    somatorio += peso
print('Peso excedido')