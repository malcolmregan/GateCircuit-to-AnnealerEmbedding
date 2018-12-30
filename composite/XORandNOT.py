import numpy as np
from random  import randint, uniform, shuffle
from solve_sys_multivar_ineq import *
    
# Combine XOR and NOT into XNOR. XOR qubits as above, NOT output = q4, NOT input = q5
# split q4 and q5 ...
system_inequalities = ['0 > G', 
                       'w0 > G', 
                       'w1 > G', 
                       'w1 + J01 + w0 > G', 
                       'w2 > G', 
                       'w2 + J02 + w0 > G', 
                       'w2 + J12 + w1 > G', 
                       'w2 + J12 + J02 + w1 + J01 + w0 > G', 
                       'w3 > G', 
                       'w3 + J03 + w0 > G', 
                       'w3 + J13 + w1 > G', 
                       'w3 + J13 + J03 + w1 + J01 + w0 > G', 
                       'w3 + J23 + w2 > G', 
                       'w3 + J23 + J03 + w2 + J02 + w0 > G', 
                       'w3 + J23 + J13 + w2 + J12 + w1 > G', 
                       'w3 + J23 + J13 + J03 + w2 + J12 + J02 + w1 + J01 + w0 > G', 
                       'w4 > G', 
                       'w4 + J04 + w0 > G', 
                       'w4 + J14 + w1 > G', 
                       'w4 + J14 + J04 + w1 + J01 + w0 > G', 
                       'w4 + J24 + w2 > G', 
                       'w4 + J24 + J04 + w2 + J02 + w0 > G', 
                       'w4 + J24 + J14 + w2 + J12 + w1 = G', 
                       'w4 + J24 + J14 + J04 + w2 + J12 + J02 + w1 + J01 + w0 > G', 
                       'w4 + J34 + w3 > G', 
                       'w4 + J34 + J04 + w3 + J03 + w0 > G', 
                       'w4 + J34 + J14 + w3 + J13 + w1 = G', 
                       'w4 + J34 + J14 + J04 + w3 + J13 + J03 + w1 + J01 + w0 > G', 
                       'w4 + J34 + J24 + w3 + J23 + w2 > G', 
                       'w4 + J34 + J24 + J04 + w3 + J23 + J03 + w2 + J02 + w0 > G', 
                       'w4 + J34 + J24 + J14 + w3 + J23 + J13 + w2 + J12 + w1 > G', 
                       'w4 + J34 + J24 + J14 + J04 + w3 + J23 + J13 + J03 + w2 + J12 + J02 + w1 + J01 + w0 > G', 
                       'w5 = G', 
                       'w5 + J05 + w0 > G', 'w5 + J15 + w1 > G', 
                       'w5 + J15 + J05 + w1 + J01 + w0 > G', 'w5 + J25 + w2 > G', 
                       'w5 + J25 + J05 + w2 + J02 + w0 > G', 
                       'w5 + J25 + J15 + w2 + J12 + w1 > G', 
                       'w5 + J25 + J15 + J05 + w2 + J12 + J02 + w1 + J01 + w0 > G', 
                       'w5 + J35 + w3 > G', 
                       'w5 + J35 + J05 + w3 + J03 + w0 > G', 
                       'w5 + J35 + J15 + w3 + J13 + w1 > G', 
                       'w5 + J35 + J15 + J05 + w3 + J13 + J03 + w1 + J01 + w0 > G', 
                       'w5 + J35 + J25 + w3 + J23 + w2 > G',
                       'w5 + J35 + J25 + J05 + w3 + J23 + J03 + w2 + J02 + w0 = G', 
                       'w5 + J35 + J25 + J15 + w3 + J23 + J13 + w2 + J12 + w1 > G', 
                       'w5 + J35 + J25 + J15 + J05 + w3 + J23 + J13 + J03 + w2 + J12 + J02 + w1 + J01 + w0 > G', 
                       'w5 + J45 + w4 > G', 
                       'w5 + J45 + J05 + w4 + J04 + w0 > G', 
                       'w5 + J45 + J15 + w4 + J14 + w1 > G', 
                       'w5 + J45 + J15 + J05 + w4 + J14 + J04 + w1 + J01 + w0 > G', 
                       'w5 + J45 + J25 + w4 + J24 + w2 > G', 
                       'w5 + J45 + J25 + J05 + w4 + J24 + J04 + w2 + J02 + w0 > G', 
                       'w5 + J45 + J25 + J15 + w4 + J24 + J14 + w2 + J12 + w1 > G', 
                       'w5 + J45 + J25 + J15 + J05 + w4 + J24 + J14 + J04 + w2 + J12 + J02 + w1 + J01 + w0 > G', 
                       'w5 + J45 + J35 + w4 + J34 + w3 > G', 
                       'w5 + J45 + J35 + J05 + w4 + J34 + J04 + w3 + J03 + w0 > G', 
                       'w5 + J45 + J35 + J15 + w4 + J34 + J14 + w3 + J13 + w1 > G', 
                       'w5 + J45 + J35 + J15 + J05 + w4 + J34 + J14 + J04 + w3 + J13 + J03 + w1 + J01 + w0 > G', 
                       'w5 + J45 + J35 + J25 + w4 + J34 + J24 + w3 + J23 + w2 > G', 
                       'w5 + J45 + J35 + J25 + J05 + w4 + J34 + J24 + J04 + w3 + J23 + J03 + w2 + J02 + w0 > G', 
                       'w5 + J45 + J35 + J25 + J15 + w4 + J34 + J24 + J14 + w3 + J23 + J13 + w2 + J12 + w1 > G', 
                       'w5 + J45 + J35 + J25 + J15 + J05 + w4 + J34 + J24 + J14 + J04 + w3 + J23 + J13 + J03 + w2 + J12 + J02 + w1 + J01 + w0 > G',
                       # XOR
                       'w0 = 500',
                       'w2 = 50',
                       'w3 = 50',
                       'J01 = 3263.6',
                       'J02 = -300',
                       'J03 = -380',
                       'J12 = -100',
                       'J13 = -100',
                       'J23 = 80',
                       # NOT
                       'w5 = -50',
                       'J45 = 500', 
                       # all cplers btwn XOR and NOT 0
                       'J04 = 0',
                       'J05 = 0',
                       'J15 = 0'#500', # bc q1 and q4 are synched and there is a coupler between q4 and q5, there must also be
                       'J24 = 0',   # one between q1 and q5 
                       'J25 = 0',
                       'J34 = 0',
                       'J35 = 0',
                       #########
                       'w1 = 150',
                       'w4 = 50',
                       'J14 = -100'] 


#            .-----J14-----------.
#           /                     \
# outN    inN     in2X    in1X    outX    anc    
# w5      w4      w3      w2      w1      w0
# 1       0       0       0       0       0                                  
# 0       1       0       1       1       0 
# 0       1       1       0       1       0 
# 1       0       1       1       0       1 

inputs = ['w2','w3']
outputs = ['w5']


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
