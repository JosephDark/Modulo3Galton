import numpy as np
import matplotlib.pyplot as plt
from random import randint

def grafica(carriles2):
    """
    Funcion que grafica los resultados obtenidos de la maquina de Galton
    """
    abcisa = []                 #Creamos una lista de 12 elementos, del 1 al 12, para rotular el eje de las abcisas.
    for i in range(12):         #Llenamos con los valores del 1 al 12 mediante un ciclo for
        abcisa.append(i+1)

    plt.suptitle('Simulacion de la Maquina de Galton') #Titulamos al grafico
    plt.ylabel("Cantidad de pelotas Eje Y")            #Rotulamos al eje Y
    plt.xlabel("Distribucion de pelotas Eje X")        #Rotulamos al eje X
    plt.bar(abcisa, carriles2,width=1)                 #Mandamos los valores de X y Y, junto con el ancho de columna  
    plt.show()                                         #Ejecutamos el gráfico 


def calculo(niveles,carril ):
    """
    Función que se encarga del calculo de las palotas lanzandas a la maquina de Galton
    """
    carriles = []     #Lista que recibe la sumatoria de en que carril cae cada pelota
    for i in range(niveles):     #Inicializamos la lista a 12 elementos en 0 con funcion append
        valor = 0
        carriles.append(valor)



    for i in range((carril)*250):   #Ciclo for que maneja cada una de las 3000 pelotas arrojadas a la máquina
        guarda = -1                 #Inicializamos el contador que guarda el valor de los movimientos de la pelota con -1
        for j in range(carril):     #para que vaya contando cada uno de los 12 pasos que recorre la pelota
            
            guarda = guarda + randint(0,1)  #Generammos el movimiento aleatorio con randint en 1 o 0 para determinar la direccion
        carriles[guarda] += 1               #Al terminar el ciclo, aumantamos en uno la casilla del carril donde cayó la pelota.    
                                            #El ciclo de la la siguiente pelota comienza.    

    print((niveles)*250, "pelotas")     #Imprimimos la cantida de pelotas lanzadas
    print("Resultados por carril: ",carriles)  #Imprimimos la cantida de pelotas recolectadas por carril
    print ("Total de carriles", len(carriles))

    

    #LLAMAMOS A LA SEGUNDA FUNCION DEL PROGRAMA, LA DE GRAFICACION, PASANDO LA LISTA DE RESULTADOS DE CARRIL 
    grafica(carriles)
    

#LLAMAMOS A LA PRIMERA FUNCION DEL PROGRAMA, LA DE CALCULO DE PELOTAS POR CARRIL, PASANDO EL NUMERO DE NIVELES Y CARRILES 
calculo(12,12)
