

from ._instruction import Instruction
from ._instructionset import InstructionSet
from ._quantumcircuit import QuantumCircuit
from ._quantumregister import QuantumRegister
from ._classicalregister import ClassicalRegister


class Measure(Instruction):
    pass

    def __init__(self, qubit, bit, circuit=None):
        pass

    def qasm(self):
        pass

    def reapply(self, circuit):
        pass


def measure(self, qubit, cbit):
    pass





