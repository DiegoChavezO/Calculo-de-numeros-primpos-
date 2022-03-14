import matplotlib.pyplot as plt
import math 
from random import randint

global ones_amount
global symbols_amount 
list_ones = []
list_symbols = []
#List_String_size = []

#Funcion generica para las gráficas 
def grafica(x_acces, y_acces, str, title):
	plt.clf()
	plt.plot(x_acces,y_acces, color = "green")
	plt.xlabel("Numero de cadena")
	plt.ylabel(str)
	plt.ticklabel_format(style = 'plain')
	plt.title(title)
	plt.grid()
	plt.show()
		

def generador_binario(num, n_bits):
    containter = ""
    for i in range(n_bits):  
        bit = num % 2
        containter += str(bit)
        num = num // 2

    return containter[::-1] #retorna la lista pero de atrás para delante

''' Python program to print all primes smaller than or equal to
 n using Sieve of Eratosthenes''' 
def SieveOfEratosthenes(n):
     
    '''Create a boolean array "prime[0..n]" and initialize
     all entries it as true. A value in prime[i] will
     finally be false if i is Not a prime, else true.'''
    prime = ""
    prime = [True for i in range(n + 1)]
    p = 2
    #counter = 0
    while (p * p <= n):
         
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
             
            # Update all multiples of p
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    # Print all prime numbers
    file = open("NumPrims.txt","w",) 
    file.write('{ e')
    filebin = open("PrimosBinarios.txt","w")
    filebin.write('{ e')
    
    ones_amount = 0
    symbols_amount = 0 
    counter = 0
    List_String_size = []
    for p in range(n + 1):
       
        if prime[p]:
            #p = ""
            dec_prim = generador_binario(p,n)
            file.write(", "+ str(p)) 
            filebin.write(", "+ dec_prim.lstrip("0"))
            ones_amount += dec_prim.count('1')	
            symbols_amount += 1 *len(dec_prim.lstrip("0")) #* n
            list_ones.append(ones_amount)
            list_symbols.append(symbols_amount)

            ones_amount = 0
            symbols_amount = 0
            counter += 1
            List_String_size.append(counter)

    file.write("}")
    file.close()
    filebin.write("}")
    filebin.close()


    #graficas
  
    log_symbols = [ math.log10(elements ) for elements in list_symbols ]
    log_ones = [ math.log10(elements) for elements in list_ones ]
    
    grafica(List_String_size, list_symbols,"Numero de simbolos en la cadena","Gráfica 1: numero de simbolos")
    grafica(List_String_size, log_symbols,"Numero de simbolos en logaritmo en la cadena","Gráfica 2: logaritmo base 10 de la primer lista")
    grafica(List_String_size, list_ones,"Numero de 1's en la cadena","Gráfica 3: numero de 1's en la cadena")
    grafica(List_String_size, log_ones,"Numero de 1's con logaritmo en la cadena","Gráfica 4: Logaritmo base 10 de la tercer lista")

    
 
n = int(input("Ingrese un número para el cuál desee generar dicha cantidad de primos:\n"))
SieveOfEratosthenes(n)