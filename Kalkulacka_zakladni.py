a=int(input("Zadej hodnotu A: "))
c=str(input("Zadej matematickou operaci(+, -, *, /): "))
b=int(input("Zadej hodnotu B: "))
if c=="+":
    print("Výsledek: ", a+b)
elif c=="-":
    print("Výsledek: ", a-b)
elif c=="/":
    if b != 0:
        print("Výsledek: ", a/b)
    else:
        print("Nelze dělit nulou!")
elif c=="*":
    print("Výsledek: ", a*b)
else:
    print("Výsledek nejde vypočítat")