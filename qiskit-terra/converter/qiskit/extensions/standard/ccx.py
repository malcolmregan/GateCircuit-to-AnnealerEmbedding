# -*- coding: utf-8 -*-

# Copyright 2017, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

"""
Toffoli gate. Controlled-Controlled-X.
"""
from converter.qiskit import Gate
from converter.qiskit import QuantumCircuit
from converter.qiskit._instructionset import InstructionSet
from converter.qiskit._quantumregister import QuantumRegister
from converter.qiskit.extensions.standard import header  # pylint: disable=unused-import


class ToffoliGate(Gate):
    """Toffoli gate."""

    def __init__(self, ctl1, ctl2, tgt, circ=None):
        """Create new Toffoli gate."""
        super().__init__("ccx", [], [ctl1, ctl2, tgt], circ)

    def inverse(self):
        """Invert this gate."""
        return self  # self-inverse

    def reapply(self, circ):
        """Reapply this gate to corresponding qubits in circ."""
        self._modifiers(circ.ccx(self.qargs[0], self.qargs[1], self.qargs[2]))


def ccx(self, ctl1, ctl2, tgt):
    if isinstance(ctl1, QuantumRegister) and \
       isinstance(ctl2, QuantumRegister) and \
       isinstance(tgt, QuantumRegister) and \
       len(ctl1) == len(tgt) and len(ctl2) == len(tgt):
        for i in range(ctl1.size):
            self.ccx((ctl1, i), (ctl2, i), (tgt, i))
        return None


    ############################## Write Dwave CCNOT ##################################

    import os
    import sys
    import __main__
        
    ctl1name = ctl1[0].name + '_' + str(ctl1[1])
    ctl2name = ctl2[0].name + '_' + str(ctl2[1])
    tgtname = tgt[0].name + '_' + str(tgt[1])

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

            
    f.write("####################################################\n"\
            "## CCNOT - control1: {0} control2: {1} target: {2} ##\n"\
            "####################################################\n\n"\
            "if \'{0}\' not in globals():\n"\
            "    {0}=0\n"\
            "if \'{1}\' not in globals():\n"\
            "    {1}=0\n"\
            "if \'{2}\' not in globals():\n"\
            "    {2}=0\n\n"\
            "bqm = dimod.BinaryQuadraticModel({{\'anc1\' : 4, \'anc2\' : 4, \'out{2}\' : 1, \'{2}\' : 1}}, {{(\'anc1\', \'anc2\') : -4, (\'anc1\', \'out{2}\') : 4, "\
            "(\'anc1\',\'{2}\') : -4, (\'anc2\', \'{0}\') : -2, (\'anc2\', \'{1}\') : -2, (\'anc2\', \'out{2}\') : -2, (\'anc2\', \'{2}\') : 2, (\'{0}\', \'{1}\') : 1, "\
            "(\'out{2}\', \'{2}\') : -2}}, 0, dimod.BINARY)\n"\
            "sampler = dimod.ExactSolver()\n"\
            "response = sampler.sample(bqm)\n\n"\
            "for sample, energy in response.data(['sample', 'energy']):\n"\
            "    if sample[\'{0}\']=={0} and sample[\'{1}\']=={1} and sample[\'{2}\']=={2} and int(energy)==0:\n"\
            "        {0}=sample[\'{0}\']\n"\
            "        {1}=sample[\'{1}\']\n"\
            "        {2}=sample[\'out{2}\']\n"\
            "        tgt_before = sample[\'{2}\']\n"
            "        #print(sample, energy)\n"\
            "        break\n\n"\
            "print(\"######################################################\")\n"\
            "print(\"CCNOT operation on {0} (control1), {1} (control2) and {2} (target):\")\n"\
            "print(\"    in:  {0}={{0}}, {1}={{1}}, {2}={{2}}\".format({0},{1},tgt_before))\n"\
            "print(\"    out: {0}={{0}}, {1}={{1}}, {2}={{2}}\".format({0},{1},{2}))\n"\
            "print(\"######################################################\")\n"\
            "print(\"\\n\\n\\n\")\n\n\n".format(ctl1name,ctl2name,tgtname))

    f.close()

    ##################################################################################
                                                                                      
    return None

QuantumCircuit.ccx = ccx
