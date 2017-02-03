#-*- coding: utf-8 -*-

# kalman1.py
# written by Greg Czerniak (email is greg {aT] czerniak [dOt} info )
#
# Implements a single-variable linear Kalman filter.
#
# Note: This code is part of a larger tutorial "Kalman Filters for Undergrads"
# located at http://greg.czerniak.info/node/5.

# --------------------------------------------------------------------------------------------#
# OBS: ALGORITMO MODIFICADO POR ALYNNE FERREIRA E MATEUS RODRIGUES                            #
# quantidade de números, nome do arquivo com os valores verdadeiros, nome do arquivo com erro #
#                                                                                             #
# argv[1] - quantidade de valores                                                             #
# argv[2] - arquivo com valor real                                                            #
# in - arquivo de entrada (com erros)                                                         #
# --------------------------------------------------------------------------------------------#

import random
import numpy
import pylab
import sys

class Voltmeter:
  def __init__(self,_truevoltage,_noiselevel):
    self.truevoltage = _truevoltage
    self.noiselevel = _noiselevel
  def GetVoltage(self):
    return self.truevoltage
  def GetVoltageWithNoise(self):
    return random.gauss(self.GetVoltage(),self.noiselevel)

numsteps = int(sys.argv[1])

A    = numpy.matrix([1])# matriz de transicao de estado
H    = numpy.matrix([1]) # matriz de observacao
B    = numpy.matrix([0]) # matriz de controle
Q    = numpy.matrix([0.00001]) # erro estimado no processo
R    = numpy.matrix([0.1]) # erro estimado nas medidas
xhat = numpy.matrix([3]) # estimativa inicial do estado
P    = numpy.matrix([1]) # estimativa de covariância inicial

voltmeter = Voltmeter(1.25,0.25)

measuredvoltage = []
truevoltage = []

for i in range(numsteps):
    measured = voltmeter.GetVoltageWithNoise()
    measuredvoltage.append(measured)
    truevoltage.append(voltmeter.GetVoltage())
    
#gravando em arquivos

## valores reais
arq = open('%s.txt' %sys.argv[2],'w')
for i in range (len(measuredvoltage)):
        arq.write(str("1.25"))
        arq.write('\n')    
arq.close()

## valores com erro
arq = open('in.h','w')
arq.write("float DATA[] = {");
for i in range (len(measuredvoltage)-1):
        arq.write(str(round(measuredvoltage[i],2)))
        arq.write(',')    
arq.write(str(round(measuredvoltage[i],2))) #último sem vírgula
arq.write("};")
arq.close()
