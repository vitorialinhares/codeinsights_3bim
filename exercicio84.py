# @cikey 3749a643a52f3d6250bf1405b3469420
# @sid 20251174010010
# @aid V8.4

Dados = {}
with open("bloco84.txt","w",encoding="utf-8") as dados:
   for n in range(5):
     Nome = input("Escreva seu Nome:")
     Cpf =  input("Escreva seu CPF:")
     Dados[Nome] = Cpf
     dados.write(f"{Nome};{Cpf}\n")
print("_______________________")
with open("bloco84.txt","r",encoding="utf-8") as leia:
    ler = leia.read()
    print(ler.strip())