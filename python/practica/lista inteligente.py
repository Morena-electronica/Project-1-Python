def pedir_numeros():
    lista = []
    cantidad = int(input("¿Cuántos números deseas ingresar? "))
    for i in range(cantidad):
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

numeros = pedir_numeros()
analizar(numeros)

