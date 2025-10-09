# @cikey 3749a643a52f3d6250bf1405b3469420
# @sid 20251174010010
# @aid V6.3


#begin_inputs
n = int(input(":"))
#end_inputs
def reverso (n):
    return int(str(n) [ : : -1])

print(reverso(n))
