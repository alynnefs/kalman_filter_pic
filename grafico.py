import time
import serial
import sys
import matplotlib.pyplot as plt
'''
def gera_grafico(_arq_real, _arq_in, _arq_out,_x,_y):
    entrada = []
    saida = []
    real = []

    for line in _arq_real:
        real.append([line])
        
    for line in _arq_in:
        entrada.append([line])

    for line in _arq_out:
        saida.append([line])

    x = [c for c in range(len(entrada))]

    print len(entrada)
    print len(saida)

    plt.plot(x, real, linestyle='--', color='g', marker='s', linewidth=3.0)
    plt.plot(x, entrada, linestyle='--', color='r', marker='s', linewidth=3.0)
    plt.plot(x, saida, linestyle='--', color='b', marker='s', linewidth=3.0)


    plt.axis([0,_x,0,_y])

    plt.xlabel(u'Tempo')
    plt.ylabel(u'Valores')
    plt.show()

'''

def main():
    arq_in = open('voltagein.txt','w')
    arq_out = open('voltageout.txt','w')
    arq_in2 = open('cannonin.txt','w')
    arq_out2 = open('cannonout.txt','w')
    
    # configure the serial connections (the parameters differs on the device you are connecting to)
    ser = serial.Serial(
        port='/dev/ttyUSB1',
        baudrate=9600
    )

    print(ser.isOpen())

    cont = 0
    while cont < 800:
        valor = ser.readline()
        print(valor)
        print(valor.split('\t')[1])
        print(valor.split('\t')[2].strip('\n'))
        arq_in.write(str(valor.split('\t')[1])+'\n')
        arq_out.write(str(valor.split('\t')[2].strip('\n'))+'\n')
        cont += 1
    cont = 0
    
    while cont < 800:
        valor = ser.readline()
        print(valor)
        print(valor.split('\t')[1])
        print(valor.split('\t')[2].strip('\n'))
        arq_in2.write(str(valor.split('\t')[1])+'\n')
        arq_out2.write(str(valor.split('\t')[2].strip('\n'))+'\n')
        cont += 1

    arq_in.close()
    arq_out.close()
  
    arq_in2.close()
    arq_out2.close()
    
'''
    arq_real = open('voltagereal.txt','r')
    arq_in = open('voltagein.txt','r')
    arq_out = open('voltageout.txt','r')
    arq_real = open('cannonreal.txt','r')
    arq_in2 = open('cannonin.txt','r')
    arq_out2 = open('cannonout.txt','r')
    
    gera_grafico(arq_real,arq_in,arq_out,2,800)
    gera_grafico(arq2_real,arq2_in,arq2_out,400,400)
'''
main()