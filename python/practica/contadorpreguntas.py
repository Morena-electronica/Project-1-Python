cantidad = int(input("¿cuantos numeros quiere ingresar?: "))

pares = 0
impares = 0

for i in range(cantidad):
    numero = input("ingrese un numero: ")
    if int(numero) % 2 == 0:
        print(numero, "es par")
        pares += 1
    else:
        print(numero, "es impar")
        impares += 1

print("resumen:")
print("pares:", pares)
print("impares:", impares)
print("total:", pares + impares)