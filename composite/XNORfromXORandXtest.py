import dimod
import numpy as np


'''
                       Make XNOR encoding from the XOR and NOT encodings below
                      ---------------------------------------------------------

       		     XOR gate encoding                         NOT gate encoding
                    -------------------                       -------------------
               
        Ancilla          J01 = 844.4	     Output                  Input
      w0 = 433.3 O------------------------O w1 = 112.8           O w4 = -729.9 
                 | \    J03 =           / |                      |
		 |    \ -767.5       /    |                      |
		 |       \        /       |                      |
		 |          \  /          |                      | 
     J02 =-471.2 |          /  \          | J13 = -606           | J45 = 823.7
		 |       /        \       |                      |
		 |    / J12 =        \    |                      |
		 | /    -185.2          \ |                      |
       w2 = 72.4 O------------------------O w3 = 493.2           O w5 = -729.9
         Input		 J23 = 239.8         Input                   Output                      
		                                           
		      Ground state = 0                       Ground state = -729.9


                          XOR   

                        0 0 0 0|1
                        0 0 0 1|0
                        0 0 1 0|0
                        0 0 1 1|0
                        0 1 0 0|0
                        0 1 0 1|0
                        0 1 1 0|1
                        0 1 1 1|0
                        1 0 0 0|0
                        1 0 0 1|0
                        1 0 1 0|1
                        1 0 1 1|0
                        1 1 0 0|0
                        1 1 0 1|1
                        1 1 1 0|0
                        1 1 1 1|0
'''




qubit_weights = {'w0' : 433.3,
                 'w1' : 112.8,    
                 'w2' : 72.4,
                 'w3' : 493.2,
                 'w4' : -729.9,
                 'w5' : -729.9}

coupler_weights = {('w0','w1') : 844.4,
                   ('w0','w2') : -471.2,
                   ('w0','w3') : -767.5,
                   ('w1','w2') : -185.2,
                   ('w1','w3') : -606,
                   ('w2','w3') : 239.8,
                   ('w4','w5') : 823.7,
                   ('w1','w4') : 1}


bqm = dimod.BinaryQuadraticModel(qubit_weights, coupler_weights, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

groundstate = 1000000
for sample, energy in response.data(['sample','energy']):
    if energy<groundstate:
        groundstate = energy


for sample, energy in response.data(['sample', 'energy']):
    if energy == groundstate:
        print(sample['w2'], sample['w3'], sample['w5'], energy)

