def pedir_numero():
    lista = []
    cantidad = int(input("¿Cuántos números deseas ingresar? "))

    while cantidad <= 0:
        print("La cantidad debe ser mayor que 0")
        cantidad = int(input("¿Cuántos números deseas ingresar? "))

    for i in range(cantidad):
        n = int(input("Ingresa el número: "))
        while n < 0:
            print("No se permiten números negativos.")
            n = int(input("Ingresa el número: "))
        lista.append(n)

    return lista

def analizar(lista):
    pares = 0
    impares = 0

    for n in lista:
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1

    print("Números pares:", pares)
    print("Números impares:", impares)
    print("Números totales:", len(lista))

numeros = pedir_numero()
analizar(numeros)