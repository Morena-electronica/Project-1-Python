def pedir_cantidad():
    while True:
        try:
            cantidad = int(input("¿Cuántos números deseas ingresar? "))
            if cantidad > 0:
                return cantidad
            else:
                print("La cantidad debe ser mayor que 0")
        except:
            print("Por favor, ingresa un número entero válido.")

def pedir_numero(cantidad):
    lista = []
    
    for i in range(cantidad):
        while True:
            try:
                n = int(input("Ingresa el número: "))
                if n >= 0:
                    lista.append(n)
                    break
                else:
                    print("No se permiten números negativos.")
                    
            except:
                print("Por favor, ingresa un número entero válido.")

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

cantidad = pedir_cantidad()
numeros = pedir_numero(cantidad)
analizar(numeros)