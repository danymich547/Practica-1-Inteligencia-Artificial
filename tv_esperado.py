print("INSERTE DATOS DE LA PRIMERA OPCION\n")
valor1 = float(input("Cantidad a ganar:\t"))
probabilidad1 = float(input("Probabilidad de ganar:\t"))
valor2 = float(input("Cantidad a perder:\t"))
probabilidad2 = float(input("Probabilidad de perder:\t"))

print("\n\nINSERTE DATOS DE LA SEGUNDA OPCION\n")
valorA = float(input("Cantidad a ganar:\t"))
probabilidadA = float(input("Probabilidad de ganar:\t"))
valorB = float(input("Cantidad a perder:\t"))
probabilidadB = float(input("Probabilidad de perder:\t"))

print("\nLa primera opcion es:\nGanar ", valor1," con ", probabilidad1, " de probabilidad o perder ", valor2, " con ", probabilidad2, " de probabilidad ")
print("\nLa segunda opcion es:\nGanar ", valorA," con ", probabilidadA, " de probabilidad o perder ", valorB, " con ", probabilidadB, " de probabilidad ")

resultado1 = ((valor1*(probabilidad1/100)) - (valor2*(probabilidad2/100)))
resultado2 = ((valorA*(probabilidadA/100)) - (valorB*(probabilidadB/100))) 

if(resultado1>resultado2):
	print("\n MEJOR RESULTADO: PRIMERA OPCION :3")
else:
	print("\n MEJOR RESULTADO: SEGUNDA OPCION :3")
