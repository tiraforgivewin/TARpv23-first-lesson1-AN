from random import *
#arv=randint(0,100) #juhulik täisrv vahemikust 0...100
#print(arv)
#if arv%2==0:
#    print(arv,"on paaris arv")
#else:
#    print(arv,"on paaritu arv")
#print()


#print("Tund on alnud")
#hilinemine=input("Kas opilane on hilenenud?") 
## "JAH"-a.upper(), "jah"-a.lower(), "Jah"-a.capitalize(), jAH
#if hilinemine.upper()=="JAH":
#    print("Õpilane ootab 30 min")
#print("Õpilane aastub klasssi")

#protsent=randint(0,100)#0-100 o-60 "2", 61-75 "3" 75-85 "4", 86-100 "5"
#print(protsent,"% on teisti tulemus")
#if protsent<0 or protsent>100:
#    tulemus="valed andmed"
#elif protsent<60:
#    tulemus="hinne 2"
#elif 60<=protsent<75:
#    tulemus="hinne 3"
#elif 75<=protsent<85:
#    tulemus="hinne 4"
#else:
#    tulemus="hinne 5"
#print(tulemus)



#1
nimi=input("Mis on sinu nimi?")
print("Tere", nimi)
if nimi.capitalize()=="Juku":
    print("Lahme kino")
    vanus=int(input("Kui vana sa oled?"))
    if vanus<0 or vanus>100:
        pilet=" viga andmetega"
    elif vanus<6:
        pilet="tasuta pilet"
    elif vanus<=14:
        pilet="lastepilet"
    elif vanus<=65:
        pilet="täispilet"
    elif vanus<=100:
        pilet="soduspilet"
    print(pilet)


else:
    print("Ma ootan Jukut")






