# @cikey 3749a643a52f3d6250bf1405b3469420
# @sid 20251174010010
# @aid V2.4


#begin_inputs
valor_compra = 100
#end_inputs

avista = valor_compra * 0.91
prestacao_5x = valor_compra / 5
prestacao_10x = (valor_compra * 1.17) / 10

print(round(avista, 2))
print(round(prestacao_5x, 2))
print(round(prestacao_10x, 2))

