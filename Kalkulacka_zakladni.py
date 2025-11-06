a=int(input("Zadej hodnotu A: "))
c=str(input("Zadej matematickou operaci(+, -, *, /, **, //): "))
b=int(input("Zadej hodnotu B: "))
if c=="+":                          #sčítání
    print("Výsledek: ", a+b)
elif c=="-":                        #odčítání
    print("Výsledek: ", a-b)
elif c=="/":                        #dělení
    if b != 0:
        print("Výsledek: ", a/b)    #kontrola dělení nulou
    else:
        print("Nelze dělit nulou!")
elif c=="*":                        #násobení
    print("Výsledek: ", a*b)
elif c=="**":                       #mocnina
    print("Výsledek:", a**b)
elif c=="//":                       #odmocnina
    print("Výsledek:", a**(1.0/b))
else:
    print("Výsledek nejde vypočítat")
    