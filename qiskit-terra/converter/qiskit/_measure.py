# -*- coding: utf-8 -*-

# Copyright 2017, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

"""
Quantum measurement in the computational basis.
"""
from ._instruction import Instruction
from ._instructionset import InstructionSet
from ._quantumcircuit import QuantumCircuit
from ._quantumregister import QuantumRegister
from ._classicalregister import ClassicalRegister


class Measure(Instruction):
    """Quantum measurement in the computational basis."""

    def __init__(self, qubit, bit, circuit=None):
        """Create new measurement instruction."""
        super().__init__("measure", [], [qubit], [bit], circuit)

    def qasm(self):
        """Return OPENQASM string."""
        qubit = self.qargs[0]
        bit = self.cargs[0]
        return self._qasmif("measure %s[%d] -> %s[%d];" % (qubit[0].name,
                                                           qubit[1],
                                                           bit[0].name,
                                                           bit[1]))

    def reapply(self, circuit):
        """Reapply this gate to corresponding qubits."""
        self._modifiers(circuit.measure(self.qargs[0], self.cargs[0]))


def measure(self, qubit, cbit):

    ############################## Dwave 'Measure' ##################################
    if 'writeflag' not in globals():
        global writeflag
        writeflag = 1
    if writeflag==0:

        import os
        import sys
        import __main__

        if sys.argv[-1] == 'dwave':
            tgtname = list()
            if isinstance(qubit,tuple):
                for i in range(qubit[0].size):
                    tgtname.extend([qubit[0].name+'_{}'.format(i)])
            else:
                for i in range(qubit.size):
                    tgtname.extend([qubit.name+'_{}'.format(i)])

            filename = __main__.__file__.split(".")[0]
            filename = filename + "_dwave.py"
        
            #f = open("./{}".format(filename), "r")
            #linelist = f.readlines()
            #f.close()
    
            f = open("./{}".format(filename), "a")
            for i in range(len(tgtname)):
                f.write("print(\"Measurement of {0} => {{0}}\".format({0}))\n"\
                        "\n\n\n".format(tgtname[i]))

            f.close()
            writeflag=1
            #return

    ###############################################################################

    """Measure quantum bit into classical bit (tuples).

    Returns:
        qiskit.Instruction: the attached measure instruction.

    Raises:
        QISKitError: if qubit is not in this circuit or bad format;
            if cbit is not in this circuit or not creg.
    """
    if isinstance(qubit, QuantumRegister) and \
       isinstance(cbit, ClassicalRegister) and len(qubit) == len(cbit):
        instructions = InstructionSet()
        writeflag=0
        for i in range(qubit.size):
            instructions.add(self.measure((qubit, i), (cbit, i)))
        return instructions

    self._check_qubit(qubit)
    self._check_creg(cbit[0])
    cbit[0].check_range(cbit[1])
    return self._attach(Measure(qubit, cbit, self))


QuantumCircuit.measure = measure
