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
   I) Gate circuit-to-annealer ecnoding by way of intermediate logical truthtable representation 
   	  - Covers implementation through an example of a simple XOR function
	  - TODO list
	
   II) Gate circuit-to-annealer encoding by way of intermediate bloch sphere truthtable 
       representation
   	  - Notes and ideas on this approach
	  - TODO list for implementation of this approach
	  
   III) Lump annealer encoding as composite of serial annealer encodings 
   	  - Notes and ideas on this approach
	  - TODO list for implementation of this approach

-----------------------------------------------------------------------------------------------------
(I) GATE CIRCUIT-TO-ANNEALER ENCODING BY WAY OF INTERMEDIATE LOGICAL TRUTHTABLE REPRESENTATION
-----------------------------------------------------------------------------------------------------
    
The following describes how this approach generate a lump annealer encoding from a gate circuit 
through an example of the XOR function. Note: file locations are described assuming the base
directory is ~/path/to/Lump-Annealer-Encoding-From-Gate-Circuit/logical/

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
	
	qc = QuantumRegister(qr0,qr1,cr0,cr1) ----.
	   .--------------------------------------'				  
	   |					 
	   '-->	In this case, when QuantumRegister is called its truthtable
		attribute is initialized as follows:
			qc.truthtable.numinputs = 4 (2 for input and 2 for output)			
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
                       'q1_0', 'Circ_Input' <----.  \     /   .----> 'q0_0_out', 'Circ_Output'
                                                  \  \   /   /
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

        qc = QuantumRegister(qr0,qr1,cr0,cr1)  

	qc.cx(qr0[0],qr1[0]) 
	    \                                                     .----------> Target bit 'q1_0_out'
             '---> Before cx:                       After cx:    /  .--------> Control bit 'q0_0_out'
                                                                /  /
                      [[ 0  0  0  0 ]    1            [[ 0  0  0  0 ]    1
                       [ 0  0  0  1 ]    0             [ 0  0  0  1 ]    0     Positions of 1's in  
                       [ 0  0  1  0 ]    0             [ 0  0  1  0 ]    0     truthtable.output are changed
                       [ 0  0  1  1 ]    0             [ 0  0  1  1 ]    0     in positions where the 
                       [ 0  1  0  0 ]    0             [ 0  1  0  0 ]    0     control bit ('q0_0_out')
                       [ 0  1  0  1 ]    1 <---.       [ 0  1  0  1 ]    0     is one. They are moved to
                       [ 0  1  1  0 ]    0      \      [ 0  1  1  0 ]    0     positions where rows of
                       [ 0  1  1  1 ]    0       '---> [ 0  1  1  1 ]    1     truthtable.graycode are
                       [ 1  0  0  0 ]    0             [ 1  0  0  0 ]    0     identical in all bits except
                       [ 1  0  0  1 ]    0             [ 1  0  0  1 ]    0     the target bit ('q1_0_out').
                       [ 1  0  1  0 ]    1             [ 1  0  1  0 ]    1
                       [ 1  0  1  1 ]    0             [ 1  0  1  1 ]    0     Similar routines are 
                       [ 1  1  0  0 ]    0             [ 1  1  0  0 ]    0     implemented for other gates.
                       [ 1  1  0  1 ]    0       .---> [ 1  1  0  1 ]    1
                       [ 1  1  1  0 ]    0      /      [ 1  1  1  0 ]    0
                       [ 1  1  1  1 ]]   1 <---'       [ 1  1  1  1 ]]   0


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

        qc = QuantumRegister(qr0,qr1,cr0,cr1)

        qc.cx(qr0[0],qr1[0])
                                                 
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

        qc = QuantumRegister(qr0,qr1,cr0,cr1)

        qc.cx(qr0[0],qr1[0])

        qc.measure(qr1,cr1)

	execute(qc)

    'q0_0',
 'Circ_Input' <--.         .------> 'q1_0_out', 'Circ_Output'
                  \       /
   'q1_0', <----.  \     /   .----> 'q0_0_out', 'Ancilla' <-. 
 'Circ_Input'    \  \   /   /         .---------------------'  
               [[ 0  0  0  0 ]    1   '-> Type change                     .-------> 'q0_0', 'Circ_Input'
                [ 0  0  0  1 ]    0       so it can be                   / .------> 'q1_0', 'Circ_Input'
                [ 0  0  1  0 ]    0       identified in                 / / .-----> 'q1_0_out',
                [ 0  0  1  1 ]    0       reduce_truthtable()          / / /        'Circ_Output'
                [ 0  1  0  0 ]    0                                [[ 0 0 0 ]    1
                [ 0  1  0  1 ]    0                                 [ 0 0 1 ]    0
                [ 0  1  1  0 ]    0                                 [ 0 1 0 ]    0
                [ 0  1  1  1 ]    1                                 [ 0 1 1 ]    1
                [ 1  0  0  0 ]    0 ----- reduce_truthtable() ----> [ 1 0 0 ]    0 
                [ 1  0  0  1 ]    0                                 [ 1 0 1 ]    1
                [ 1  0  1  0 ]    1                                 [ 1 1 0 ]    1
                [ 1  0  1  1 ]    0                                 [ 1 1 1 ]]   0
                [ 1  1  0  0 ]    0
                [ 1  1  0  1 ]    1
                [ 1  1  1  0 ]    0
                [ 1  1  1  1 ]]   0

	If the ancilla bit to be removed is not in the least significant position elements of 
	truthtable.inputnames, truthtable.inputtypes, and truthtable.outputs are adjusted until it is. 
	Then, the reduced output is constructed from the old output.

6) Next in execute(), a system of inequalities in terms of annealer qubit and coupler weights are generated 
   from the truthtable

	         [[ 0 0 0 ]    1           system_inequalities = ['0 = G',
                  [ 0 0 1 ]    0                                  'w0 > G',
                  [ 0 1 0 ]    0                                  'w1 > G',
                  [ 0 1 1 ]    1                                  'wo + w1 = G',
                  [ 1 0 0 ]    0                                  'w2 > G',
                  [ 1 0 1 ]    1                                  'w1 + w2 + J12 = G',
                  [ 1 1 0 ]    1                                  'w1 + w2 + J12 = G',
                  [ 1 1 1 ]]   0                                  'w0 + w1 + w2 + J01 + J02 + J12 > G'] 

    The system of inequalities is generated as a list of strings by the get_ineq_from_truthtable() function
    in converter/qiskit/get_annealer_encoding.py 

7) This list of inequalities is then passed to the solver. The solver works by extracting symbols and their 
   constraints from the equations, and iterating over the constraints to tighten the bounds of the 
   symbols. When bounds converge, a value is picked for the symbol having a constraint composed of the 
   least amount of unknown symbols and the tightest bounds. After a value is picked, the constraints of 
   all symbols are iterated over again and their bounds are tightened further. This is repeated until all 
   symbols have values.

   If a valid solution cannot be found, as in the case of the 3-bit XOR truthtable above, an ancilla is 
   added. All 1's in the output are place on ancilla 0's except for the last 1 in the output which is placed 
   on an ancilla 1. If the system still cannot be solved another ancilla is added, this time all 1's in the 
   output are placed on ancilla 0's except for the second-to-last output 1 which is placed on an ancilla 1. 
   This can be continued until all output ones are on rows corresponding to 1's of different ancillas.

   This works well for smaller systems of inequalities or simpler large systems of inequalities but does not 
   work on larger, more complicated systems yet. The solver still needs alot of work.
   
   Once the system is solved, qubit and coupler weights are reported:
		
		Annealer Encoding:
			w3 	 40.7 	 
			J03 	 -906.5 	 
			J01 	 779.4 	 
			J13 	 -368.4 	 
			J23 	 491.1 	 
			w0 	 972.5 	 
			w1 	 327.7 	 
			J02 	 -991.8 	 
			J12 	 -721.7 	 
			w2 	 394.0 	 
			G 	 0 	 

		Check:
			True 	-	 0 = G
			True 	-	 w0 > G
			True 	-	 w1 > G
			True 	-	 w1 + J01 + w0 > G
			True 	-	 w2 > G
			True 	-	 w2 + J02 + w0 > G
			True 	-	 w2 + J12 + w1 = G
			True 	-	 w2 + J12 + J02 + w1 + J01 + w0 > G
			True 	-	 w3 > G
			True 	-	 w3 + J03 + w0 > G
			True 	-	 w3 + J13 + w1 = G
			True 	-	 w3 + J13 + J03 + w1 + J01 + w0 > G
			True 	-	 w3 + J23 + w2 > G
			True 	-	 w3 + J23 + J03 + w2 + J02 + w0 = G
			True 	-	 w3 + J23 + J13 + w2 + J12 + w1 > G
			True 	-	 w3 + J23 + J13 + J03 + w2 + J12 + J02 + w1 + J01 + w0 > G

		Ancillas added: 1

   Solver functions and classes are implemented in converter/qiskit/solve_sys_multivar_ineq.py

8) *Not yet implemented* Last, a script which runs the found encoding on an annealer will be written by 
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
	  
3) Write script in execute() that creates dwave script with the encoding that was found

4) Implement Fredkin and swap gates.

5) Change README example to an XNOR (NXOR?) to illustrate that this implementation can generate a 
   single annealer encoding for multi-gate circuits

-----------------------------------------------------------------------------------------------------
(II) GATE CIRCUIT-TO-ANNEALER ENCODING BY WAY OF INTERMEDIATE BLOCH SPHERE TRUTHTABLE REPRESENTATION
-----------------------------------------------------------------------------------------------------
Notes:
	
TODO:

-----------------------------------------------------------------------------------------------------
(III) LUMP ANNEALER ENCODING AS COMPOSITE OF SERIAL ANNEALER ENCODINGS
-----------------------------------------------------------------------------------------------------
Notes:

TODO:

```
