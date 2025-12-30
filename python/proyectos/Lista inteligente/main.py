def pedir_cantidad():
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de numeros: "))
            if cantidad > 0:
                return cantidad
            else:
                print("Por favor, ingrese un número positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

def pedir_numeros(cantidad):
    lista = []
    for i in range(cantidad):
        while True:
            try:
                n = int(input(f"Ingrese el numero: "))
                if n >= 0:
                    lista.append(n)
                    break
                else:
                    print("Por favor, ingrese un número no negativo.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero.")
    return lista

def analizar_lista(lista):
    pares = 0
    impares = 0

    for n in lista:
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1
    print("Resumen:")
    print(f"Números pares: {pares}")
    print(f"Números impares: {impares}")
    print(f"Total de números: {len(lista)}")

def main():
    cantidad = pedir_cantidad()
    numeros = pedir_numeros(cantidad)
    analizar_lista(numeros)

main()
