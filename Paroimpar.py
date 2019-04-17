#Programa que te dice si un numero es par o impar
numero=int(input("\tIngresa un numero y te dire si es par o no"))
div=numero%2
if (div == 0):
    print("El numero es par")
else:
    print("El numero es impar")