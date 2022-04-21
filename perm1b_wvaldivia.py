# Definimos las funciones para mostrar los menús respectivos 
def mostrar_menu():
	print("\n")
	print("1_Retirar")
	print("2_Ver saldo")
	print("3_Salir")
	print("\n")

def mostrar_montos():
	print("\n")
	print("1_S/20")
	print("2_S/50")
	print("3_S/100")
	print("4_S/150")
	print("5_S/500")
	print("6_Ingresar monto")
	print("\n")

# Definimos las variables
clave = "1313"
saldo = 10000

# Pedimos la clave de cajero al usuario 
clave_intento = input("Ingrese la clave : ")
while clave != clave_intento:
	print("Clave equivocada")
	clave_intento= input("Ingrese la clave : ")

# Declaramos un bucle while para mostrar y pedir los datos del cajero 
while clave == clave_intento:
	mostrar_menu()
	opcion = input("Seleccione una opcion : ")
	if opcion == "1":
		mostrar_montos()
		print("Saldo actual : S/", saldo)
		try :
			opcion2 = input("Ingrese una opcion : ")
			if saldo <= 0 :
				print("Se quedo sin fondos, ya no puede retirar")
				continue
			if opcion2 == "1":
				saldo -= 20
			if opcion2 == "2":
				saldo -= 50
			if opcion2 == "3":
				saldo -= 100
			if opcion2 == "4":
				saldo -= 150
			if opcion2 == "5":
				saldo -= 500
			if opcion2 == "6":
				monto_añadido = int(input("Ingrese un monto a añadir(soles) : "))
				saldo += monto_añadido
				if monto_añadido == 0 : 
					print("Usted no puede ingresar S/_0 al cajero")
			print("Saldo actual : S/", saldo)
				
		except :
			print("Ingrese un monto valido ")
			continue
	if opcion == "2":
		print("Saldo actual : S/", saldo)

	if opcion == "3":
		print("Gracias por usar el cajero ")
		break










