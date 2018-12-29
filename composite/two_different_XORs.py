import numpy as np
from random  import randint, uniform, shuffle
from solve_sys_multivar_ineq import *


# compose 2 XORS into an embedding for the following circuit

#    X1  X2           
# a --o------- a      a b c o
#     |               0 0 0|0
#     | o1            0 0 1|1
# b --x----o-- b      0 1 0|1
#          |          0 1 1|0
# c -------x-- o      1 0 0|1
#                     1 0 1|0
#                     1 1 0|0
#                     1 1 1|1
#
#
#       a       b       o1              o1       c      o 
# X1a   X1i1    X1i2    X1o  |  X2a     X2i1    X2i2    X2o        line
# 0     0       0       0    |  0       0       0       0          0   
# 0     1       0       1    |  0       1       0       1          85  
# 0     0       1       1    |  0       1       0       1          53
# 0     0       0       0    |  0       0       1       1          3
# 1     1       1       0    |  0       0       0       0          224
# 0     1       0       1    |  1       1       1       0          94
# 0     0       1       1    |  1       1       1       0          62
# 1     1       1       0    |  0       0       1       1          227
# 
# Combined embedding:
#
#                                                  o1 
#              Ancilla         J01 = 6141.6        Output
#           w0 = 9534.0 O------------------------O w1 = 65.4        
#                       |'.    J03 =           .'|',                   
#                       |  ''. -6708.1      .''  |  '--------------.   
#                       |     ''.        .''     |                 |    
#                       |        ''.  .''        |                 |      
#         J02 = -8974.5 |          .''.          | J13 = -2222.2   |      
#                       |       .''    ''.       |                 |     
#                       |    .''J12 =     ''.    |                 |         
#             a         |,.''  -3474.2       ''.,| b               |     
#           w2 = 3408.8 O------------------------O w3 = 2156.8     |
#             Input            J23 = 583.0         Input           |
#                                                                  |
#                                                                  | 
#                                                                  |
#                                                                  |
#                                                                  |
#                                                 o                | J16 = ?
#             Ancilla         J45 = 3263.6        Output           |
#           w4 = 500.0 O------------------------O w5 = 50.0        |   
#                      |'.    J47 =           .'|                  |  
#                      |  ''. -380.0       .''  |                  |  
#                      |     ''.        .''     |                  |   
#                      |        ''.  .''        |                  |    
#          J46 =-300.0 |          .''.          | J57 = -100.0     |    
#                      |       .''    ''.       |                  |   
#                      |    .''J56 =     ''.    |                  |   
#            o1        |,.''  -100.0        ''.,| c                |   
#            w6 = 50.0 O------------------------O w7 = 50.0        |
#              Input   |      J67 = 80.0          Input            |
#                      ',                                          |
#                        '-----------------------------------------'

inputs = ['w2','w3','w7']
outputs = ['w5']



system_inequalities = [
# XOR 1 embedding
'w3 = 2156.8',
'J23 = 583.0',
'J12 = -3474.2',
'J01 = 6141.6',
'w0 = 9534.0',
'J02 = -8974.5',
'J03 = -6708.1',
'w2 = 3408.8',
'J13 = -2222.2',
# XOR 2 embedding
'w4 = 500',
'w5 = 50',
'w7 = 50',
'J45 = 3263.6',
'J46 = -300',
'J47 = -380',
'J56 = -100',
'J57 = -100',
'J67 = 80',

# all couplers btwn XORS zero except J16
'J04 = 0',
'J05 = 0',
'J06 = 0',
'J07 = 0',
'J14 = 0',#-300',
'J15 = 0',#-100',
'J17 = 0',#80',
'J24 = 0',
'J25 = 0',
'J26 = 0',
'J27 = 0',
'J34 = 0',
'J35 = 0',
'J36 = 0',
'J37 = 0',
###########
'w1 = 65.4',
'w6 = 50',
'J16 = -100']

############################################
############################################

besttruecount = 0

stop = False
count = 0
while stop == False:  
    shuffle(system_inequalities)
    symbols = solve(system_inequalities)
    
    correct = evaluate_sys(system_inequalities, symbols)
    truecount = 0
    falses = list()
    for elem in correct:
        #print(elem['valid'], "\t-", elem['inequality'])
        if elem['valid']==True:
            truecount = truecount + 1
        else:
            falses.append(elem['inequality'])
    #print("\n")

    if truecount >= besttruecount:
        best = list()
        for sym in symbols:
            a = [sym.name, sym.value]
            best.append(a)    
        besttruecount = truecount
        #print('best: ', besttruecount)
        bestfalse = falses
    if truecount == len(correct): 
        stop = True
    
    count = count + 1

    if count % 200 == 0:
        s = input('Tried {} times. Stop? (y/n) '.format(count))
        if s == 'y':
            stop = True
        elif s == 'n':
            stop = False
        else:
            stop = False
    print(count)

print("\nSymbol Values: ")
for entry in best:
    print("\t",entry[0],"\t",entry[1])

print('{} were true, {} were false:'.format(besttruecount,len(system_inequalities)-besttruecount))
for i in range(len(bestfalse)):
    print('False: ', bestfalse[i])

import dimod

qubit=list()
qubitweight =list()
coupler=list()
couplerweight=list()
offset = 0

for sym in symbols:
    if 'w' in sym.name:
        qubit.append(sym.name)
        qubitweight.append(sym.value)
    if  'J' in sym.name:
        numbers = sym.name[1:]
        coupler.append(('w{}'.format(numbers[0]), 'w{}'.format(numbers[1])))
        couplerweight.append(sym.value)
    if sym.name == 'offset':
        offset = sym.value

qubit_weights = {q:w for q,w in zip(qubit, qubitweight)}
coupler_weights = {c:w for c,w in zip(coupler,couplerweight)}

print(qubit_weights,coupler_weights)

bqm = dimod.BinaryQuadraticModel(qubit_weights, coupler_weights, offset, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

groundstate = 1000000
for sample, energy in response.data(['sample','energy']):
    if energy<groundstate:
        groundstate = round(energy,1)

function = list()
for sample, energy in response.data(['sample', 'energy']):
    if round(energy,1) == groundstate:
        print(sample, round(energy,1))
        row = []
        for inp in inputs:
            row.append(sample[inp])
        for outp in outputs:
            row.append(sample[outp])
        function.append(row)
print('\n')

function.sort()
for i in range(len(function)):
    print(function[i])
