# Lump Quantum Annealer Encoding from Quantum Gate Circuit
```
-----------------------------------------------------------------------------------------------------
GENERAL NOTES
-----------------------------------------------------------------------------------------------------
 
 - Set PYTHONPATH to Lump-Annealer-Encoding-From-Gate-Circuit/logical directory or
   Lump-Annealer-Encoding-From-Gate-Circuit/blochsphere directory to run corresponding examples
   
   e.g., ~/path/to/Lump-Annealer-Encoding-From-Gate-Circuit/logical$ export PYTHONPATH=$(pwd)

-----------------------------------------------------------------------------------------------------
CONTENTS
-----------------------------------------------------------------------------------------------------

   I) Gate circuit-to-lump annealer embedding by way of intermediate logical truth table 
      representation
   	  - Covers implementation through an example of an XNOR function
	  - TODO list
	
   II) Bloch sphere truth table representation of qubit
   	  - Notes and ideas on this approach
	  	- General Notes
		- Annealer Encodings for single gates using Bloch sphere
		  truth table representation of qubit
	  - TODO list for implementation of this approach
	  
   III) Lump annealer embedding as composite of single gate annealer embeddings 
   	  - Notes and ideas on this approach
	  - TODO list for implementation of this approach

-----------------------------------------------------------------------------------------------------
(I) GATE CIRCUIT-TO-ANNEALER EMBEDDING BY WAY OF INTERMEDIATE LOGICAL TRUTH TABLE REPRESENTATION
-----------------------------------------------------------------------------------------------------

This approach will be unable to scale to any practical circuit, as practical circuits often 
require upwards of 100 qubits. Clearly, solving a system of 2**100 inequalities is infeasible.
However, the classes and functions used to implement this approach are useful in the later parts
of this project, discussed in sections II and III.

The following describes how this approach generates a lump annealer embedding from a multi-gate 
circuit through an example of the XNOR function. 

File locations are described assuming the base directory is 
~/path/to/Lump-Annealer-Encoding-From-Gate-Circuit/logical/

1) Truthtable initialized in QuantumCircuit class based on the lengths of its QuantumRegisters. 
   Added to quantum circuit in converter/qiskit/_quantumcircuit.py. truthtable class implemented 
   in converter/qiskit/get_annealer_encoding.py

	from converter.qiskit import QuantumCircuit 
        from converter.qiskit import ClassicalRegister, QuantumRegister, 
	from converter.qiskit import execute

	qr0 = QuantumRegister(1)
	qr1 = QuantumRegister(1)
	cr0 = ClassicalRegister(1)
	cr1 = ClassicalRegister(1)
	
	qc = QuantumCircuit(qr0,qr1,cr0,cr1) ----.
	   .-------------------------------------'				  
	   |					 
	   '-->	In this case, when QuantumCircuit is called its truthtable
		attribute is initialized as follows:
			qc.truthtable.numinputs = 4 (2 for qr0 and 2 for qr1)			
			qc.truthtable.inputnames = ['q1_0','q0_0','q1_0_out','q0_0_out']
			qc.truthtable.inputtypes = ['Circ_Input','Circ_Input','Circ_Output','Circ_Output']
			qc.truthtable.outputs = numpy vector of length (2 ** truthtable.numinputs) 
						It is initialized with 1's in positions where input bits are
						equal to output bits in the graycode. The left half columns 
						are input bits and the right half columns are output bits.
			qc.truthtable.graycode = Gray code as a numpy array with (2 ** truthtable.numinputs) 
						rows and (truthtable.numinputs) columns. This is used in 
						routines that modify truthtable.output such as gate 
						functions and truthtable reduction. However, it is 
						inefficient and will be eliminated once better gate and 
						reduction routines are implemented

                                                                                           
                       'q0_0', 'Circ_Input' <-----.         .------> 'q1_0_out', 'Circ_Output'
                                                   \       /                                          
                       'q1_0', 'Circ_Input' <----.  \     /  .-----> 'q0_0_out', 'Circ_Output'
                                                  \  \   /  /
				               [[ 0  0  0  0 ]    1 
	        				[ 0  0  0  1 ]    0
					        [ 0  0  1  0 ]    0
			 		        [ 0  0  1  1 ]    0
                                                [ 0  1  0  0 ]    0
                                                [ 0  1  0  1 ]    1
 	truthtable.graycode as initialized -->  [ 0  1  1  0 ]    0  <-- values of truthtable.outputs  
						[ 0  1  1  1 ]    0      corresponding to gray code rows
                                                [ 1  0  0  0 ]    0
    					        [ 1  0  0  1 ]    0
						[ 1  0  1  0 ]    1
 				                [ 1  0  1  1 ]    0
                                                [ 1  1  0  0 ]    0 
						[ 1  1  0  1 ]    0
                                                [ 1  1  1  0 ]    0
						[ 1  1  1  1 ]]   1


2) Gate operations modify values truthtable.output. They are currently implemented in 
   converter/qiskit/extension/standard/x.py, cx.py. ccx.py, etc. but in the future, these scripts will just 
   serve to append the instruction to a list (specifically, QuantumCircuit.data) so that they can be carried 
   out after the truthtable is reduced.
	
        from converter.qiskit import QuantumCircuit
        from converter.qiskit import ClassicalRegister, QuantumRegister,
        from converter.qiskit import execute

	qr0 = QuantumRegister(1)
        qr1 = QuantumRegister(1)
        cr0 = ClassicalRegister(1)
        cr1 = ClassicalRegister(1)

        qc = QuantumCircuit(qr0,qr1,cr0,cr1)  
     
        qc.cx(qr0[0],qr1[0])--,
     .--qc.x(qr1[0])          |
     |        .---------------'                                    .----------> Target bit 'q1_0_out'
     |        '---> Before cx:                       After cx:    /  .--------> Control bit 'q0_0_out'
     |                                                           /  /
     |                 [[ 0  0  0  0 ]    1            [[ 0  0  0  0 ]    1
     |                  [ 0  0  0  1 ]    0             [ 0  0  0  1 ]    0    Positions of 1's in  
     |                  [ 0  0  1  0 ]    0             [ 0  0  1  0 ]    0    truthtable.output are changed
     |                  [ 0  0  1  1 ]    0             [ 0  0  1  1 ]    0    in positions where the 
     |                  [ 0  1  0  0 ]    0             [ 0  1  0  0 ]    0    control bit ('q0_0_out')
     |                  [ 0  1  0  1 ]    1 <---.       [ 0  1  0  1 ]    0    is one. They are moved to
     |                  [ 0  1  1  0 ]    0      \      [ 0  1  1  0 ]    0    positions where rows of
     |                  [ 0  1  1  1 ]    0       '---> [ 0  1  1  1 ]    1    truthtable.graycode are
     |                  [ 1  0  0  0 ]    0             [ 1  0  0  0 ]    0    identical in all bits except
     |                  [ 1  0  0  1 ]    0             [ 1  0  0  1 ]    0    the target bit ('q1_0_out').
     |                  [ 1  0  1  0 ]    1             [ 1  0  1  0 ]    1
     |                  [ 1  0  1  1 ]    0             [ 1  0  1  1 ]    0     
     |                  [ 1  1  0  0 ]    0             [ 1  1  0  0 ]    0     
     |                  [ 1  1  0  1 ]    0       .---> [ 1  1  0  1 ]    1
     |                  [ 1  1  1  0 ]    0      /      [ 1  1  1  0 ]    0
     |                  [ 1  1  1  1 ]]   1 <---'       [ 1  1  1  1 ]]   0
     |
     |
     '------------> Before x:                       After x:      ,-----------> Target bit 'q1_0_out'
                                                                 /  
                       [[ 0  0  0  0 ]    1 <---,      [[ 0  0  0  0 ]    0
                        [ 0  0  0  1 ]    0      \      [ 0  0  0  1 ]    0    Positions of 1's in  
                        [ 0  0  1  0 ]    0       '---> [ 0  0  1  0 ]    1    truthtable.output are changed
                        [ 0  0  1  1 ]    0             [ 0  0  1  1 ]    0    to positions where the 
                        [ 0  1  0  0 ]    0             [ 0  1  0  0 ]    0    rows of truthtable.graycode
                        [ 0  1  0  1 ]    0       ,---> [ 0  1  0  1 ]    1    identical except for 
                        [ 0  1  1  0 ]    0      /      [ 0  1  1  0 ]    0    the target bit ('q1_0_out').
                        [ 0  1  1  1 ]    1 <---'       [ 0  1  1  1 ]    0     
                        [ 1  0  0  0 ]    0       ,---> [ 1  0  0  0 ]    1    
                        [ 1  0  0  1 ]    0      /      [ 1  0  0  1 ]    0    Similar routines are
                        [ 1  0  1  0 ]    1 <---'       [ 1  0  1  0 ]    0    implemented for other gates
                        [ 1  0  1  1 ]    0             [ 1  0  1  1 ]    0    
                        [ 1  1  0  0 ]    0             [ 1  1  0  0 ]    0     
                        [ 1  1  0  1 ]    1 <---,       [ 1  1  0  1 ]    0
                        [ 1  1  1  0 ]    0      \      [ 1  1  1  0 ]    0
                        [ 1  1  1  1 ]]   0       '---> [ 1  1  1  1 ]]   1
     
     
3) Calling measure appends the measure instruction to a list (specifically, QuantumCircuit.data) so that it 
   can be known when execute() is called. This is necessary for determining which bits will be considered 
   ancillas and eliminated from the truthtable. ie any bit with type 'Circ_Output' that isn't measured will 
   be recast as type 'Ancilla' when execute is called.

        from converter.qiskit import QuantumCircuit
        from converter.qiskit import ClassicalRegister, QuantumRegister,
        from converter.qiskit import execute

        qr0 = QuantumRegister(1)
        qr1 = QuantumRegister(1)
        cr0 = ClassicalRegister(1)
        cr1 = ClassicalRegister(1)

        qc = QuantumCircuit(qr0,qr1,cr0,cr1)

        qc.cx(qr0[0],qr1[0])
        qc.x(qr1[0])
	
	qc.measure(qr1,cr1)  ---------------->  in converter/qiskit/_measure.py the only
                                                significant thing that happens is: 
                                                    
                                                                  qc.data.append('q1_0_out')

5) execute() is implemented in converter/qiskit/tools/_compiler.py. execute() first recasts bits not 
   measured as ancillas and reduces the truth table accordingly as mentioned above. reduce_truthtable() 
   is implemented as a class method of truthtable in converter/qiskit/get_annealer_encoding.py

        from converter.qiskit import QuantumCircuit
        from converter.qiskit import ClassicalRegister, QuantumRegister,
        from converter.qiskit import execute

        qr0 = QuantumRegister(1)
        qr1 = QuantumRegister(1)
        cr0 = ClassicalRegister(1)
        cr1 = ClassicalRegister(1)

        qc = QuantumCircuit(qr0,qr1,cr0,cr1)

        qc.cx(qr0[0],qr1[0])
        qc.x(qr1[0])
	
        qc.measure(qr1,cr1)

	execute(qc)

    'q0_0',
 'Circ_Input' <--.         .------> 'q1_0_out', 'Circ_Output'
                  \       /
   'q1_0', <----.  \     /   .----> 'q0_0_out', 'Ancilla' <-. 
 'Circ_Input'    \  \   /   /         .---------------------'  
               [[ 0  0  0  0 ]    0   '-> Type change                     .-------> 'q0_0', 'Circ_Input'
                [ 0  0  0  1 ]    0       so it can be                   / .------> 'q1_0', 'Circ_Input'
                [ 0  0  1  0 ]    1       identified in                 / / .-----> 'q1_0_out',
                [ 0  0  1  1 ]    0       reduce_truthtable()          / / /        'Circ_Output'
                [ 0  1  0  0 ]    0                                [[ 0 0 0 ]    0
                [ 0  1  0  1 ]    1                                 [ 0 0 1 ]    1
                [ 0  1  1  0 ]    0                                 [ 0 1 0 ]    1
                [ 0  1  1  1 ]    0                                 [ 0 1 1 ]    0
                [ 1  0  0  0 ]    1 ----- reduce_truthtable() ----> [ 1 0 0 ]    1 
                [ 1  0  0  1 ]    0                                 [ 1 0 1 ]    0
                [ 1  0  1  0 ]    0                                 [ 1 1 0 ]    0
                [ 1  0  1  1 ]    0                                 [ 1 1 1 ]]   1
                [ 1  1  0  0 ]    0
                [ 1  1  0  1 ]    0
                [ 1  1  1  0 ]    0
                [ 1  1  1  1 ]]   1

	If the ancilla bit to be removed is not in the least significant position elements of 
	truthtable.inputnames, truthtable.inputtypes, and truthtable.outputs are adjusted until it is. 
	Then, the reduced output is constructed from the old output.

6) Next in execute(), a system of inequalities in terms of annealer qubit and coupler weights are generated 
   from the truthtable

	         [[ 0 0 0 ]    0           system_inequalities = ['0 > G',
                  [ 0 0 1 ]    1                                  'w0 = G',
                  [ 0 1 0 ]    1                                  'w1 = G',
                  [ 0 1 1 ]    0                                  'w0 + w1 > G',
                  [ 1 0 0 ]    1                                  'w2 = G',
                  [ 1 0 1 ]    0                                  'w1 + w2 + J12 > G',
                  [ 1 1 0 ]    0                                  'w1 + w2 + J12 > G',
                  [ 1 1 1 ]]   1                                  'w0 + w1 + w2 + J01 + J02 + J12 = G'] 

    The system of inequalities is generated as a list of strings by the get_ineq_from_truthtable() function
    in converter/qiskit/get_annealer_encoding.py 

7) This list of inequalities is then passed to the solver. The solver works by extracting symbols and their 
   constraints from the equations, and iterating over the constraints to tighten the bounds of the 
   symbols. When bounds converge, a value is picked for the symbol having a constraint composed of the 
   least amount of unknown symbols and the tightest bounds. After a value is picked, the constraints of 
   all symbols are iterated over again and their bounds are tightened further. This is repeated until all 
   symbols have values.

   If a valid solution cannot be found, as in the case of the 3-bit XNOR truthtable above, an ancilla is 
   added. All 1's in the output are placed on ancilla 0's except for the last 1 in the output which is 
   placed on an ancilla 1. If the system still cannot be solved another ancilla is added, this time all 
   1's in the output are placed on ancilla 0's except for the second-to-last output 1 which is placed on 
   an ancilla 1. This can be continued until all output ones are on rows corresponding to 1's of different 
   ancillas.

   This works well for smaller systems of inequalities or simpler large systems of inequalities but does not 
   work on larger, more complicated systems yet. The solver still needs alot of work.
   
   Once the system is solved, qubit and coupler weights are reported:
		
		Annealer Encoding:
			J02 	 -364.5
			w0 	 831.3
			J23 	 141.8
			w3 	 -43.3
			w1 	 -43.3	
			G 	 -43.3
			J01 	 -517.9
			J12 	 120.3
			J03 	 -426.6
			J13 	 302.2
			w2 	 -43.3

		Check:
			True 	-	 0 > G
			True 	-	 w0 > G
			True 	-	 w1 = G
			True 	-	 w1 + J01 + w0 > G
			True 	-	 w2 = G
			True 	-	 w2 + J02 + w0 > G
			True 	-	 w2 + J12 + w1 > G
			True 	-	 w2 + J12 + J02 + w1 + J01 + w0 > G
			True 	-	 w3 = G
			True 	-	 w3 + J03 + w0 > G
			True 	-	 w3 + J13 + w1 > G
			True 	-	 w3 + J13 + J03 + w1 + J01 + w0 > G
			True 	-	 w3 + J23 + w2 > G
			True 	-	 w3 + J23 + J03 + w2 + J02 + w0 > G
			True 	-	 w3 + J23 + J13 + w2 + J12 + w1 > G
			True 	-	 w3 + J23 + J13 + J03 + w2 + J12 + J02 + w1 + J01 + w0 = G

		Ancillas added: 1

   Solver functions and classes are implemented in converter/qiskit/solve_sys_multivar_ineq.py

8) *Not yet implemented* After this general embedding is found, it will be adjusted to correspond to 
   actual Dwave connectivity 
 
9) *Not yet implemented* Last, a script which runs the found embedding on an annealer will be written by 
   execute().
   
TODO:
1) Get solver into a place where it can determine in one shot if system is solvable or not (hopefully in 
   correct implementation, disjoint bounds will be the indicator of an unsolvable system)

2) Truthtable attribute of QuantumCircuit class gets too massive for even moderately sized circuits
	- Find out how to do gate operations and truthtable reduction on output column without the crutch 
	  of the gray code
		- Investigate how fourier transform of output column changes under gate operations
	- Look into perrforming truthtable reduction before gate operations. As currently implemented,
	  gate operations take a long time on large truthtables
	- Find way to encode output bits position on bloch sphere

3) After system of inequalities are solved, adjust found embedding to represent actual Dwave connectivity 
	  
4) Write script in execute() that creates dwave script with the embedding that was found

5) Implement Fredkin and swap gates.

-----------------------------------------------------------------------------------------------------
(II) BLOCH SPHERE TRUTH TABLE REPRESENTATION OF QUBIT
-----------------------------------------------------------------------------------------------------

Notes:

    File locations are described assuming the base directory is 
    ~/path/to/Lump-Annealer-Encoding-From-Gate-Circuit/blochsphere/
    
    Truth table could be used to represent position of qubit on Bloch sphere instead of representing
    a bits logical value which would allow implementation of Hadamard and phase gates. This would 
    result in massive truth tables and as such, the best approach would be to determine annealer 
    embeddings of single gates and from those, find a way to create a lump annealer encoding as a 
    composite of these.
    
   	                   theta bits <---,-,     ,-,---> phi bits  
   	                                   \ \   / / 
   	theta = 0,      phi = 0          [[ 0 0 0 0 ]    1 <------ output vector = 1 to
	theta = 0,      phi = pi/2        [ 0 0 0 1 ]    0 <-,      indicate where a given bit is
	theta = 0,      phi = pi          [ 0 0 1 0 ]    0 <--,         
	theta = 0,	phi = 3*pi/2      [ 0 0 1 1 ]    0 <---,
	theta = pi/2,	phi = 0	          [ 0 1 0 0 ]    0      ,
	theta = pi/2,	phi = pi/2        [ 0 1 0 1 ]    0       ,       ,--------------
	theta = pi/2,	phi = pi          [ 0 1 1 0 ]    0        ,     | These rows don't
	theta = pi/2,	phi = 3*pi/2      [ 0 1 1 1 ]    0         ,    | correspond to 
	theta = pi,	phi = 0	          [ 1 0 0 0 ]    0          :---| anything so   
	theta = pi,	phi = pi/2        [ 1 0 0 1 ]    0 <-------'    | they will always
	theta = pi,	phi = pi          [ 1 0 1 0 ]    0 <------'     | be 0.         
	theta = pi,	phi = 3*pi/2      [ 1 0 1 1 ]    0 <-----'      | I guess that means 
	theta = 3*pi/2,	phi = 0	          [ 1 1 0 0 ]    0 <----'       | the truth table  
	theta = 3*pi/2,	phi = pi/2        [ 1 1 0 1 ]    0 <---'        | can be reduced to  
        theta = 3*pi/2, phi = pi          [ 1 1 1 0 ]    0 <--'         | 3 bits.      
	theta =	3*pi/2, phi = 3*pi/2      [ 1 1 1 1 ]]   0 <-'           '--------------
		                                                        
    Rows in truth table represent discrete points on the Bloch sphere and 
    the output vector indicates the position of a qubit
    
    The phi bits go from 0=2*pi (where all phi bits are 0) 
    to 2*pi-2*pi/(2**num_of_phi_bits) (where all phi bits are 1)
    Not having the row where all phi bits are 1 equal to 2*pi allows
    for there to be discrete points at phi = 0, pi and pi/2.
   
    Right now, I'm thinking the theta bits should represent the same discretization
    as phi. That is, theta is in the interval (0=2*pi, 2*pi/(2**num_of_theta_bits)).
    The reason is: Even though any position on the bloch sphere can be described
    by theta on the continous interval (0, pi), if theta is descritized by 
    a power of two, there will be nothing corresponding to the point
    theta = pi/2. 

    The size of the truth table can expand as finer resolution is needed.
    									
                                                    z
                                                    .
                                                   /|\ theta = [0 0]
                                                    |  phi   = [0 0]    
                                             ,,,-'''|'''-,,,            __,
                                         ,,''       |       '',,        ,'|
                                     ,,''           |           '',,  ,'
                                  ,''               |               '',
                                ,'                  |             ,'   ',
                               '                    |           ,'       '
                              /                     |         ,' <--------\------ theta = [0 1] 
                             ,                  ,,,,|----''';'''-.,        ,      phi =   [1 0] 
                            ,         ,,,,-'''''    |     ,'       ''.,     ,
                            ,    ..'''              |   ,'             '.,  ,
                      ,    , ,,''                   | ,'                  ', ,   ,
                    ,'_____,'_______________________|'______________________',____', y
                     ',    ,,                     ,'|                       ,,   ,'
             theta = [0 1]  ,'-                 ,'  |                   ,,'',  theta = [0 1] 
             phi   = [1 1]  ,  '.             ,'    |              ,,,''    ,  phi   = [0 1]  
                             ,   '',,       ,'      |    ,,,,,-''''         ,
                              \      ''-,,,;,,,,----|''''                  /
           theta = [0 1] ------',-----> ,'          |                    ,'
           phi   = [0 0]         ',   ,'            |                  ,'
                                   ','              |               ,,'
                                  ,' '',,           |           ,,''
                                ,'       '',,       |       ,,''
                             |,'             '''-,,,|,,,-'''
                             '--                    |
                            x                      \|/ theta = [1 0]
                                                    '  phi   = [0 0] 
    
    Annealer embeddings for single gates using crude 4-bit bloch sphere truth table representation 
    of qubit:
    
	Hadamard: 
	
		Hadamard gate is very inelegantly implemented in
		converter/qiskit/extensions/standard/h.py for the 4-bit Bloch sphere qubit
		representation shown above. I will change this once a better way to represent 
		a qubit is implemented.
		
		Right now it just changes the truthtable.outputs vector by mapping 
		a 1 on a given row to a different row as follows:
		        
	            'Circ_Input' 'Circ_Output'       'Circ_Input' 'Circ_Output'
			'q0_0'	  'q0_0_out'             'q0_0'    'q0_0_out'
                     t1 t0 p1 p0 t1 t0 p1 p0    H     t1 t0 p1 p0 t1 t0 p1 p0
                         	 0  0  0  0   ====>                0  1  0  0  
                       		 0  1  0  0   ====>                0  0  0  0        
                                 0  1  0  1   ====>                0  1  1  1                               
                                 0  1  1  0   ====>                1  0  0  0                               
                                 0  1  1  1   ====>                0  1  0  1                              
                                 1  0  0  0   ====>                0  1  1  0 
			
			
		 	Input columns are blank because they can be anything and 
			the Hadamard operation does not affect them.
                                                                                               
		Running examples/Hadamard.py returns coupler and qubit weights for an annealer 
		Hadamard gate using a 4-bit discretization of the bloch sphere (assuming full 
		connectivity): 		
		
			J67 	 -47.3                                          
			J16 	 115.0			                
			w7 	 546.6                                                      
			J01 	 -246.7                                                           
			J25 	 342.3			                                           
			J02 	 -108.4
			w0 	 320.2
			J26 	 978.9
			J12 	 96.9
			J56 	 -514.3                 
			J36 	 -201.9
			J06 	 53.6
			J34 	 667.0
			J24 	 -499.6
			J35 	 -821.9
			w2 	 -747.1		        
			w3 	 627.7
			J17 	 -564.1
			w1 	 38.1	      
			J07 	 880.6
			J03 	 938.0
			w5 	 910.4
			J57 	 837.0
			w6 	 -747.1
			J14 	 -240.1
			w4 	 984.6
			J04 	 -48.2
			J05 	 -595.6
			J45 	 -379.6
			G 	 -747.1
			J47 	 708.5
			J15 	 547.5
			J46 	 -697.2
			J37 	 -312.2
			J13 	 651.5
			J27 	 -117.5
			J23 	 -548.1
			
		The above embedding is setup to run on a Dwave simulator in 
		examples/Hadamard_dwave.py
 	   					
	Z:
	
	Y:
	
	X:
	
	Controlled-X:
	
	Toffoli:
	
	Swap:
	
	Fredkin:

    Need 6 bit truth table representation of single qubit to do T gate
    
    	

TODO:

    1) Change reduce_truthtable() of truthtable class in
       blochsphere/converter/qiskit/get_annealer_encoding.py to work with Bloch sphere truthtable
    2) Think about how add_ancilla() of truthtable class in
       blochsphere/converter/qiskit/get_annealer_encoding.py needs to change if at all and change
       it if it does
    3) Implement gate operations for bloch sphere truth table representation of qubit

-----------------------------------------------------------------------------------------------------
(III) LUMP ANNEALER EMBEDDING AS COMPOSITE OF SINGLE GATE ANNEALER EMBEDDINGS
-----------------------------------------------------------------------------------------------------

Notes:

   If possible, it would probably be much more efficient to algorithmically determine a lump 
   adiabatic embedding of a circuit from its component single gate embeddings than to determine
   a lump adiabatic from a truth table as described above.
   
   	Consider a logical XOR and a NOT embedding (assuming full connectivity) 
	and try to compose a logical XNOR embedding from these
	
       		     XOR gate embedding                         NOT gate encoding
                    -------------------                       -------------------
               
        Ancilla          J01 = 844.4	     Output                  Input
      w0 = 433.3 O------------------------O w1 = 112.8           O w4 = -729.9 
                 |'.    J03 =           .'|                      |
		 |  ''. -767.5       .''  |                      |
		 |     ''.        .''     |                      |
		 |        ''.  .''        |                      | 
     J02 =-471.2 |          .''.          | J13 = -606           | J45 = 823.7
		 |       .''    ''.       |                      |
		 |    .''J12 =     ''.    |                      |
		 |,.''  -185.2        ''.,|                      |
       w2 = 72.4 O------------------------O w3 = 493.2           O w5 = -729.9
         Input		 J23 = 239.8         Input                   Output                      
		                                           
		      Ground state = 0                       Ground state = -729.9
		 
		 
                                      XNOR gate embedding ?
				     ---------------------- 
                  ,-----------------------------------------------------------,
                 |                         JO4 = ?                             ',
                 |  ,------------------------------------------,                 ',
        Ancilla  |.'       J01 = 844.4        Ancilla           '.     Ancilla     ',
      w0 = 433.3 O------------------------O, w1 = 112.8     ,----,O, w4 = -729.9     ',
                 |'.    J03 =           .'|\',            ,'   ,' | '.                |
                 |  ''. -767.5       .''  | \ '----------'    /   |   ',              | J05 = ?
                 |     ''.        .''     |  \  J14 = ?      /    |     '-------,     |
                 |        ''.  .''        |   ',  J15 = ?   /     |              ',,,''
     J02 =-471.2 |          .''.          | J13 '----------/-,    | J45 = 823.7,,'|
                 |       .''    ''.       | = -606        /   \   |        ,,''   | 
                 |    .''J12 =     ''.    |   ,----------'     \  |    ,,''       |
                 |,.''  -185.2        ''.,| ,'    J34 = ?       \ |,,''           | J24 = ?
       w2 = 72.4 O------------------------O' w3 = 493.2           O w5 = -729.9   |
         Input ,'|       J23 = 239.8      |   Input             ,' ',   Output    |               
             ,'  |                        '--------------------'     ',           |
           ,'    |                                J35 = ?              '----------|---,
	   |     |                        J25 = ?                                ,'   | J25 = ? 
           |	  '-------------------------------------------------------------'     |
            '-------------------------------------------------------------------------'
                                       Ground state = ?
	
	Solving the system of inequalities corresponding to an XNOR with three ancilla bits 
	(2 intermediate inputs/outputs recast as ancillas + the 1 XOR ancilla that was already
	there) for the unknown ground state and coupler weights between the 2 subembeddings 
	(using the values for variables from XOR and NOT embeddings) is not possible as the values
	of known variables immediately pose contradicting constraints on the ground state:
	
	False 	- 0 > G
	False 	- 433.3 > G
	False 	- 112.8 > G
	False 	- 112.8 + 844.4 + 433.3 > G
	True 	- 72.4 = G
	False 	- 72.4 + -471.2 + 433.3 > G
	False 	- 72.4 + -185.2 + 112.8 > G
	False 	- 72.4 + -185.2 + -471.2 + 112.8 + 844.4 + 433.3 > G
	False 	- 493.2 > G
	True 	- 493.2 + -767.5 + 433.3 = G
	False 	- 493.2 + -606 + 112.8 > G
	False 	- 493.2 + -606 + -767.5 + 112.8 + 844.4 + 433.3 > G
	False 	- 493.2 + 239.8 + 72.4 > G
	False 	- 493.2 + 239.8 + -767.5 + 72.4 + -471.2 + 433.3 > G
	False 	- 493.2 + 239.8 + -606 + 72.4 + -185.2 + 112.8 > G
	False 	- 493.2 + 239.8 + -606 + -767.5 + 72.4 + -185.2 + -471.2 + 112.8 + 844.4 + 433.3 > G
	False 	- -729.9 > G
	True 	- -729.9 + J04 + 433.3 > G
	True 	- -729.9 + J14 + 112.8 > G
	True 	- -729.9 + J14 + J04 + 112.8 + 844.4 + 433.3 > G
	False 	- -729.9 + J24 + 72.4 > G
	True 	- -729.9 + J24 + J04 + 72.4 + -471.2 + 433.3 > G
	True 	- -729.9 + J24 + J14 + 72.4 + -185.2 + 112.8 > G
	True 	- -729.9 + J24 + J14 + J04 + 72.4 + -185.2 + -471.2 + 112.8 + 844.4 + 433.3 > G
	False 	- -729.9 + J34 + 493.2 > G
	True 	- -729.9 + J34 + J04 + 493.2 + -767.5 + 433.3 > G
	True 	- -729.9 + J34 + J14 + 493.2 + -606 + 112.8 > G
	True 	- -729.9 + J34 + J14 + J04 + 493.2 + -606 + -767.5 + 112.8 + 844.4 + 433.3 > G
	False 	- -729.9 + J34 + J24 + 493.2 + 239.8 + 72.4 > G
	True 	- -729.9 + J34 + J24 + J04 + 493.2 + 239.8 + -767.5 + 72.4 + -471.2 + 433.3 > G
	True 	- -729.9 + J34 + J24 + J14 + 493.2 + 239.8 + -606 + 72.4 + -185.2 + 112.8 > G
        .... etc. ....
        .... etc. ....
		
	This indicates the fact (which probably should have been obvious to me) that two arbitrary
	embeddings representing logic functions cannot be trivially combined into one encoding 
	representing a composite function.
	
	--> try and add a coupling qubit inbetween the circuits
		doesn't seem to work
	--> try using global offset in the inequalities
		doesn't seem to work
		
	System of inequalities for 6 and 7 qubit XNOR that use values of variables in XOR
	and NOT embeddings above are setup to run in the main() block of
	composite/solve_sys_multivar_ineq.py.
	This file can be run with the appropriate system of inequalities uncommented 
	to see if unknown coupler and qubit weights, ground state, and global offset can be
	solved for. 
	There is a line which adds the global offset variable to all inequalities that can be
	commented or uncommented depending on whether or not you want to include the global
	offset variable.
	The best embedding found is run on a Dwave simulator after solving is complete. This
	is to validate that the embedding works if/when one is found.
		
  Comparison of 4-bit XOR and 4-bit XNOR embeddings:
  
  	Maybe by staring at the XOR and XNOR embeddings, the properties of the NOT 
	embedding which contribute to transforming an XOR into an XNOR encoding
	will become apparent:
	
  	       	     XOR gate embedding                         NOT gate encoding
                    -------------------                       -------------------
               
        Ancilla          J01 = 844.4	     Output                  Input
      w0 = 433.3 O------------------------O w1 = 112.8           O w4 = -729.9 
                 |'.    J03 =           .'|                      |
		 |  ''. -767.5       .''  |                      |
		 |     ''.        .''     |                      |
		 |        ''.  .''        |                      | 
     J02 =-471.2 |          .''.          | J13 = -606           | J45 = 823.7
		 |       .''    ''.       |                      |
		 |    .''J12 =     ''.    |                      |
		 |,.''  -185.2        ''.,|                      |
       w2 = 72.4 O------------------------O w3 = 493.2           O w5 = -729.9
         Input		 J23 = 239.8         Input                   Output                      
		                                           
		      Ground state = 0                       Ground state = -729.9
		      

       	                          4-bit XNOR gate embedding                
		                 --------------------------                       
               
                        Ancilla          J01 = -517.9        Output                  
                      w0 = 831.3 O------------------------O w1 = -43.3           
                                 |'.    J03 =           .'|                       
		                 |  ''. -426.6       .''  |                      
                                 |     ''.        .''     |                      
                         	 |        ''.  .''        |                       
                     J02 =-364.5 |          .''.          | J13 = 302.2          
                                 |       .''    ''.       |                      
                         	 |    .''J12 =     ''.    |                      
                         	 |,.''   120.3        ''.,|                      
                      w2 = -43.3 O------------------------O w3 = -43.3           
                         Input	        J23 = 141.8          Input
		                                           
		                     Ground state = -43.3                       

TODO:

    1) Figure out how to do this
    2) Figure out scheme to simplify annealer embedding graphs

```
