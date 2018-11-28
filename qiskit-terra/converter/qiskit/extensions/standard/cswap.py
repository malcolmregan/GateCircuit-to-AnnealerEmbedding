# -*- coding: utf-8 -*-

# Copyright 2017, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

"""
Cswap gate. Fredkin gate - Controlled Swap.
"""
from converter.qiskit import Gate
from converter.qiskit import QuantumCircuit
from converter.qiskit._instructionset import InstructionSet
from converter.qiskit._quantumregister import QuantumRegister
from converter.qiskit.extensions.standard import header  # pylint: disable=unused-import


class FredkinGate(Gate):
    """Cswap gate."""

    def __init__(self, ctl1, tgt1, tgt2, circ=None):
        """Create new Cswap gate."""
        super().__init__("cswap", [], [ctl1, tgt1, tgt2], circ)

    def inverse(self):
        """Invert this gate."""
        return self  # self-inverse

    def reapply(self, circ):
        """Reapply this gate to corresponding qubits in circ."""
        self._modifiers(circ.cswap(self.qargs[0], self.qargs[1], self.qargs[2]))

def cswap(self, ctl1, tgt1, tgt2):
    if isinstance(ctl1, QuantumRegister) and \
       isinstance(tgt1, QuantumRegister) and \
       isinstance(tgt2, QuantumRegister) and \
       len(ctl1) == len(tgt2) and len(tgt1) == len(tgt2):
        for i in range(ctl1.size):
            self.cswap((ctl1, i), (tgt1, i), (tgt2, i))
        return None
    ############################## Write Dwave CSWAP ##################################
    elif isinstance(ctl1, QuantumRegister) and \
       isinstance(tgt1, QuantumRegister) and \
       isinstance(tgt2, QuantumRegister):
       raise("All registers must be of the same size")

    """Apply CSWAP from ctl1 to tgt1 and tgt2."""
    import os
    import sys
    import __main__ as main

    ctl1name = ctl1[0].name + "_" + str(ctl1[1])
    tgt1name = tgt1[0].name + "_" + str(tgt1[1])
    tgt2name = tgt2[0].name + "_" + str(tgt2[1])

    filename = main.__file__.split(".")[0] + "_dwave.py"
    with open(filename, "a") as f:

        f.write("####################################################\n"\
                "## CSWAP - control1: {0} target1: {1} target2: {2} ##\n"\
                "####################################################\n\n"\
                "if \'{0}\' not in globals():\n"\
                "    {0}=0\n"\
                "if \'{1}\' not in globals():\n"\
                "    {1}=0\n"\
                "if \'{2}\' not in globals():\n"\
                "    {2}=0\n\n"\
                "qubit_weights = {{\'{1}\' : 1, \'{2}\' : 1, \'out{1}\' : 1, \'out{2}\' : 1, \'a\' : 6, \'b\' : 6}}\n"\
                "binding_weights = {{(\'{0}\', \'out{1}\') : 2, (\'{0}\', \'out{2}\') : 2, (\'{0}\', \'a\') : -4, (\'{0}\', \'b\') : -4, (\'{1}\', \'out{1}\') : -2, (\'{1}\', \'a\') : 2, (\'{1}\', \'b\') : -2, (\'{2}\', \'out{2}\') : -2, (\'{2}\', \'a\') : -2, (\'{2}\', \'b\') : 2, (\'out{1}\', \'a\') : -4, (\'out{2}\', \'b\') : -4}}\n"\
                "bqm = dimod.BinaryQuadraticModel(qubit_weights, binding_weights, 0, dimod.BINARY)\n"\
                "sampler = dimod.ExactSolver()\n"\
                "response = sampler.sample(bqm)\n\n"\
                "for sample, energy in response.data(['sample', 'energy']):\n"\
                "    if sample[\'{0}\']=={0} and sample[\'{1}\']=={1} and sample[\'{2}\']=={2} and int(energy)==0:\n"\
                "        {0}=sample[\'{0}\']\n"\
                "        {1}=sample[\'out{1}\']\n"\
                "        {2}=sample[\'out{2}\']\n"\
                "        tgt1_before = sample[\'{1}\']\n"\
                "        tgt2_before = sample[\'{2}\']\n"\
                "        #print(sample, energy)\n"\
                "        break\n\n"\
                "print(\"######################################################\")\n"\
                "print(\"CSWAP operation on {0} (control1), {1} (target1) and {2} (target2):\")\n"\
                "print(\"    in:  {0}={{0}}, {1}={{1}}, {2}={{2}}\".format({0},tgt1_before,tgt2_before))\n"\
                "print(\"    out: {0}={{0}}, {1}={{1}}, {2}={{2}}\".format({0},{1},{2}))\n"\
                "print(\"######################################################\")\n"\
                "print(\"\\n\\n\\n\")\n\n\n".format(ctl1name, tgt1name, tgt2name))

    ##################################################################################
    return None

QuantumCircuit.cswap = cswap
