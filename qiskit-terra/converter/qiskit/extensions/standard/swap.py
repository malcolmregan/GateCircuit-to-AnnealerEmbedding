# -*- coding: utf-8 -*-

# Copyright 2017, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

"""
swap gate.
"""
from converter.qiskit import Gate
from converter.qiskit import QuantumCircuit
from converter.qiskit._instructionset import InstructionSet
from converter.qiskit._quantumregister import QuantumRegister
from converter.qiskit.extensions.standard import header  # pylint: disable=unused-import


class SwapGate(Gate):
    """swap gate."""

    def __init__(self, ctl, tgt, circ=None):
        """Create new SWAP gate."""
        super().__init__("swap", [], [ctl, tgt], circ)

    def inverse(self):
        """Invert this gate."""
        return self  # self-inverse

    def reapply(self, circ):
        """Reapply this gate to corresponding qubits in circ."""
        self._modifiers(circ.swap(self.qargs[0], self.qargs[1]))



def swap(self, ctl, tgt):
    """Apply SWAP from ctl to tgt."""
    if isinstance(ctl, QuantumRegister) and \
            isinstance(tgt, QuantumRegister) and len(ctl) == len(tgt):
        instructions = InstructionSet()
        for j in range(ctl.size):
            instructions.add(self.swap((ctl, j), (tgt, j)))
        return instructions

    self._check_qubit(ctl)
    self._check_qubit(tgt)
    self._check_dups([ctl, tgt])
    return self._attach(SwapGate(ctl, tgt, self))




    ############################## Write Dwave SWAP ##################################
    elif isinstance(ctl, QuantumRegister) and \
       isinstance(tgt, QuantumRegister):
       raise("All registers must be of the same size")

    import os
    import sys
    import __main__ as main

    ctlname = ctl[0].name + "_" + str(ctl[1])
    tgtname = tgt[0].name + "_" + str(tgt[1])

    filename = main.__file__.split(".")[0] + "_dwave.py"
    with open(filename, "a") as f:

        f.write("####################################################\n"\
                "## SWAP - control: {1} target: {2} ##\n"\
                "####################################################\n\n"\
                #"if \'{0}\' not in globals():\n"\
                #"    {0}=1\n"\
                "     c=1\n"\
                "if \'{0}\' not in globals():\n"\
                "    {0}=0\n"\
                "if \'{1}\' not in globals():\n"\
                "    {1}=0\n\n"\
                "qubit_weights = {{\'{0}\' : 1, \'{1}\' : 1, \'out{0}\' : 1, \'out{1}\' : 1, \'a\' : 6, \'b\' : 6}}\n"\
                "binding_weights = {{(\'c\', \'out{0}\') : 2,(\'c\',\'out{1}\') : 2, (\'c\', \'a\') : -4, (\'c\', \'b\') : -4, (\'{0}\', \'out{0}\') : -2, (\'{0}\', \'a\') : 2, (\'{0}\', \'b\') : -2, (\'{1}\', \'out{1}\') : -2, (\'{1}\', \'a\') : -2, (\'{1}\', \'b\') : 2, (\'out{0}\', \'a\') : -4, (\'out{1}\', \'b\') : -4}}\n"\
                "bqm = dimod.BinaryQuadraticModel(qubit_weights, binding_weights, 0, dimod.BINARY)\n"\
                "sampler = dimod.ExactSolver()\n"\
                "response = sampler.sample(bqm)\n\n"\
                "for sample, energy in response.data(['sample', 'energy']):\n"\
                "    if sample[\'c\']==c and sample[\'{0}\']=={0} and sample[\'{1}\']=={1} and int(energy)==0:\n"\
                "        c=sample[\'c\']\n"\
                "        {0}=sample[\'out{0}\']\n"\
                "        {1}=sample[\'out{1}\']\n"\
                "        tgt1_before = sample[\'{0}\']\n"\
                "        tgt2_before = sample[\'{1}\']\n"\
                "        #print(sample, energy)\n"\
                "        break\n\n"\
                "print(\"######################################################\")\n"\
                "print(\"SWAP operation on {0} (control), {1} (target):\")\n"\
                "print(\"    in:  {0}={{0}}, {1}={{1}}\".format(tgt1_before,tgt2_before))\n"\
                "print(\"    out: {0}={{0}}, {1}={{1}}\".format({0},{1}))\n"\
                "print(\"######################################################\")\n"\
                "print(\"\\n\\n\\n\")\n\n\n".format(ctl1name, tgt1name))

    ##################################################################################
    return None

QuantumCircuit.swap = swap
