numeros = ["16", "97", "24", "81", "53", "31", "92", "78", "45", "666"]

pares = 0
impares = 0

for n in numeros:
    if int(n) % 2 == 0:
        print(n, "es par")
        pares += 1
    else:
        print(n, "es impar")
        impares += 1

print("resumen:")
print("pares:", pares)
print("impares:", impares)
print("total de números:", len(numeros))