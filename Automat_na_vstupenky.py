vek=int(input("Zadej svůj věk:"))          #zjištění věku uživatele
if vek<=6:                                 #podmínka pro zjištění věkové kategorie
    print("Vstupné je zdarma")             #pokud je uživatel starší než 6 let
elif vek>=7 and vek<=17:                   #podmínka pro zjištění věkové kategorie
    print("Vstupné je 80 Kč")              #pokud je uživatel mladší než 15 let
elif vek>=18 and vek<=64:                  #pokud je uživatel starší nebo roven 15 let a zároveň mladší než 65 let
    print("Vstupné je 150 Kč")             #pokud je uživatel ve věku 15-64 let
else:                                      #pokud je uživatel starší nebo roven 65 let
    print("Vstupné je 100 Kč")             #pokud je uživatel ve věku 65 a více let
