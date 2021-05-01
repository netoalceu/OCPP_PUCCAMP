#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import time
import serial           # necessário para importar a biblioteca pyserial

# abre a primeira porta disponível
try:
    port="com7"
    timeout=100
    ser = serial.Serial(port,timeout)    #atenção. esta é a porta padrão para um arduino uno. Altere para o seu caso

except serial.SerialException as e:
    sys.stderr.write("Impossivel abrir porta  %r: %s\n" % (port, e))
    sys.exit(1)

#espera o rest do arduino terminar
print ("Esperando 2 segundos para o reset do arduino")
time.sleep(2)

if ser.isOpen():    #se a porta serial abril corretamente
    print ("Porta serial aberta corretamente")
    # escreve os caracteres  nesta porta

    caracLido = ser.readline()
    print(type(caracLido))
    print(str(caracLido))

    # fecha a porta
    ser.close()
    print ("Porta serial fechada")

else:
    print ("Nao foi possivel abrir a porta serial")
