# @cikey 3749a643a52f3d6250bf1405b3469420
# @sid 20251174010010
# @aid V5.2


#begin_inputs
 

#end_inputs

minutos = 0
tartaruga = 1 * minutos + 500 
lebre = 10 * minutos

while tartaruga > lebre:
    tartaruga = round(tartaruga + 1)
    lebre = round(lebre + 10)
    minutos += 1
print("{}".format(minutos))