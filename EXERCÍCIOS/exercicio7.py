'''Programa que solicite o número de litros de gasolina e a quilometragem e imprima o consumo'''

litros = float(input("Digite a quantidade de litros de gasolina consumidos: "))
km = float(input("Digite a quilometragem percorrida: "))

consumo = km/litros

print(f"O consumo foi de: {consumo} km/l")

