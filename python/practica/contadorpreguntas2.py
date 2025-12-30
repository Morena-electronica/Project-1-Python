
def analizar(n):
    if n % 2 == 0:
        return "par"
    else:
        return "impar"

cantidad = int(input("¿Cuántos números deseas ingresar? "))

for i in range(cantidad):
    numero = int(input("Ingresa un número: "))
    resultado = analizar(numero)
    print(numero, "es", resultado)
    