# @cikey 3749a643a52f3d6250bf1405b3469420
# @sid 20251174010010
# @aid V6.4


#begin_inputs

#end_inputs
valor_dado = int(input('valor sorteado no dado: '))

if valor_dado == 7 or valor_dado == 11:
    print('Voce ganhou!')
elif valor_dado == 2 or valor_dado == 3 or valor_dado == 12:
    print('Voce perdeu!')
else:
    ponto = valor_dado
    valor_dado = int(input('valor sorteado no dado: '))
    while True:
        if valor_dado == ponto:
            print('Voce ganhou!')
            break
        elif valor_dado == 7:
            print('Voce perdeu!')
            break
        else:
            valor_dado = int(input('valor sorteado no dado: '))