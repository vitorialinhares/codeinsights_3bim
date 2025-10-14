# @cikey 3749a643a52f3d6250bf1405b3469420
# @sid 20251174010010
# @aid V6.2


#begin_inputs
n = int(input(""))
#end_inputs

def trianguloretangulo(n):
    for i in range(1, n + 1):
        for r in range(1, i + 1):
            print(r, end=' ')
        print()
trianguloretangulo(n)

