# Este programa se encarga de cifrar y descifrar mensajes mediante el algoritmo de RSA
#from pruebaa import *
#ERML
import time 
import os

# Algoritmo de creacion de clave privada

def createPrivateKey (var):
	p = int (input ("Ingrese un número primo:\n>> "))
	q = int (input("Ingrese un segundo número primo:\n>> "))
	n = p * q
	#option nos permite decidir entre cifar numeros o caracteres
	option = []
	# phi(n) es el número phi de euler que nos devuelve como valor la cantidad de números coprimos de n 
	""" Aplicando propiedades obtenemos que:
	phi(n) = phi (q) * phi (p) = (p-1) (q-1) """

	phi = (p-1) * (q-1)
	#while True:
	print("Ingrese su CLAVE PÚBLICA:\n\n","*"*100,"\n","La clave pública debe ser un número primo menor que",n,"\n(recomendado: 65537)\n\n","*"*100,"\n")
	public_key = int (input(">> "))
	#check(public_key)

	private_key = euclides(phi, public_key)
	cifrate_mess = cifrate(public_key,n,option)
	print ("El mensaje cifrado es: ",cifrate_mess)
	print ("\n\nPara decifrar el mensaje escriba DES, para salir presione cualquier tecla:")
	command = input (">> ")
	timer = 0
	while timer < 3:
		os.system(var) 
		print("descifrando.\r")
		time.sleep(0.35)
		os.system(var) 
		print("descifrando..\r")
		time.sleep(0.35)
		os.system(var) 
		print("descifrando...\r")
		time.sleep(0.35)
		timer = timer + 1
	if command == "des" or command == "DES":  
		messagge = descifrate (private_key,cifrate_mess,n)
		if option [0] == "t" or option [0] == "T":
			print ("El mensaje es: ", changeStr(messagge))
		else:
			print ("El mensaje es: ",messagge)
	else:
		print ("Fin del programa")



# Algoritmo de creacion de cifrado 

def cifrate (public_key,n,option):
    while True:
        option.append(input("Para cifarar texto pesione T , para numeros presione N\n>> "))
        if option[0] == "t" or option[0] == "T":
            while True:
                print ("ingrese el mensaje a cifrar (máximo", (len(str(n))-1)//2, "caracteres contando espacios): ")
                char_messagge = input(">> ")
                char_messagge = char_messagge.upper()
                messagge = changeAscci(char_messagge)
                # Verifica que el mensaje sea menor que n de lo contrario no se puede cifrar
                if messagge < n:
                    break
                # Fin del verificado
            break
        elif option[0] == "n" or option[0] == "N":
            # Este bucle obliga al usuario a ingresar números
            while True:
                try:
                    # Verifica que el mensaje sea menor que n de lo contrario no se puede cifrar
                    while True:
                        print("ingrese el número a cifrar menor que",n,"(",len(str(n)),"digitos):")
                        messagge = int(input(">> "))
                        if messagge < n:
                            break
                    # Fin del verificado
                    break
                except ValueError:
                    print("ERROR Ingrese sólo números\n")
            break
        else:
            print("ERROR\n")
    cifrate_message = 1
    binary_figures = []
    # El siguiente algoritmo obtinene las cifras binarias 
    while public_key != 0:
        if public_key % 2 == 0:
            public_key = public_key / 2
            binary_figures.append(0)
        elif public_key % 2 != 0:
            public_key = (public_key - 1) / 2
            binary_figures.append(1)

    if binary_figures[0] == 1:
        cifrate_message = cifrate_message * messagge
    for i in binary_figures[1:]:
        messagge = (messagge * messagge) % n
        if i == 1:
            cifrate_message = cifrate_message * messagge
    cifrate_message = cifrate_message %  n
    return cifrate_message

# Algoritmo para decifrar 

def descifrate (private_key,cifrate_mess,n):
	descifrate_message = 1
	binary_figures = []
	# El siguiente algoritmo obtinene las cifras binarias 
	while private_key != 0:
		if private_key % 2 == 0:
			private_key = private_key / 2
			binary_figures.append(0)
		elif private_key % 2 != 0:
			private_key = (private_key - 1) / 2
			binary_figures.append(1)

	if binary_figures[0] == 1:
		descifrate_message = descifrate_message * cifrate_mess
	for i in binary_figures[1:]:
		cifrate_mess = (cifrate_mess ** 2) % n
		if i == 1:
			descifrate_message = descifrate_message * cifrate_mess
	descifrate_message = descifrate_message %  n
	return descifrate_message

def changeAscci(messagge):
	ascci_messagge = ""
	for i in messagge:
		#la funcion str convierte los numeros en cadenas
		#para poder concatenarlas despues y ord convierte las letras a ascii
		ascci_char = str(ord(i))
		# se concatenan todos los digitos para formar un numero operable
		ascci_messagge = ascci_messagge + ascci_char
	# se convierte el mensaje a un entero para poder manipularlo
	ascci_messagge = int (ascci_messagge)
	return ascci_messagge


def changeStr(messagge):
	descifrate_phrase = ""
	str_messagge = str(messagge)
	count = len(str_messagge)
	i = 0
	while i< count-1:
		str_word = (str_messagge[i]+str_messagge[i+1])
		word = chr(int(str_word))
		descifrate_phrase = descifrate_phrase + word
		i = i + 2
	return(descifrate_phrase)



# Check define si el numero ingresado es primo o no
def check(primo):
	# rset se define como el resto 
	rset= 0
	flag = 0
	for i in range (2, primo):
		if rset != 0:
			break
		else:
			rset = primo % i;
	
	if (rset == 0):
		return flag
	
	else: 
		flag = 1
		return flag

""" Esta funcion nos permite encontrar el modulo inverso de a medinate una version del algoritmo extendido de Euclides """

def euclides (modulo,public_key):
	# las siguientes variavles representan los valores de la matriz
	u = [1,0]
	v = [0,1]
	y = [0,0]
	g = [modulo, public_key]
	i = 1
	while g[i] != 0:
		y.append(g[i-1] // g[i])
		g.append(g[i-1] - (y[i+1] * g[i]))
		u.append(u[i-1] - (y[i+1] * u[i]))
		v.append(v[i-1] - (y[i+1] * v[i]))
		i = i+1
	if v[i-1] < 0:
		v[i-1] = v[i-1] + modulo
	return v [i-1]







if __name__ == "__main__":
	if os.name == "posix":
		var = "clear"        
	elif os.name == "ce" or os.name == "nt" or os.name == "dos":
		var = "cls"
	os.system(var) 
	print("#"*20,"CIFRADO CON EL ALGORITMO RSA","#"*20,"\n\n\n")
# la clave queda de la forma c (clave cifrada = x ** k (mod n))
	answer = "Y"
	while answer != "n" and answer !="N":
		createPrivateKey(var)
		answer = input("\n\nDesea cifrar otro mensaje? (Y/N) \n>>")
		os.system(var) 



