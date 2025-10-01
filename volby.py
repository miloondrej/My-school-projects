vek = int(input("Napiš svůj věk:"))
if vek >=40:                #porovnání věku 40+let
    print("Může volit")
    print("Může do parlamentu")
    print("Může do senátu")
    print("Může být prezident")
elif vek >=18 and vek >=21: #porovnání věku v rozsahu let
    print("Může volit")
    print("Může do parlamentu")
elif vek >=18:              #porovnání věku vůči minimální hodnotě
    print("Může volit")
    