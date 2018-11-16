

from ._instruction import Instruction
from ._instructionset import InstructionSet
from ._quantumcircuit import QuantumCircuit
from ._quantumregister import QuantumRegister


class Reset(Instruction):
    pass

    def __init__(self, qubit, circ=None):
        pass

    def reapply(self, circ):
        pass


def reset(self, quantum_register):
    pass


