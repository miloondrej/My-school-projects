import math                                 #import knihoven math a cmath 
import cmath
a=int(input("zadej hodnotu A:"))            #deklarace proměnných
c=str(input("Zadej matematickou operaci(+, -, *, /, **, //, %, log):"))
b=int(input("Zadej hodnotu B:"))   
last_result = None                          #proměnná pro uložení posledního výsledku
if c=="+":                                  #sčítání
    last_result = a+b
    print("Výsledek: ", last_result)
elif c=="-":                                #odčítání
    last_result = a-b
    print("Výsledek: ", last_result)
elif c=="/":                                #dělení
    if b != 0:
        last_result = a/b                   #kontrola dělení nulou
        print("Výsledek: ", last_result)
    else:
        print("Nelze dělit nulou!")
elif c=="*":                                #násobení
    last_result = a*b
    print("Výsledek: ", last_result)
elif c=="**":                               #mocnina
    last_result = a**b
    print("Výsledek:", last_result)
elif c=="//":                               #odmocnina
    last_result = a**(1.0/b)
    print("Výsledek:", last_result)
elif c=="%":                                #modulo
    if b != 0:
        last_result = a%b
        print("Výsledek:", last_result)
    else:
        print("Nelze dělit nulou!")
elif c=="log":                              #logaritmus
    if a > 0 and b > 0 and b != 1:
        last_result = math.log(a, b)
        print("Výsledek:", last_result)
    else:
        print("Logaritmus není definován pro zadané hodnoty!")
else:
    print("Výsledek nejde vypočítat")
if last_result is not None:
    with open("kalkulacka_pokrocila_vysledek.txt", "w") as file:        # Pokročilá kalkulačka s podporou modulo a logaritmu, včetně kontroly dělení nulou a záporných hodnot pro logaritmus.
        file.write("Poslední výsledek: " + str(last_result) + "\n")     # Výsledek je uložen do souboru "kalkulacka_pokrocila_vysledek.txt". 
              

