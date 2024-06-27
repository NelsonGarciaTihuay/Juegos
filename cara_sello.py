import random
input("Elgir cara o sello:")
PJugador=0
PMaquina=0

while PJugador < 5 and PMaquina<5:
    eleccionjugador= input(" Elegir cara o sello: c o s: ")
    
lanzamiento = random.randrange(1,3)
if eleccionjugador == "c":
    monedajugador = 1
else:
    monedajugador = 2


if monedajugador == lanzamiento:
    PJugador +=1
else:
    PMaquina +=1

print("Lanzamiento de moneda: ", lanzamiento)
print("PUntaje juagdor: ",PJugador)
print("Puntaje de maquina: ",PMaquina)




