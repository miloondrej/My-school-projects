import time           # import knihovny time pro pauzu
x=0
while x<5:            # cyklus se opakuje, dokud je x menší než 5
    print(x)
    x +=1             # zvýšení hodnoty x o 1
    time.sleep(0.5)   # pauza 0,5 sekunda
while x>0:            # cyklus se opakuje, dokud je x větší než 0
    print(x)
    x -=1             # snížení hodnoty x o 1
    time.sleep(0.5)   # pauza 0,5 sekunda