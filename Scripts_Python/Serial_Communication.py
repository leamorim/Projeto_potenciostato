# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 12:27:39 2019

Este Script Python faz os seguintes procedimentos;

    1) Envia para o esp os parâmetros usado no DPV
        Envio na forma: PARAM_01/PARAM_02/PARAM_03/PARAM_04/PARAM_05/e onde 'e' sinaliza o fim do envio
    2) Recebe os valores de corrente medidos
        X --> Valor float referente a coordenada X
        Y --> Valor inteiro referente a corrente faradaica/capacitiva
        Y1 --> Valor inteiro referente a corrente faradaica/capacitiva
    3) Recebe os valores de ajuste de escala
        Zero
        Fundo de escala Positivo
        Fundo de escala Negativo

@author: lucas
"""
import numpy as np
import matplotlib.pyplot as plt
import serial, time

esp = serial.Serial('COM4',115200)
print(esp)
#time.sleep(1)
def start_send():
    a = esp.write(bytes("start".encode()))
    print(a)
    time.sleep(0.01)
    while(1): #Loop que espera o recebimento do 'start' como confirmação para envio dos parâmetros
        data = esp.readline()[:-2]
        if data:
            print(data)
            if bytes.decode(data).find("start") != -1:
                print("ACK start OK")
                break
def end_receive():
    while(1): #Loop que espera o recebimento do 'start' como confirmação para envio dos parâmetros
        data = esp.readline()[:-2]
        if data:
            print(data)
            if bytes.decode(data).find("end") != -1:
                print("ACK end OK")
                break

def start_receive():
    while(1): #Loop que espera o recebimento do 'start' como confirmação para envio dos parâmetros
        data = esp.readline()[:-2]
        if data:
            print(data)
            if bytes.decode(data).find("start") != -1:
                esp.write(bytes("start".encode()))
                print("ACK start OK")
                break




start_send()

V_inicio = -0.6
V_fim = 0.0
V_pulso = 0.01
V_passo = 0.005
T_pulso = 0.01

data_to_send = ascii(V_inicio)+"/"+ascii(V_fim)+"/"+ascii(V_pulso)+"/"+ascii(V_passo)+"/"+ascii(T_pulso)+"/"+"e"
ret = esp.write(bytes(data_to_send.encode()))
print(ret)
end_receive()

''' LEITURA DOS VALORES DO DPV'''
y2 = np.array([])#criando array vazio que vai receber o Y2 (ou I2) do ESP
y1 = np.array([])#criando array vazio que vai receber o Y1 (ou I1) do ESP
y = np.array([])#criando array vazio que vai receber o Y do ESP
x = np.array([])#criano array correspondente as coordenadas X

start_receive()

while(1): #Loop que armazena os dados e encerra ao receber o 'end'    
    data = esp.readline()[:-2] #Coordenada X
    if data:
        if bytes.decode(data).find("end") != -1:
            esp.write(bytes("end".encode()))
            print("ACK end OK")
            break
        else:
            x = np.concatenate((x,np.array(float(bytes.decode(data)))),axis = None)

    data1 = esp.readline()[:-2]#Corrente faradaica ou capacitiva
    if data1:
        y = np.concatenate((y,np.array(int(bytes.decode(data1)))),axis = None)


    data2 = esp.readline()[:-2]#Corrente faradaica ou capacitiva  
    if data2:
        y1 = np.concatenate((y1,np.array(int(bytes.decode(data2)))),axis = None)
        y2 = np.concatenate((y2,np.array(int(bytes.decode(data2)) - int(bytes.decode(data1)))),axis = None)

#Recebendo os valores do ajuste de fundo de escala
start_receive()

while(1): #Loop que armazena os dados e encerra ao receber o 'end'    
    data = esp.readline()[:-2] #Coordenada X
    if data:
        if bytes.decode(data).find("end") != -1:
            esp.write(bytes("end".encode()))
            print("ACK end OK")
            break
        else:
            zero = int(bytes.decode(data))
        
    data = esp.readline()[:-2]#Fundo de escala positivo
    if data:
         f_positivo = int(bytes.decode(data))
    
    data = esp.readline()[:-2]#Fundo de escala negativo
    if data:
         f_negativo = int(bytes.decode(data))

esp.close()

plt.plot(x,y, color = 'blue',label = 'Curva Y')
plt.plot(x,y1, color = 'red',label = 'Curva Y1')
plt.plot(x,y2, color = 'green',label = 'Curva Y1 - Y')
plt.legend(loc='upper left')
plt.show()