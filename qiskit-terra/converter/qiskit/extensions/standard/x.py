# -*- coding: utf-8 -*-

# Copyright 2017, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

# pylint: disable=invalid-name

"""
Pauli X (bit-flip) gate.
"""
from converter.qiskit import Gate
from converter.qiskit import InstructionSet
from converter.qiskit import QuantumCircuit
from converter.qiskit import QuantumRegister
from converter.qiskit.extensions.standard import header  # pylint: disable=unused-import


class XGate(Gate):
    """Pauli X (bit-flip) gate."""

    def __init__(self, qubit, circ=None):
        """Create new X gate."""
        super().__init__("x", [], [qubit], circ)

    def inverse(self):
        """Invert this gate."""
        return self  # self-inverse

    def reapply(self, circ):
        """Reapply this gate to corresponding qubits in circ."""
        self._modifiers(circ.x(self.qargs[0]))




def x(self, q):
    if isinstance(q, QuantumRegister):
        for j in range(q.size):
            self.x((q, j))
        return None

    ############################## Write Dwave NOT ##################################
    import os
    import sys
    import __main__
        

    tgtname = q[0].name + "_" + str(q[1])

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
         
    f.write("#######################\n"\
            "## NOT - target: {0} ##\n"\
            "#######################\n\n"\
            "if \'{0}\' not in globals():\n"\
            "    {0}=0\n\n"\
            "bqm = dimod.BinaryQuadraticModel({{\'{0}\' : -4, \'out{0}\' : -4}}, {{(\'{0}\', \'out{0}\') : 8}}, 4, dimod.BINARY)\n"\
            "sampler = dimod.ExactSolver()\n"\
            "response = sampler.sample(bqm)\n\n"\
            "for sample, energy in response.data(['sample', 'energy']):\n"\
            "    if sample[\'{0}\']=={0} and int(energy)==0:\n"\
            "        {0}=sample[\'out{0}\']\n"\
            "        tgt_before = sample[\'{0}\']\n"
            "        #print(sample, energy)\n"\
            "        break\n\n"\
            "print(\"######################################################\")\n"\
            "print(\"NOT operation on {0}:\")\n"\
            "print(\"    in:  {0}={{0}}\".format(tgt_before))\n"\
            "print(\"    out: {0}={{0}}\".format({0}))\n"\
            "print(\"######################################################\")\n"\
            "print(\"\\n\\n\\n\")\n\n\n".format(tgtname))
        
    f.close()

    ##################################################################################
    return None

QuantumCircuit.x = x
