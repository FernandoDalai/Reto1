import random

aleatorio = random.randint(1,101)
intentos = 0
listaIntentos = []
#n = 0 
max = 100
min = 1
a = 100
b = 1

n = input("Ingrese un número entero dentro del intervalo [1,100]: ")

def int_test(string):
  
    if string[0] == ('-'):
        return string[1:].isdigit()

    else:
        return string.isdigit()


def verification(p):
    while not int_test(p):
        p = input("Ingrese un número dentro del intervalo: ")
        
    return int(p)


n = verification(n)


while n<1 or n>100:
    print("El número esta fuera del intervalo")
    n = input("Ingrese un número entero dentro del intervalo [1,100]: ")
    n = verification(n)


while True:

    while aleatorio!=n: 

        listaIntentos.append(n)

        if n==aleatorio:
            print("Felicidades a adivinado el número al primer intento")    
            
        elif n>max:
                print(f"El número se encuentra entre {min} y {a}")
                n = input("Ingrese otro número: ")
                n = verification(n)


        elif n<min:
                print(f"El número se encuentra entre {b} y {max}")
                n = input("Ingrese otro número: ")
                n = verification(n)

            
        elif n>aleatorio:
            a = max = n
            print(f"El número se encuentra entre {min} y {n}")
            n = input("Ingrese un número: ")
            n = verification(n)
            intentos += 1
                
        elif n<aleatorio:
            b = min = n
            print(f"El número se encuentra entre {n} y {max}")
            n = input("Ingrese un número: ")
            n = verification(n)
            intentos += 1


    print(f"Felicidades a adivinado el valor del número despues de {intentos} intentos")
    print(f"Números fallidos = {listaIntentos}")
    break

        


