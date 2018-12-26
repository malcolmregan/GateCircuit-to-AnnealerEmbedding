import dimod
import numpy as np


'''
                       Make XNOR encoding from the XOR and NOT encodings below
                      ---------------------------------------------------------

       		     XOR gate encoding                NOT gate encoding
                    -------------------              -------------------
                                                                    
        Ancilla            J01 = 844.4	     Output              Input
      w0 = 433.3 O------------------------O, w1 = 112.8    ,O  w4 = -729.9 
                 |'.    J03 =           .'| ',           ,' |   
		 |  ''. -767.5       .''  |   ',       ,'   |       
		 |     ''.        .''     |     ',   ,'     |                 
		 |        ''.  .''        |       'o' w6    |                 
     J02 =-471.2 |          .''.          |      ,' ',      | J45 = 823.7    
		 |       .''    '',       |    ,'     ',    |                 
		 |    .''J12 =     ''.    |   ,'        ',  |                
		 |,.''  -185.2        ''.,| ,'            ',|                        
       w2 = 72.4 O------------------------O' w3 = 493.2     O w5 = -729.9    
         Input	  	 J23 = 239.8         Input              Output                                                                             

		    XOR Ground state = 0             NOT Ground state = -729.9

                                     Composite Ground State = ?
'''

'''
Symbol Values: 
	 J36 	 -729.9
	 J56 	 -729.9
	 J34 	 2223.1
	 offset  729.9
	 w6 	 -1459.8
	 J25 	 6056.5
	 J35 	 729.9
	 J16 	 0
	 J46 	 29.9
	 J26 	 910.0
	 G 	 -1459.8
	 J15 	 0.0
	 J05 	 -1027.3
	 J06 	 1027.3
	 J04 	 1929.8
	 J14 	 1411.3
	 J24 	 -1669.8
128 were true, 0 were false:
'''

qubit_weights = {'w6': -1459.8, 
                 'w0': 433.3, 
                 'w1': 112.8, 
                 'w2': 72.4, 
                 'w3': 493.2, 
                 'w4': -729.2,
                 'w5': -729.9} 

coupler_weights = {('w3', 'w6'): -729.9, 
                   ('w5', 'w6'): -729.9, 
                   ('w3', 'w4'): 2223.1, 
                   ('w2', 'w5'): 6056.5, 
                   ('w3', 'w5'): 729.9, 
                   ('w1', 'w6'): 0, 
                   ('w4', 'w6'): 29.9, 
                   ('w2', 'w6'): 910.0, 
                   ('w1', 'w5'): 0.0, 
                   ('w0', 'w5'): -1027.3, 
                   ('w0', 'w6'): 1027.3, 
                   ('w0', 'w4'): 1929.8, 
                   ('w1', 'w4'): 1411.3, 
                   ('w2', 'w4'): -1669.8, 
                   ('w0', 'w1'): 844.4, 
                   ('w0', 'w2'): -471.2, 
                   ('w0', 'w3'): -767.5, 
                   ('w1', 'w2'): -185.2, 
                   ('w1', 'w3'): -606, 
                   ('w2', 'w3'): 239.8, 
                   ('w4', 'w5'): 823.7}

offset = 729.9

# w6+w4+w2+J24+J26+J46+offset
# w6+w3+w1+J13+J16+J35+offset
print(-1459.8-729.2+72.4-1669.8+910+29.9+729.9,-1459.8)

bqm = dimod.BinaryQuadraticModel(qubit_weights, coupler_weights, offset, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

groundstate = 1000000
for sample, energy in response.data(['sample','energy']):
    if energy<groundstate:
        groundstate = round(energy,1)

function = list()
print('Ground state:')
for sample, energy in response.data(['sample', 'energy']):
    if round(energy,1) == groundstate:
        print(sample['w2'], sample['w3'], sample['w5'], energy)
        function.append([sample['w2'], sample['w3'], sample['w5']])
print('\n')

print('Supposed to be ground state:')
for sample, energy in response.data(['sample', 'energy']):
    if (sample['w6']==1 and sample['w5']==1 and sample['w4']==0 and sample['w3']==0 and sample['w2']==0 and sample['w1']==0 and sample['w0']==0) \
        or (sample['w6']==1 and sample['w5']==0 and sample['w4']==1 and sample['w3']==0 and sample['w2']==1 and sample['w1']==0 and sample['w0']==0) \
        or (sample['w6']==1 and sample['w5']==0 and sample['w4']==0 and sample['w3']==1 and sample['w2']==0 and sample['w1']==1 and sample['w0']==0) \
        or (sample['w6']==1 and sample['w5']==1 and sample['w4']==0 and sample['w3']==1 and sample['w2']==1 and sample['w1']==0 and sample['w0']==1):
        print(sample['w2'], sample['w3'], sample['w5'], energy)
        function.append([sample['w2'], sample['w3'], sample['w5']])
print('\n')



function.sort()
for i in range(len(function)):
    print(function[i])










### NOT check
NOTqubitweights = {'w4': -729.9,
                   'w5': -729.9}
NOTcouplerweights = {('w4', 'w5') : 823.7}

offset = 0
print('\n\nNOT check')
bqm = dimod.BinaryQuadraticModel(NOTqubitweights, NOTcouplerweights, offset, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

groundstate = 1000000
for sample, energy in response.data(['sample','energy']):
    if round(energy,1)<groundstate:
        groundstate = round(energy,1)

function = list()
for sample, energy in response.data(['sample', 'energy']):
    if round(energy,1)==groundstate:
        #print(sample['w2'], sample['w3'], sample['w1'], energy)
        function.append([sample['w4'], sample['w5']])

function.sort()
for i in range(len(function)):
    print(function[i])
print('\n')


### XOR check

XORqubitweights = {'w0' : 433.3,
                   'w1' : 112.8,
                   'w2' : 72.4,
                   'w3' : 493.2}

XORcouplerweights = {('w0','w1') : 844.4,     # J01
                     ('w0','w2') : -471.2,    # J02
                     ('w0','w3') : -767.5,    # J03
                     ('w1','w2') : -185.2,    # J12
                     ('w1','w3') : -606,      # J13
                     ('w2','w3') : 239.8}     # J23

offset = 0

print('XOR check')
bqm = dimod.BinaryQuadraticModel(XORqubitweights, XORcouplerweights, offset, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

groundstate = 1000000
for sample, energy in response.data(['sample','energy']):
    if round(energy,1)<groundstate:
        groundstate = round(energy,1)

function = list()
for sample, energy in response.data(['sample', 'energy']):
    if round(energy,1)==groundstate:
        #print(sample['w2'], sample['w3'], sample['w1'], energy)
        function.append([sample['w2'], sample['w3'], sample['w1']])

function.sort()
for i in range(len(function)):
    print(function[i])



