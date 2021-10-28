#Helyezes;Nev;Orszag;Nyeremeny
from collections import Counter
with open("snooker.txt") as f:
    elso_sor = f.readline()
    lista = [sor.strip().split(";") for sor in f]
    
#3.feladat
    
print(f"3.feladat: A világranglistán {len(lista)} versenyző szerepel")

#4.feladat
print(f"4.feladat: A versenyzők átlagosan {sum([int(sor[3]) for sor in lista]) / len(lista):.2f} fontot kerestek")

#5.feladat
lg_kn = [sor for sor in [sor for sor in lista if sor[2] == "Kína"] if int(sor[3]) == max([int(sor[3]) for sor in [sor for sor in lista if sor[2] == "Kína"]])]
print(f"5.feladat: A legjobban kereső kínai versenyző: \n    Helyezés: {lg_kn[0][0]} \n    Név: {lg_kn[0][1]} \n    Ország: {lg_kn[0][2]} \n    Nyeremény: {int(lg_kn[0][3]) *380} Ft")

#6.feladat
van_norveg = [True for sor in lista if sor[2 ] == "Norvégia"]
print(f"6.feladat: A versenyzők között {'van' if van_norveg else 'nincs'} norvég versenyző")

#7.feladat

print("7.feladat: Statisztika  \n{}".format('\n'.join([f'{orszag} - {db} fő' for orszag, db in [Counter(sor[2] for sor in lista)][0].items() if db > 4])))







     
    
    