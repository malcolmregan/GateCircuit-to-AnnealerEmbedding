# -*- coding: utf-8 -*-

# Copyright 2017, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

# pylint: disable=invalid-name

"""
Hadamard.
"""
from converter.qiskit import Gate
from converter.qiskit import InstructionSet
from converter.qiskit import QuantumCircuit
from converter.qiskit import QuantumRegister
from converter.qiskit.extensions.standard import header  # pylint: disable=unused-import
import numpy as np

class HGate(Gate):

    def __init__(self, qubit, circ=None):
        """Create new X gate."""
        print(circ)
        super().__init__("h", [], [qubit], circ)
        
    def inverse(self):
        """Invert this gate."""
        return self  # self-inverse

    def reapply(self, circ):
        """Reapply this gate to corresponding qubits in circ."""
        self._modifiers(circ.h(self.qargs[0]))

def h(self, q):
    if isinstance(q, QuantumRegister):
        for j in range(q.size):
            self.h((q, j))
        return None

    tgtnames = list()
    for theta in [0,1]:
        tgtnames.append(q[0].name + "_" + str(q[1]) + "_theta_" + str(theta) + "_out")
    for phi in [0,1]:
        tgtnames.append(q[0].name + "_" + str(q[1]) + "_phi_" + str(phi) + "_out")
    
    tgtcolumns = list()
    for i in range(len(tgtnames)):
        tgtcolumns.append(self.truthtable.inputnames.index(tgtnames[i]))

    othercolumns = list()
    for i in range(self.truthtable.numinputs):
        if not i in tgtcolumns:
            othercolumns.append(i)

    outputidxs = list()
    for i in range(len(self.truthtable.outputs)):
        if self.truthtable.outputs[i] == 1:
            outputidxs.append(i)

    self.truthtable.outputs[outputidxs] = 0
    for row in outputidxs:
        staysame = self.truthtable.graycode[row,othercolumns]
        for k in range(len(self.truthtable.outputs)):
            if np.array_equal(staysame, self.truthtable.graycode[k,othercolumns]) and not k == row:
                self.truthtable.outputs[k] = 1
   

    '''
    t1 t0 p1 p0    H     t1 t0 p1 p0
    0  0  0  0   ====>   0  1  0  0  
    0  0  0  1   ====>   0  1  0  0 <-, 
    0  0  1  0   ====>   0  1  0  0 <--,
    0  0  1  1   ====>   0  1  0  0 <---,
    0  1  0  0   ====>   0  0  0  0      ',
    0  1  0  1   ====>   0  1  1  1        ',       These rows
    0  1  1  0   ====>   1  0  0  0          ',     don't matter
    0  1  1  1   ====>   0  1  0  1            :--> find better  
    1  0  0  0   ====>   0  1  1  0          .'     way to represent
    1  0  0  1   ====>   0  1  1  0 <-------'       qubit on Bloch sphere 
    1  0  1  0   ====>   0  1  1  0 <------'        
    1  0  1  1   ====>   0  1  1  0 <-----'
    1  1  0  0   ====>   1  0  0  0 <----'
    1  1  0  1   ====>   1  1  1  1 <---'
    1  1  1  0   ====>   0  0  0  0 <--'
    1  1  1  1   ====>   1  1  0  1 <-'
    '''





























    #print("x on {}".format(tgtname))
    #for i in range(len(self.truthtable.outputs)):
    #    print(self.truthtable.graycode[i], self.truthtable.outputs[i])
    #print("\n") 

QuantumCircuit.h = h
