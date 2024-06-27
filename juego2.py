import random



puntojugador=0
puntomaquina=0


while puntojugador < 3 and puntomaquina < 3:

    print(" Juego de 'piedra' , 'papel' , 'tijeras' ")

    maquina= random.choice(["piedra","papel","tijeras"])
    

    jugador = input("Elija una opcion: ")
     



    if jugador == "papel":
        punto = 1
    else:
        punto = 2

    if punto==jugador:
        puntojugador +=1
    else:
        puntomaquina +=1
    
    #Piedra

    if jugador=="piedra":
        if maquina=="piedra":
            print("Maquina elige 'piedra'. Empate. ")
        elif maquina== "papel":
            print("Maquina elige 'papel'. Papel envuelve a piedra. Pierdes.")
        else:
            print("Maquina elige 'tijeras'. Piedra rompe a tijeras. Ganas")

    #Papel

    elif jugador=="papel":
        if maquina=="piedra":
            print("Maquina elige 'piedra'. Papel envuelve piedra. Ganas.")
        elif maquina=="tijeras":
            print("Maquina elige 'tijeras'. Tijeras corta papel. pierdes")
        else:
            print("Maquina elige 'papel'. Empate. ")

    #Tijeras

    elif jugador=="tijeras":
        if maquina=="piedra":
            print("Maquina elige 'piedra'. Piedra rompe tijeras. Pierdes")
        elif maquina=="papel":
            print("Maquina elige 'papel'. Tijeras corta papel. Ganas. ")
        else:
            print("Maquina elige 'tijeras'. Empate.")

      
    
    else:
        print("No has elegido una opcion correcta.")


   
    print("Puntaje jugador",puntojugador)
    print("puntaje maquina",puntomaquina)







    

