
numeros=["1","2","3","4","5","6","7","8","9","10"]

for i in numeros:
    if int(i) % 2 == 0:
        print(i, "es par")
    else:
        print(i, "es impar")

print("¡Terminó el conteo!")

print("Cantidad de números:", len(numeros))

pares = 0

for i in numeros:
    if int(i) % 2 == 0:
        pares += 1

print("Cantidad de pares:", pares)


    