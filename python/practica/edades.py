nombre = input("¿Cual es tu nombre?: ")

edad = input("¿Cual es tu edad?: ")

if edad >= str(18):
    print("eres un adulto!")

else:
    print("eres menor todavia!")

color_fav = input("¿cual es tu color favorito?: ")

print("hola " + nombre + " tu edad es: " + edad + " y tu color favorito es: " + color_fav)