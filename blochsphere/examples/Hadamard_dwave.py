import dimod

values =  [['J67', -47.3],
           ['J16', 115.0],					              
           ['w7',  546.6],                                                    
           ['J01', -246.7],                                                        
           ['J25', 342.3],			                                            
           ['J02', -108.4],
           ['w0', 320.2],
           ['J26', 978.9],
           ['J12', 96.9],
           ['J56', -514.3],			  			         
           ['J36', -201.9],
           ['J06', 53.6],
           ['J34', 667.0],
           ['J24', -499.6],
           ['J35', -821.9],
           ['w2', -747.1],		  				  
           ['w3', 627.7],
           ['J17', -564.1],
           ['w1', 38.1],			    
           ['J07', 880.6],
           ['J03', 938.0],
           ['w5', 910.4],
           ['J57', 837.0],
           ['w6', -747.1],
           ['J14', -240.1],
           ['w4', 984.6],
           ['J04', -48.2],
           ['J05', -595.6],
           ['J45', -379.6],
           ['J47', 708.5],
           ['J15', 547.5],
           ['J46', -697.2],
           ['J37', -312.2],
           ['J13', 651.5],
           ['J27', -117.5],
           ['J23', -548.1]]

#ground state supposed to be -747.1

qubit = list()
qubitwght = list()
coupler = list()
couplerwght = list()

for i in range(len(values)):
    if 'J' in values[i][0]:
        numbers = values[i][0][1:]
        coupler.append(('w{}'.format(numbers[0]),'w{}'.format(numbers[1])))
        couplerwght.append(values[i][1])
    if 'w' in values[i][0]:
        qubit.append(values[i][0])
        qubitwght.append(values[i][1])

qubit_weights = {q:w for q,w in zip(qubit, qubitwght)}
coupler_weights = {c:w for c,w in zip(coupler,couplerwght)}

offset = 0

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
        print(sample, sample, sample, energy)
print('\n')
