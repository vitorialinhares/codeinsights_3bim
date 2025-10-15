# @cikey 3749a643a52f3d6250bf1405b3469420
# @sid 20251174010010
# @aid V6.6
import random

def megasena():
    nummegasena = random.randint(1, 1000)
    trys = 0
    while True:
        palpite = int(input("Digite um numero entre 1 e 1000: "))
        trys += 1
        if trys >= 6:
            print("acabou suas tentativas")
            break

        if palpite < nummegasena:
            print("O numero secreto e MAIOR.")
        elif palpite > nummegasena:
            print("O numero secreto e ENOR.")
        else:
            print(f"Parabens! Você acertou! O numero secreto era {nummegasena}.")
            break
       
megasena()