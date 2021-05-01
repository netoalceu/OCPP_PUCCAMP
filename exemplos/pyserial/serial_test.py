#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import serial
import time
# https://cleitonbueno.com/python-comunicacao-serial-com-arduino/
# http://www.roboliv.re/conteudo/pyserial-python-comunicando-com-arduino
# https://cadernodelaboratorio.com.br/a-biblioteca-pyserial-i/
# https://cadernodelaboratorio.com.br/a-biblioteca-pyserial-ii/

# https://cadernodelaboratorio.com.br/comunicacao-serial-pc-arduino-em-python/



ser = serial.Serial('COM7', 9600)
time.sleep(3)

#ser.write(b'hello')
print(" Olha o que chegou ")
tempo = 0
while (tempo < 10):
    textoEncoded = ser.readline()
    textoEntrada = textoEncoded.decode('utf-8')
    print(textoEntrada)
    time.sleep(10)
    tempo +=1

ser.close()
