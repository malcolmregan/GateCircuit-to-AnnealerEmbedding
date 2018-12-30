import numpy as np
from random  import randint, uniform, shuffle
from solve_sys_multivar_ineq import *


#                                                 'out1'
#             Ancilla         J0,1 = 3263.6       Output
#           w0 = 500.0 O------------------------O,w1 = ?            
#                      |'.   J0,3 =           .'| '',,            
#                      |  ''. -380.0       .''  |     '',,            
#                      |     ''.        .''     |         '',,         
#                      |        ''.  .''        |             '',       
#         J0,2 =-300.0 |          .''.          | J1,3 = -100.0  |      
#                      |       .''    ''.       |                |     
#                      |    .''J1,2 =    ''.    |                |     
#            'a'       |,.''  -100.0        ''.,| 'i'            |     
#            w2 = 50.0 O------------------------O w3 = 50.0      |
#              Input          J2,3 = 80.0         Input          |
#                                                                |
#                                                 'out2'         | J1,7 = ?
#             Ancilla         J4,5= 3263.6        Output         |
#           w4 = 500.0 O------------------------O,w5 = ?         |     
#                      |'.    J4,7 =          .'| ',             |    
#                      |  ''. -380.0       .''  |   ',           |    
#                      |     ''.        .''     |     ',         |     
#                      |        ''.  .''        |       ',       |      
#         J4,6 =-300.0 |          .''.          | J5,7 =  ',  ,,'       
#                      |       .''    ''.       | -100.0  ,,';         
#                      |    .''J5,6 =    ''.    |     ,,''    ',                
#            'b'       |,.''  -100.0        ''.,| ,,''          ',      
#            w6 = 50.0 O------------------------O' 'out1'        |
#              Input         J6,7 = 80.0          w7 = ?         |
#                                                 Input          |
#                                                                |
#                                                 'S'            |
#             Ancilla        J8,9 = 3263.6        Output         | J5,11 = ?
#           w8 = 500.0 O------------------------O w9 = 50.0      |      
#                      |'.   J8,11 =          .'|                |     
#                      |  ''. -380.0       .''  |                |     
#                      |     ''.        .''     |                |      
#                      |        ''.  .''        |                |       
#         J8,10=-300.0 |          .''.          | J9,11 =     ,,'    
#                      |       .''    ''.       | -100.0  ,,''             
#                      |    .''J9,10 =   ''.    |     ,,''                 
#            'c'       |,.''  -100.0        ''.,| ,,''              
#            w10= 50.0 O------------------------O' 'out2'   
#              Input         J10,11 = 80.0          w11 = ?    
#		                                        Input
#
#                           Ground State = ?

inputs = ['w3','w0','w6','w10']
outputs = ['w9']



system_inequalities = [
# XOR 1 embedding
'w0 = 500',
#'w1 = 50',
'w2 = 50',
'w3 = 50',
'J0,1 = 3263.6',
'J0,2 = -300',
'J0,3 = -380',
'J1,2 = -100',
'J1,3 = -100',
'J2,3 = 80',
# XOR 2 embedding
'w4 = 500',
#'w5 = 50',
'w6 = 50',
#'w7 = 50',
'J4,5 = 3263.6',
'J4,6 = -300',
'J4,7 = -380',
'J5,6 = -100',
'J5,7 = -100',
'J6,7 = 80',
# XOR 2 embedding
'w8 = 500',
'w8 = 50',
'w10 = 50',
#'w11 = 50',
'J8,9 = 3263.6',
'J8,10 = -300',
'J8,11 = -380',
'J9,10 = -100',
'J9,11 = -100',
'J10,11 = 80',
# most couplers between XORS 0
'J0,4 = 0',
'J0,5 = 0',
'J0,6 = 0',
'J0,7 = 0',
'J0,8 = 0',
'J0,9 = 0',
'J0,10 = 0',
'J0,11 = 0',
#
'J1,4 = 0',
'J1,5 = 0',
#'J1,7 = 0',
'J1,6 = 0',
'J1,8 = 0',
'J1,9 = 0',
'J1,10 = 0',
'J1,11 = 0',
#
'J2,4 = 0',
'J2,5 = 0',
'J2,6 = 0',
'J2,7 = 0',
'J2,8 = 0',
'J2,9 = 0',
'J2,10 = 0',
'J2,11 = 0',
#
'J3,4 = 0',
'J3,5 = 0',
'J3,6 = 0',
'J3,7 = 0',
'J3,8 = 0',
'J3,9 = 0',
'J3,10 = 0',
'J3,11 = 0',
#
'J4,8 = 0',
'J4,9 = 0',
'J4,10 = 0',
'J4,11 = 0',
#
'J5,8 = 0',
'J5,9 = 0',
'J5,10 = 0',
#'J5,11 = 0',
#
'J6,8 = 0',
'J6,9 = 0',
'J6,10 = 0',
'J6,11 = 0',
#
'J7,8 = 0',
'J7,9 = 0',
'J7,10 = 0',
'J7,11 = 0',
###########
'w1 = 100',
'w7 = 100',
'J1,7 = -100',
'w5 = 200',
'w11 = 400',
'J5,11 = -400']

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
        numbers = str.split(sym.name[1:], ',')
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
