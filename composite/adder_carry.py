import numpy as np
from random  import randint, uniform, shuffle
from solve_sys_multivar_ineq import *


#                                                  J0,7 = ?
#                   ,-----------------------------------------------------------------,
#                  |                     Ancilla                                      |
#                  |                    w0 = 8463.2                                   |
#            ,-----|-----------------------,o,----------------------------,           |
#            |     |   J0,1 = 8625.9 ,,,'''   ''',,,J0,2 = -9566.3        |           |
#            |     '-------,      ,'                ',                    |           |
#            |     'out1'   ',  ,'   J1,2 = -8244.1   ',      'i'         |           |
#            |     w1 = ?     'O------------------------O w2 = 6313.9     |           |
#            |                 |'. J1,4 =             .'|                 |           |
#            |J0,3 =           |  ''. -1926.5      .''  |                 |J0,4 =     |
#            | -1503.0         |     ''.        .''     |                 | -5659.2   |
#            |                 |        ''.  .''        |                 |           |
#            |    J1,3 = -14.3 |          .''.          | J2,4 = 1926.5   |           |
#            '---,             |       .''    ''.       |             ,---'           |
#                 ''',,,       |    .''J2,3 =    ''.    |       ,,,'''                |
#                       ''',,, |,.''   14.3         ''.,| ,,,'''                      |
#                    w3 = ?   'O------------------------O'w4 = ?                      |
#                     'x'    ,'       J3,4 = 10.6       |  'y'                        |
#      J3,13 = ?           ,'                          ,'                             | 
#  ,----------------------'    J4,8 = ?              ,'                               |
# |     ,-------------------------------------------'                                 |
# |    |                                                                              | 
# |    |                                          J6,12 = ?                           |
# |    |            ,-----------------------------------------------------------------|--.
# |    |           |                     Ancilla                                      |  |
# |    |           |                    w5 = 8463.2                                   |  |
# |    |     ,-----|-----------------------,o,----------------------------,           |  |
# |    |     |     |   J5,6 = 8625.9 ,,,'''   ''',,,J5,7 = -9566.3        |           |  |
# |    |     |     '-------,      ,'                ',        ,,----------|-----------'  |
# |    |     |     'out2'   ',  ,'   J1,2 = -8244.1   ',  ,,''            |              |
# |    |     |     w6 = ?     'O------------------------O'w7 = ?          |              |
# |    |     |                 |'. J6,9 =             .'|      'out1'     |              |
# |    |     |J5,8 =           |  ''. -1926.5      .''  |                 |J5,9 =        |
# |    |     | -1503.0         |     ''.        .''     |                 | -5659.2      |
# |    |     |                 |        ''.  .''        |                 |              |
# |    |     |    J6,8 = -14.3 |          .''.          | J7,9 = 1926.5   |              | 
# |    |     '---,             |       .''    ''.       |             ,---'              |
# |    |          ''',,,       |    .''J7,8 =    ''.    |       ,,,'''                   |
# |    |                ''',,, |,.''   14.3         ''.,| ,,,'''                         |
# |    |             w8 = ?   'O------------------------O'w9 = ?                         |
# |    |               'y'     |      J8,9 = 10.6       |  'z'                           | 
# |    |                      ,'                        ',                               |
# |    |                    ,'                            ',    J9,14 = ?                | 
# |     '------------------'                                '------------------,         |
# |                                      Ancilla                                ',       |
# |                                    w10 = 8463.2                               ',     |
# |          ,-----------------------------,o,----------------------------,         ',   |
# |          |       J10,11 = 8625.9 ,,,'''   ''',,,J10,12 = -9566.3      |          |   |
# |          |                    ,'                ',        ,,----------|----------|--'
# |          |        'C'       ,'   J1,2 = -8244.1   ',  ,,''            |          |
# |          |    w11 = 1930.2 O------------------------O'w12 = ?         |          |
# |          |                 |'. J11,14 =           .'|       'out2'    |          | 
# |          |J10,13 =         |  ''. -1926.5      .''  |                 |J10,14 =  | 
# |          | -1503.0         |     ''.        .''     |                 | -5659.2  | 
# |          |                 |        ''.  .''        |                 |          |
# |          |       J11,13 =  |          .''.          | J12,14 =        |          |
# |          '---,       -14.3 |       .''    ''.       |  1926.5     ,---'          |
# |               ''',,,       |    .''J12,13 =  ''.    |       ,,,'''               |
# |                     ''',,, |,.''   14.3         ''.,| ,,,'''                     |
# |                  w13 = ?  'O------------------------O'w14 = ?                    |
# |                     'x'    |    J13,14 = 10.6       |   'z'                      | 
#  '--------------------------'                          '--------------------------'  

inputs = ['w2','w3','w4','w9']
outputs = ['w11']

system_inequalities = [
# Toffoli 1
'w0 = 8463.2',
#'w1 = 1930.2',
'w2 = 6313.9',
#'w3 = 0',
#'w4 = 0',
'J0,1 = 8625.9',
'J0,2 = -9566.3',
'J0,3 = -1503.0',
'J0,4 = -5659.2',
'J1,2 = -8244.1',
'J1,3 = -14.3',
'J1,4 = -1926.5',
'J2,3 = 14.3',
'J2,4 = 1926.5',
'J3,4 = 10.6',
# Toffoli 2
'w5 = 8463.2',
#'w6 = 1930.2',
#'w7 = 6313.9',
#'w8 = 0',
#'w9 = 0',
'J5,6 = 8625.9',
'J5,7 = -9566.3',
'J5,8 = -1503.0',
'J5,9 = -5659.2',
'J6,7 = -8244.1',
'J6,8 = -14.3',
'J6,9 = -1926.5',
'J7,8 = 14.3',
'J7,9 = 1926.5',
'J8,9 = 10.6',
# Toffoli 3
'w10 = 8463.2',
'w11 = 1930.2',
#'w12 = 6313.9',
#'w13 = 0',
#'w14 = 0',
'J10,11 = 8625.9',
'J10,12 = -9566.3',
'J10,13 = -1503.0',
'J10,14 = -5659.2',
'J11,12 = -8244.1',
'J11,13 = -14.3',
'J11,14 = -1926.5',
'J12,13 = 14.3',
'J12,14 = 1926.5',
'J13,14 = 10.6',
# Most couplers btwn Toffoli gates 0
'J0,5 = 0',
'J0,6 = 0',
'J0,7 = 0',
'J0,8 = 0',
'J0,9 = 0',
'J0,10 = 0',
'J0,11 = 0',
'J0,12 = 0',
'J0,13 = 0',
'J0,14 = 0',
#
'J1,5 = 0',
'J1,6 = 0',
#'J1,7 = 0',
'J1,8 = 0',
'J1,9 = 0',
'J1,10 = 0',
'J1,11 = 0',
'J1,12 = 0',
'J1,13 = 0',
'J1,14 = 0',
#
'J2,5 = 0',
'J2,6 = 0',
'J2,7 = 0',
'J2,8 = 0',
'J2,9 = 0',
'J2,10 = 0',
'J2,11 = 0',
'J2,12 = 0',
'J2,13 = 0',
'J2,14 = 0',
#
'J3,5 = 0',
'J3,6 = 0',
'J3,7 = 0',
'J3,8 = 0',
'J3,9 = 0',
'J3,10 = 0',
'J3,11 = 0',
'J3,12 = 0',
#'J3,13 = 0',
'J3,14 = 0',
#
'J4,5 = 0',
'J4,6 = 0',
'J4,7 = 0',
#'J4,8 = 0',
'J4,9 = 0',
'J4,10 = 0',
'J4,11 = 0',
'J4,12 = 0',
'J4,13 = 0',
'J4,14 = 0',
#
'J5,10 = 0',
'J5,11 = 0',
'J5,12 = 0',
'J5,13 = 0',
'J5,14 = 0',
#
'J6,10 = 0',
'J6,11 = 0',
#'J6,12 = 0',
'J6,13 = 0',
'J6,14 = 0',
#
'J7,10 = 0',
'J7,11 = 0',
'J7,12 = 0',
'J7,13 = 0',
'J7,14 = 0',
#
'J8,10 = 0',
'J8,11 = 0',
'J8,12 = 0',
'J8,13 = 0',
'J8,14 = 0',
#
'J9,10 = 0',
'J9,11 = 0',
'J9,12 = 0',
'J9,13 = 0',
#'J9,14 = 0',
######
# 'out1'
'w1 = 3860.4',#1930.2',
'w7 = 12627.8',#6313.9',
'J1,7 = 0',
# 'x'
'w3 = 0',
'w13 = 0',
'J3,13 = 0',
# 'y'
'w4 = 0',
'w8 = 0',
'J4,8 = 0',
# 'out2'
'w6 = 3860.4',#1930.2',
'w12 = 12627.8',#6313.9',
'J6,12 = 0',
# 'z'
'w9 = 0',
'w14 = 0',
'J9,14 = 0']

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
