import random, string

def creaPass(n):
    todas = list(string.ascii_letters)+list(string.digits)+list(string.punctuation)
    passw = []

    for i in range(8):
        tmp = random.choice(todas)
        passw.append(tmp)
    res = "".join(passw)
    return res

n = int(input("Ingrese contraseña de 8 digitos en adelante: "))
if n >=8:
    test = creaPass(n)
    print(test)

else:
    print("Numero invalido. Intentelo de nuevo.")
