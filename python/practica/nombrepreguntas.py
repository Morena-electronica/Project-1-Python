nombres = []

n = int(input("¿Cuántos nombres deseas ingresar? "))

for i in range(n):
    nombre = input("Ingresa el nombre:")
    nombres.append(nombre)

print("Los nombres ingresados son:")
for nombre in nombres:
    print(nombre)

print("Total:", len(nombres))