print("Tere! Olen sinu uus sõber - Python!")
nimi=input("Palun sisestage oma nimi. ")
print(nimi+ ", oi kui ilus nimi!")
num=int(input(nimi+ "! Kas leian Sinu keha indeksi? 0-ei, 1-jah =>"))
if num==1:
   try:
     pikkus=float(input("Lisage oma pikkus."))
   except:
    print("Sisestusviga, proovige uuesti.")
    exit()
   try:
     mass=float(input("Lisage oma mass."))
   except:
    print("Sisestusviga, proovige uuesti.") 
    exit()
   indeks=round(mass / (0.01*pikkus)**2,1)
   print(nimi+ "! Sinu keha indeks on:" +str(indeks))
   if indeks<16:
     print("Tervisele ohtlik alakaal")
   elif  16<=indeks<19: 
     print("Alakaal")
   elif  19<=indeks<25:  
     print("Normaalkaal")
   elif  25<=indeks<30:
     print("Ülekaal")
   elif  30<=indeks<35:
     print("Rasvumine")
   elif  35<=indeks<40: 
     print("Tugev rasvumine")
   elif  indeks>=40: 
     print("Tervisele ohtlik rasvumine  ")
else:
  print("Kahju! See on väga kasulik info!""\n")
print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")
     
     
    
   
    

