# @cikey 3749a643a52f3d6250bf1405b3469420
# @sid 20251174010010
# @aid V8.3

with open("bloco82.txt","r",encoding="utf-8") as arquivo_original:
    conteudo = arquivo_original.read()
with open("bloco83.txt","w",encoding="utf-8") as copiar:
     copiar.write(conteudo)  
print("Arquivo copiado com sucesso")