from math import * #käsu vale sõnade jada
print("Ruudu karakteristikud")
a=float(input('Sisesta ruudu külje pikkus => ')) #float puudub
S=a**2
print("Ruudu pindala", S)
P=4*a
print("Ruudu ümbermõõt", P) #viga sulgudes
di=a*sqrt(2) #viga, math  
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud") #seal oli lisasulg
b=float(input("Sisesta ristküliku 1. külje pikkus => ")) #float puudub
c=float(input("Sisesta ristküliku 2. külje pikkus => ")) #float puudub
S=b*c
print("Ristküliku pindala", S) #viga sulgudes
P=2*(b+c) #korrutamismärk puudub
print("Ristküliku ümbermõõt", P)
di=sqrt(b**2+c**2) #viga, math ja atendamine puudub
print("Ristküliku diagonaal", round(di,2)) #sulgud ei olnud suletud
print()
print("Ringi karakteristikud")
r=float(input('Sisesta ringi raadiusi pikkus => ')) #viga sulgudes ja seal oli lisasulg ja float puudub
d=2*r #korrutamismärk puudub
print("Ringi läbimõõt", d) #kolma puudu
S=pi*r**2 #sulgusid pole vaja, atendamine puudub
print("Ringi pindala", round(S,2))
C=2*pi*r #korrutamismärk puudub ja sulgusid pole vaja
print("Ringjoone pikkus", round(C,2)) #sulg oli puudu
