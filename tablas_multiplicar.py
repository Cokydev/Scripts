#Programa que genera las tablas de multiplicacion
numero = int(raw_input("Dijite el numero de la tabla de multiplicacion: "))
for x in range(0,11): #Hace una pregunta
	print str(x)+" * "+ str(numero)+ " = "+str((numero * x)) #Ejecuta una o varias acciones
	# Primera iteracion: imprime 0 * 5 = 0
	#Segunda iteracion: 1 * 5 = 5
	#Tercera iteracion: 2 * 5 = 10
	#....