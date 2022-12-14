#import matplotlib.pyplot as plt
#from pylab import *
import serial
import time


#########################################    FUNCIONES    ########################################################
def recoger_datos_tension():
    valor = serialArduino.readline().decode('ascii','replace')
    print(valor)
    
    #print(mi_lista)
    #return valor
"""




def ordenar_dato_en_lista(element):
    longitud = len(element)
    if ((element != "") and (longitud != 8)):
        first_char = element[0]
        first_number = 4
        elemento_cortado = float(element[first_number:])
        
        if (first_char == '0'): lista_A0.append(elemento_cortado);
        if (first_char == '1'): lista_A1.append(elemento_cortado);
        if (first_char == '2'): lista_A2.append(elemento_cortado);
        if (first_char == '3'): lista_A3.append(elemento_cortado);
            
            
def imprimir_grafico(lista):
    plot(lista)
    show()
"""

##########################################    VARIABLES   ###############################################

TENSION_MINIMA = 0,2
contador = 0
cont = contador

lista_A0 = []
lista_A1 = []
lista_A2 = []
lista_A3 = []

MAX_VUELTAS = 10


lista_en_crudo = []


#serialArduino = serial.Serial("COM3", 9600)
serialArduino = serial.Serial("/dev/ttyACM0", 9600)
time.sleep(1)

#/dev/ttyACM0



########################################    PROGRAMA   #############################

while contador != MAX_VUELTAS:
    valor = recoger_datos_tension();
    contador += 1;
    
"""
# ACTIVAR en arduino
"""
"""

    
    if (valor >= TENSION_MINIMA):
        lista_en_crudo += valor;
        #lista_en_crudo.append(valor)


cadena = cadena_en_crudo.split("A");
for elemento in cadena:
    ordenar_dato_en_lista(elemento);
    

imprimir_grafico(lista_A0)
imprimir_grafico(lista_A1)
imprimir_grafico(lista_A2)
imprimir_grafico(lista_A3)
"""


        
    #while contador  != MAX_VUELTAS and comprovar0==1:
    #    valor = recoger_datos_tension()
    #    valor= valor/10000
    #    print(valor)
    #    lista.append(valor)
    #    print("*********")
    #    contador +=1
    #    if valor_maximo <=valor:
    #        valor_maximo =valor


#print(valor_maximo )