








import sympy

from ._qiskiterror import QISKitError
from ._quantumregister import QuantumRegister
from ._classicalregister import ClassicalRegister


class Instruction(object):
    pass

    def __init__(self, name, param, qargs, cargs, circuit=None):
        pass



    def check_circuit(self):
        pass

    def c_if(self, classical, val):
        pass

    def _modifiers(self, gate):
        pass

    def _qasmif(self, string):
        pass

    def qasm(self):
        pass


