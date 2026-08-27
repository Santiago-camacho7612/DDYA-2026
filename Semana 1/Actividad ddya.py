def positivo_negativo(numero):
    if numero > 0:
        print("El numero es positivo")
    elif numero < 0:
        print("El numero es negativo")
    else:
        print("El numero es cero")


def fibonacci(numero):
    a = 0
    b = 1

    while a <= numero:
        if a == numero:
            print("Pertenece a Fibonacci")
            return
        c = a + b
        a = b
        b = c

    print("No pertenece a Fibonacci")


def primo(numero):
    if numero < 2:
        print("No es primo")
        return

    i = 2

    while i < numero:
        if numero % i == 0:
            print("No es primo")
            return
        i = i + 1

    print("Es primo")


def suma_intermedios(a, b):
    suma = 0

    if a < b:
        i = a + 1
        while i < b:
            suma = suma + i
            i = i + 1
    else:
        i = b + 1
        while i < a:
            suma = suma + i
            i = i + 1

    print("Suma de intermedios:", suma)


def negativos(a, b):
    if a < 0 and b < 0:
        print("Resultado:", a * b)
    else:
        print("Resultado:", a + b)


def par_impar(numero):
    if numero % 2 == 0:
        print("Resultado:", numero * numero)
    else:
        print("Resultado:", numero * numero * numero)


def obtener_mes(fecha):

    mes = (fecha // 100000000) % 100

    if mes == 1:
        print("enero")
    elif mes == 2:
        print("febrero")
    elif mes == 3:
        print("marzo")
    elif mes == 4:
        print("abril")
    elif mes == 5:
        print("mayo")
    elif mes == 6:
        print("junio")
    elif mes == 7:
        print("julio")
    elif mes == 8:
        print("agosto")
    elif mes == 9:
        print("septiembre")
    elif mes == 10:
        print("octubre")
    elif mes == 11:
        print("noviembre")
    elif mes == 12:
        print("diciembre")
    else:
        print("Mes invalido")


def vocal_consonante(letra):

    if letra == "a":
        print("Vocal")
    elif letra == "e":
        print("Vocal")
    elif letra == "i":
        print("Vocal")
    elif letra == "o":
        print("Vocal")
    elif letra == "u":
        print("Vocal")
    else:
        print("Consonante")


def posicion(letra):

    if letra == "a":
        print(1)
    elif letra == "b":
        print(2)
    elif letra == "c":
        print(3)
    elif letra == "d":
        print(4)
    elif letra == "e":
        print(5)
    elif letra == "f":
        print(6)
    elif letra == "g":
        print(7)
    elif letra == "h":
        print(8)
    elif letra == "i":
        print(9)
    elif letra == "j":
        print(10)
    elif letra == "k":
        print(11)
    elif letra == "l":
        print(12)
    elif letra == "m":
        print(13)
    elif letra == "n":
        print(14)
    elif letra == "o":
        print(15)
    elif letra == "p":
        print(16)
    elif letra == "q":
        print(17)
    elif letra == "r":
        print(18)
    elif letra == "s":
        print(19)
    elif letra == "t":
        print(20)
    elif letra == "u":
        print(21)
    elif letra == "v":
        print(22)
    elif letra == "w":
        print(23)
    elif letra == "x":
        print(24)
    elif letra == "y":
        print(25)
    elif letra == "z":
        print(26)
    else:
        print("No valida")
