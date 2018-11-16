# -*- coding: utf-8 -*-

# Copyright 2017, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

# pylint: disable=invalid-name

"""
controlled-NOT gate.
"""
from qiskit import Gate
from qiskit import QuantumCircuit
from qiskit._instructionset import InstructionSet
from qiskit._quantumregister import QuantumRegister
from qiskit.extensions.standard import header  # pylint: disable=unused-import


class CnotGate(Gate):
    """controlled-NOT gate."""

    def __init__(self, ctl, tgt, circ=None):
        """Create new CNOT gate."""
        super().__init__("cx", [], [ctl, tgt], circ)

    def inverse(self):
        """Invert this gate."""
        return self  # self-inverse

    def reapply(self, circ):
        """Reapply this gate to corresponding qubits in circ."""
        self._modifiers(circ.cx(self.qargs[0], self.qargs[1]))


def cx(self, ctl, tgt):
    
    ############################## Write Dwave CNOT ##################################
    
    import os
    import sys
    import __main__

    if sys.argv[-1] == 'dwave':

        ctlname = ctl[0].name
        tgtname = tgt[0].name

        filename = __main__.__file__.split(".")[0]
        filename = filename + "_dwave.py"
        if not os.path.exists("./{}".format(filename)):
            f = open("./{}".format(filename), "a")
            f.write("#from dwave.system.samplers import DWaveSampler\n"\
                "#from exact_solver import ExactSolver\n"\
                "#from dwave.cloud.exceptions import SolverOfflineError\n"\
                "#import minorminer\n"\
                "import dimod\n\n")
        else:
            f = open("./{}".format(filename), "a")

        f.write("## CNOT - control: {0} target: {1}\n"\
                "bqm = dimod.BinaryQuadraticModel({{'{0}\' : 1, \'{1}\' : 1, \'out{1}\' : 1, \'anc\' : 4}}, {{(\'{0}\', \'{1}\') : 2, (\'{0}\', \'out{1}\') : -2, (\'{1}\', \'out{1}\') : "\
                "-2, (\'{0}\', \'anc\') : -4, (\'{1}\', \'anc\') : -4, (\'out{1}\', \'anc\') : 4}}, 0, dimod.BINARY)\n"\
                "sampler = dimod.ExactSolver()\n"\
                "response = sampler.sample(bqm)\n"\
                "for sample, energy in response.data(['sample', 'energy']):\n"\
                "    print(sample, energy)\n\n".format(ctlname,tgtname))
        f.close()
        return

    ##################################################################################

    """Apply CX from ctl to tgt."""
    if isinstance(ctl, QuantumRegister) and \
       isinstance(tgt, QuantumRegister) and len(ctl) == len(tgt):
        instructions = InstructionSet()
        for i in range(ctl.size):
            instructions.add(self.cx((ctl, i), (tgt, i)))
        return instructions

    if isinstance(ctl, QuantumRegister):
        gs = InstructionSet()
        for j in range(ctl.size):
            gs.add(self.cx((ctl, j), tgt))
        return gs

    if isinstance(tgt, QuantumRegister):
        gs = InstructionSet()
        for j in range(tgt.size):
            gs.add(self.cx(ctl, (tgt, j)))
        return gs

    self._check_qubit(ctl)
    self._check_qubit(tgt)
    self._check_dups([ctl, tgt])
    return self._attach(CnotGate(ctl, tgt, self))


QuantumCircuit.cx = cx
